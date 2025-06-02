#apiyfinance.py
import yfinance as yf
import random
import math

tickers_top = [
    "MSFT", "NVDA", "AAPL", "AMZN", "GOOGL",
    "META", "AVGO", "TSLA", "BRK-B", "TSM",
    "WMT", "JPM", "V", "LLY", "MA",
    "NFLX", "ORCL", "COST", "XOM", "PG",
    "JNJ", "HD", "SAP", "BAC", "ABBV",
    "PLTR", "KO", "SPY", "QQQ", "DIA",
    "IWM", "VTI", "VEA", "VWO", "TLT",
    "GLD", "XLF", "XLE", "XLV", "XLK",
    "XLY", "XLU", "AXP", "CRM", "INTC",
    "CSCO", "PEP", "MCD", "DIS", "NKE",
    "BA", "GS", "UPS", "CAT", "CVX",
    "IBM", "GE", "ADBE", "HON", "MDT",
    "UNH", "PFE"
]

def obtener_datos_accion(ticker):
    accion = yf.Ticker(ticker)
    info = accion.info

    datos = {
        "ticker": ticker,
        "nombre": info.get("shortName"),
        "precio_actual": info.get("regularMarketPrice"),
        "variacion_pct": info.get("regularMarketChangePercent"),
        "max_dia": info.get("dayHigh"),
        "min_dia": info.get("dayLow"),
        "max_historico": accion.history(period="max")["High"].max(),
        "capitalizacion_bursatil": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "rendimiento_dividendos": info.get("dividendYield"),
        "sector": info.get("sector"),
        "recomendacion": info.get("recommendationKey"),
    }

    return datos

def generar_alerta(datos):
    precio_actual = datos["precio_actual"]
    max_historico = datos["max_historico"]
    recomendacion = datos["recomendacion"]

    if recomendacion in ["buy", "strongBuy"] and precio_actual < 0.8 * max_historico:
        PE = math.floor(precio_actual)
        SL_pct = -random.uniform(6, 14) / 100
        SL = math.floor(PE * (1 + SL_pct))
        R = abs(SL_pct)

        TP1 = math.floor(PE * (1 + R * 0.9))
        TP2 = math.floor(PE * (1 + R * 1.8))
        TP3 = math.floor(PE * (1 + R * 2.6))

        mensaje = f"""
📢 *ALERTA ANÁLISIS* // ESPECULATIVO 
👉🏼 Perfil Agresivo❗
•Ticker: *{datos['ticker']}* ({datos['nombre']}) 🇦🇷🇺🇸
•Zona de compra: {PE} USD
⛔ STOP LOSS = *{round(SL_pct * 100)}%*
✅ DESARMES: ( {TP1} USD / {TP2} USD / {TP3} USD )
- - - - - - - - - - - - - - - - - - - - - - 
Recuerde operar bajo su propio riesgo y en la justa y considerada proporción de su cartera. (la misma no configura ninguna recomendación)
"""
        return mensaje.strip()
    else:
        return None

def generar_alerta_aleatoria():
    """Busca en la lista tickers_top alguna acción que cumpla y devuelve mensaje o None."""
    import random
    import time

    tickers_restantes = tickers_top.copy()
    random.shuffle(tickers_restantes)

    for ticker in tickers_restantes:
        try:
            datos = obtener_datos_accion(ticker)
            mensaje = generar_alerta(datos)
            if mensaje:
                return mensaje
            time.sleep(1)  # para no saturar requests
        except Exception as e:
            print(f"Error con {ticker}: {e}")
    return None

# Si quieres probar el script directamente
if __name__ == "__main__":
    alerta = generar_alerta_aleatoria()
    if alerta:
        print(alerta)
    else:
        print("No hay alertas en este momento.")
