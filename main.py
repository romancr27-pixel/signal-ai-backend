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
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": pair,
        "interval": "1min",
        "outputsize": 100,
        "apikey": API_KEY
    }
    r = requests.get(url, params=params)
    data = r.json()
    
    if "values" not in data:
        return None
    
    df = pd.DataFrame(data["values"])
    df = df.iloc[::-1].reset_index(drop=True)
    df["close"] = df["close"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    return df

@app.get("/signal")
def get_signal(pair: str = "EUR/USD"):
    df = get_candles(pair)
    
    if df is None:
        return {"error": "Не вдалося отримати дані"}
    
    # Індикатори
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
        "rsi": round(last["rsi"], 1)
    }
