#envioWhatsapp.py
import pywhatkit
import pyautogui
import pyperclip
import datetime
import ctypes
import time
from mensajes.mensajeCotizacionesDolar import generar_cotizacion_dolar
from mensajes.mensajeNoticias import generar_noticia_mercado
from mensajes.mensajeAlertaCompra import generar_alerta_aleatoria
from mensajes.mensajeAlertaCompraArg import generar_alerta_aleatoria_arg

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_AWAYMODE_REQUIRED = 0x00000040

ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED)

nombre_grupo = "I22BQXw1eO45eh2ee83WuZ"

mensajes_semana = [
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "10:55", "mensaje": "noticia_mercado"},
    {"dias": ["friday"], "hora": "13:30", "mensaje": "💰 ¡No te olvides de caucionar lo líquido este finde semana!"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:00", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:03", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:06", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:09", "mensaje": "alerta_bursatil_arg"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:12", "mensaje": "alerta_bursatil_arg"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:15", "mensaje": "alerta_bursatil_arg"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "15:00", "mensaje": "cotizacion_dolar"},
]

mensajes_fecha = [
    {"fecha": "13/06/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El lunes 17/06 la Bolsa de Buenos Aires estará cerrada por el feriado en conmemoración del Gral. Güemes."},
    {"fecha": "18/06/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El jueves 19/06 la Bolsa de Nueva York estará cerrada por Juneteenth.\nEl viernes 20/06 la Bolsa de Buenos Aires estará cerrada por el Paso a la Inmortalidad del Gral.  Belgrano."},
    {"fecha": "02/07/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El jueves 03/07 la Bolsa de Nueva York cerrará temprano a las 13:00 por el Día de Independencia.\nEl viernes 04/07 estará cerrada por el mismo motivo."},
    {"fecha": "08/07/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El lunes 09/06 la Bolsa de Buenos Aires estará cerrada por el feriado del Día de la Independencia."},
    {"fecha": "14/08/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El lunes 15/08 la Bolsa de Buenos Aires estará cerrada por el feriado en honor al Gral. San Martín."},
    {"fecha": "29/08/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El lunes 01/09 la Bolsa de Nueva York estará cerrada por el feriado del Día del Trabajo."},
    {"fecha": "20/11/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El viernes 21/11 y el lunes 24/11 la Bolsa de Buenos Aires estará cerrada por el feriado del Día de la Soberanía Nacional."},
    {"fecha": "26/11/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El jueves 27/11 la Bolsa de Nueva York estará cerrada por el Día de Acción de Gracias.\nEl viernes 28/11 cerrará temprano a las 13:00 por el mismo motivo."},
    {"fecha": "05/12/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El lunes 08/12 la Bolsa de Buenos Aires estará cerrada por el feriado de la Inmaculada Concepción."},
    {"fecha": "23/12/2025 12:20", "mensaje": "📢 *Aviso Feriado:*\n" "El martes 24/12 la Bolsa de Nueva York cerrará temprano a las 13:00 hs por la víspera de Navidad.\n""El miércoles 25/12 Las Bolsas de Nueva York y Buenos Aires permanecerán cerradas por el feriado de Navidad."},
    {"fecha": "19/06/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 20/06, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 19/06) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "17/07/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 18/07, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 17/07) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "14/08/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 15/08, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 14/08) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "18/09/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 19/09, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 18/09) a las 15:30 hs y ejercerse en cualquier momento."}, 
    {"fecha": "16/10/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 17/10, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 16/10) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "20/11/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 21/11, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 20/11) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "18/12/2025 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 19/12, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 18/12) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "15/01/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 16/01, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 15/01) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "19/02/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 20/02, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 19/02) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "19/03/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 20/03, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 19/03) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "16/04/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 17/04, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 16/04) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "14/05/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 15/05, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 14/05) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "18/06/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 19/06, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 18/06) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "16/07/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 17/07, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 16/07) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "20/08/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 21/08, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 20/08) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "17/09/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 18/09, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 17/09) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "15/10/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 16/10, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 15/10) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "19/11/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 20/11, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 19/11) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "17/12/2026 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 18/12, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 17/12) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "14/01/2027 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 15/01, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 14/01) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "18/02/2027 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 19/02, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 18/02) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "18/03/2027 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 19/03, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 18/03) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "15/04/2027 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 16/04, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 15/04) a las 15:30 hs y ejercerse en cualquier momento."},
    {"fecha": "20/05/2027 12:30", "mensaje": "📢 *Vencimiento de Opciones*\n📅 Mañana, viernes 21/05, se produce el vencimiento mensual de opciones.\n⚠️ Recuerde que pueden negociarse hasta hoy (jueves 20/05) a las 15:30 hs y ejercerse en cualquier momento."},
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
            elif item["mensaje"] == "alerta_bursatil_arg":
                mensaje_final = generar_alerta_aleatoria_arg()
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
