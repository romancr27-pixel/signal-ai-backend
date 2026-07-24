from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd
import ta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "4142e36f34764df196bfcbbba0cb9df9"

def get_candles(pair: str):
    symbols_to_try = [pair, pair.replace("/", "")]
    
    for symbol in symbols_to_try:
        url = "https://api.twelvedata.com/time_series"
        params = {
            "symbol": symbol,
            "interval": "1min",
            "outputsize": 30,          # ще менше навантаження
            "apikey": API_KEY
        }
        
        try:
            r = requests.get(url, params=params, timeout=10)
            data = r.json()
            
            if "values" in data:
                df = pd.DataFrame(data["values"])
                df = df.iloc[::-1].reset_index(drop=True)
                df["close"] = df["close"].astype(float)
                df["high"] = df["high"].astype(float)
                df["low"] = df["low"].astype(float)
                return df
            
            if "message" in data:
                return {"error_msg": data["message"]}
                
        except Exception as e:
            continue
    
    return None

@app.get("/signal")
def get_signal(pair: str = "EUR/USD"):
    result = get_candles(pair)
    
    if result is None:
        return {"error": "Не вдалося отримати дані"}
    
    if isinstance(result, dict) and "error_msg" in result:
        return {"error": result["error_msg"]}
    
    df = result
    
    df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd_diff()
    bb = ta.volatility.BollingerBands(df["close"])
    df["bb_high"] = bb.bollinger_hband()
    df["bb_low"] = bb.bollinger_lband()
    
    last = df.iloc[-1]
    prev = df.iloc[-2]
    
    signal = "WAIT"
    confidence = 50
    
    if last["rsi"] < 32 and last["close"] <= last["bb_low"] and last["macd"] > prev["macd"]:
        signal = "CALL"
        confidence = min(92, 70 + int(32 - last["rsi"]))
    elif last["rsi"] > 68 and last["close"] >= last["bb_high"] and last["macd"] < prev["macd"]:
        signal = "PUT"
        confidence = min(92, 70 + int(last["rsi"] - 68))
    
    return {
        "pair": pair,
        "direction": signal,
        "confidence": confidence,
        "rsi": round(float(last["rsi"]), 1)
    }
