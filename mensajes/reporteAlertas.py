#reporteAlertas.py
import yfinance as yf
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

SHEET_ID = "1Z9gfXGPdhBktLMwAIj4KpJ5SI2hDKK5lXG2Z63DaMSI"

def conectar_gsheet(sheet_id):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    ruta_credenciales = os.path.join(os.path.dirname(__file__), "credenciales.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(ruta_credenciales, scope)
    client = gspread.authorize(creds)
    return client.open_by_key(sheet_id).sheet1

def procesar_fila(fecha_alerta_str, ticker, precio_alerta_str, stop_loss_str):
    try:
        fecha_inicio = datetime.datetime.strptime(fecha_alerta_str, "%Y-%m-%d").date()
        fecha_fin = datetime.date.today()

        # Conversión segura
        precio_alerta = float(precio_alerta_str.replace(",", "."))
        stop_loss = float(stop_loss_str.replace(",", "."))

        datos = yf.Ticker(ticker)
        historico = datos.history(start=fecha_inicio, end=fecha_fin + datetime.timedelta(days=1))

        if historico.empty:
            print(f"⚠️ Sin datos para {ticker} desde {fecha_alerta_str}")
            return "", "", "Sin datos"

        minimo = round(historico["Low"].min(), 2)
        precio_actual = round(historico["Close"].iloc[-1], 2)

        if minimo < stop_loss:
            analisis = "Saltó el SL"
        else:
            cambio_pct = ((precio_actual - precio_alerta) / precio_alerta) * 100
            analisis = round(cambio_pct / 100, 4)

        return minimo, precio_actual, analisis

    except Exception as e:
        print(f"⚠️ Error con {ticker} en fecha {fecha_alerta_str}: {e}")
        return "", "", "Error"

def completar_columnas(sheet_id):
    sheet = conectar_gsheet(sheet_id)
    datos = sheet.get_all_values()

    for i, fila in enumerate(datos[1:], start=2):  # salta encabezado
        if len(fila) < 4 or not all(fila[:4]):
            continue

        fecha, ticker, precio_alerta, stop_loss = fila[:4]
        minimo, precio_actual, analisis = procesar_fila(fecha, ticker, precio_alerta, stop_loss)

        if minimo != "":
            sheet.update([[minimo, precio_actual, analisis]], f"E{i}:G{i}")
            print(f"✅ Fila {i} actualizada")
        else:
            print(f"⚠️ Fila {i} no se pudo procesar")

if __name__ == "__main__":
    completar_columnas(SHEET_ID)
