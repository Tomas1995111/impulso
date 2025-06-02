#envioWhatsapp.py
import pywhatkit
import pyautogui
import pyperclip
import datetime
import time
from mensajes.mensajeCotizacionesDolar import generar_cotizacion_dolar
from mensajes.mensajeNoticias import generar_noticia_mercado
from mensajes.mensajeAlertaCompra import generar_alerta_aleatoria

nombre_grupo = "I22BQXw1eO45eh2ee83WuZ"

mensajes_semana = [
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "10:55", "mensaje": "noticia_mercado"},
    {"dias": ["friday"], "hora": "13:30", "mensaje": "💰 ¡No te olvides de caucionar lo líquido este finde semana!"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:00", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:05", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:10", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:20", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "15:00", "mensaje": "cotizacion_dolar"},
]

mensajes_fecha = [
    {"fecha": "02/06/2025 01:08", "mensaje": "Mensaje especial .........."},
]

def enviar_mensaje(texto):
    print(f"🔔 Enviando mensaje: {texto}")
    pywhatkit.sendwhatmsg_to_group_instantly(nombre_grupo, "", wait_time=10, tab_close=False)
    time.sleep(3)
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "w")

print("Bot iniciado. Esperando el horario correcto...")

while True:
    ahora = datetime.datetime.now()
    dia_actual = ahora.strftime("%A").lower()
    hora_actual = ahora.strftime("%H:%M")
    fecha_actual = ahora.strftime("%d/%m/%Y %H:%M")

    # Mensajes por día de la semana
    for item in mensajes_semana:
        if dia_actual in item["dias"] and hora_actual == item["hora"]:
            if item["mensaje"] == "cotizacion_dolar":
                mensaje_final = generar_cotizacion_dolar()
            elif item["mensaje"] == "noticia_mercado":
                mensaje_final = generar_noticia_mercado()
            elif item["mensaje"] == "alerta_bursatil":
                mensaje_final = generar_alerta_aleatoria()
            else:
                mensaje_final = item["mensaje"]

            if "[!] Error" in mensaje_final:
                print(mensaje_final)  # Solo se muestra en consola
            else:
                enviar_mensaje(mensaje_final)

    # Mensajes por fecha específica
    for item in mensajes_fecha:
        if fecha_actual == item["fecha"]:
            enviar_mensaje(item["mensaje"])

    # Esperar hasta el siguiente minuto
    segundos_restantes = 60 - ahora.second
    time.sleep(segundos_restantes)
