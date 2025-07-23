import time
import os
import subprocess

# 🕒 Variables de tiempo
TIEMPO_INICIAL = 3 * 60
TIEMPO_ENTRE_REVISIONES = 12 * 60

# 📄 Rutas
LOG_BOT_PATH = r"C:\Users\Tomas\OneDrive\Escritorio\Proyectos\impulso_wsp_bot\LogVM\log_bot.log"
LOG_WATCHDOG_PATH = r"C:\Users\Tomas\OneDrive\Escritorio\Proyectos\impulso_wsp_bot\LogVM\watchdog.log"

# 🖥 Comando reinicio VM
REINICIAR_VM_CMD = [
    r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe",
    "controlvm", "Impulso", "reset"
]

# 💾 Log simple
def escribir_log(mensaje):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
    with open(LOG_WATCHDOG_PATH, "a", encoding="utf-8") as f:
        f.write(timestamp + mensaje + "\n")
    print(timestamp + mensaje)

# 🧠 Leer últimas N líneas del log
def leer_ultimas_lineas(path, n=5):
    try:
        with open(path, "rb") as f:
            f.seek(0, os.SEEK_END)
            end = f.tell()
            buffer = bytearray()
            lines = []
            while end > 0 and len(lines) < n:
                end -= 1
                f.seek(end)
                byte = f.read(1)
                if byte == b'\n':
                    if buffer:
                        lines.append(buffer[::-1].decode("utf-8", errors="ignore").strip())
                        buffer = bytearray()
                else:
                    buffer.append(byte[0])
            if buffer:
                lines.append(buffer[::-1].decode("utf-8", errors="ignore").strip())
            return lines[::-1]
    except Exception as e:
        escribir_log(f"❌ Error leyendo log: {e}")
        return []

# 🧹 Rotar si el log pesa mucho
def limpiar_log_si_pesa(path, max_mb=10, ultimas_lineas=1000):
    try:
        if os.path.getsize(path) > max_mb * 1024 * 1024:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                lineas = f.readlines()[-ultimas_lineas:]
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lineas)
            escribir_log(f"🧹 Log limpiado (>{max_mb}MB, {ultimas_lineas} líneas conservadas).")
    except Exception as e:
        escribir_log(f"❌ Error al limpiar log: {e}")

# ⏳ Inicio
escribir_log("⌛ Esperando inicio del sistema...")
time.sleep(TIEMPO_INICIAL)
escribir_log("🚀 Watchdog iniciado correctamente.")

# 🔁 Loop principal
while True:
    limpiar_log_si_pesa(LOG_BOT_PATH)

    lineas_antes = leer_ultimas_lineas(LOG_BOT_PATH)
    time.sleep(TIEMPO_ENTRE_REVISIONES)
    lineas_despues = leer_ultimas_lineas(LOG_BOT_PATH)

    if lineas_despues == lineas_antes:
        escribir_log("🟥 El bot no avanzó. Reiniciando VM...")
        try:
            subprocess.run(REINICIAR_VM_CMD, check=True)
            escribir_log("🔁 VM reiniciada correctamente.")
        except Exception as e:
            escribir_log(f"❌ Error reiniciando VM: {e}")
    else:
        escribir_log("✅ Bot activo.")
