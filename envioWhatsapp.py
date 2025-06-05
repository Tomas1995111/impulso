#envioWhatsapp.py
import pywhatkit
import pyautogui
import pyperclip
import datetime
import ctypes
import time
from mensajes.mensajeCotizacionesDolar import generar_cotizacion_dolar
from mensajes.mensajeResumen import generar_mensaje_resumen
from mensajes.mensajeAlertaCompra import generar_alerta_aleatoria
from mensajes.mensajeAlertaCompraArg import generar_alerta_aleatoria_arg

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_AWAYMODE_REQUIRED = 0x00000040

ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED)

nombre_grupo = "I22BQXw1eO45eh2ee83WuZ"

mensajes_semana = [
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "09:00", "mensaje": "noticia_mercado"},
    {"dias": ["thursday", "friday"], "hora": "13:30", "mensaje": "💰 ¡No te olvides de caucionar lo líquido este finde semana!"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:02", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:04", "mensaje": "alerta_bursatil"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:06", "mensaje": "alerta_bursatil_arg"},
    {"dias": ["monday", "tuesday", "wednesday", "thursday", "friday"], "hora": "11:08", "mensaje": "alerta_bursatil_arg"},
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
    {"fecha": "05/06/2025 14:30", "mensaje": "📚 *Jueves de educación financiera*\n🧠 *Mini clase: ¿Qué es un ETF?*\n\nHola Impulsores! les dejamos una explicación breve y clave 👇\n\n🔹 *¿Qué es un ETF?*\nEs un fondo que agrupa muchas acciones o activos (como el S&P 500, bonos, materias primas, etc.) y se compra como si fuera una acción individual.\n\n✅ *Permiten invertir en índices, sectores o regiones*\n✅ *Tienen baja comisión y alta liquidez*\n✅ *Podés acceder a una cartera diversificada en una sola operación*\n✅ *Se operan como cualquier acción, en tiempo real*\n\n📊 *Ideal para diversificar y seguir una estrategia sin elegir activos uno por uno.*"},
    {"fecha": "11/06/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es una acción?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una *explicación breve y clave* 👇\n\n🔹 *¿Qué es una acción?*\n*Es una parte de propiedad de una empresa* que podés comprar y vender en la bolsa.\n\n✅ *Ser dueño de una acción significa ser socio de la empresa*\n✅ *Podés ganar plata si la empresa crece y su valor sube*\n✅ *Algunas acciones pagan dividendos* (ganancias distribuidas)\n✅ *Se negocian en mercados organizados* y su precio varía según oferta y demanda\n\n*📊 Ideal para quienes buscan crecimiento y participar en el éxito de las empresas.*"},
    {"fecha": "18/06/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la tasa de interés?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la tasa de interés?\nEs el porcentaje que se paga por prestar dinero o el rendimiento que genera una inversión.\n\n✅ Afecta préstamos, ahorros e inversiones\n✅ Una tasa alta puede incentivar el ahorro y encarecer créditos\n✅ Una tasa baja puede estimular el consumo y la inversión\n✅ Clave para entender cómo funciona la economía\n\n*📊 Ideal para saber cómo impacta en tus finanzas personales e inversiones.*"},
    {"fecha": "25/06/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un bono?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un bono?\nEs un título de deuda que emite un gobierno o empresa para pedir plata prestada y, a cambio, paga intereses periódicos.\n\n✅ Recibís pagos de interés fijos o variables\n✅ Al vencimiento, te devuelven el capital invertido\n✅ Son una opción más segura que las acciones\n✅ Se usan para diversificar y generar ingresos estables\n\n*📊 Ideal para quienes buscan menor riesgo y rendimientos predecibles.*"},
    {"fecha": "02/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la diversificación?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la diversificación?\nEs repartir tus inversiones en diferentes activos para reducir riesgos.\n\n✅ No poner todos los huevos en la misma canasta\n✅ Protege tu dinero de caídas fuertes en un activo\n✅ Mejora la estabilidad y el rendimiento a largo plazo\n✅ Clave para una estrategia de inversión segura\n\n*📊 Ideal para minimizar riesgos y maximizar oportunidades.*"},
    {"fecha": "02/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es una cartera de inversión?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es una cartera de inversión?\nEs el conjunto de activos financieros que una persona tiene para diversificar y balancear riesgos y ganancias.\n\n✅ Combina acciones, bonos, fondos y otros activos\n✅ Ayuda a equilibrar rentabilidad y seguridad\n✅ Se ajusta según tus objetivos y perfil de riesgo\n✅ Clave para gestionar tu dinero de forma inteligente\n\n*📊 Ideal para construir un camino sólido hacia tus metas financieras.*"},
    {"fecha": "02/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el trading vs la inversión?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el trading?\nComprar y vender activos en plazos cortos para aprovechar movimientos rápidos de precios.\n\n🔹 ¿Qué es la inversión?\nComprar activos para mantenerlos a largo plazo buscando crecimiento y ganancias sostenidas.\n\n✅ Trading: más riesgo y necesidad de estar atento\n✅ Inversión: enfoque en objetivos a largo plazo\n✅ Cada uno tiene su lugar según perfil y tiempo disponible\n✅ Es importante elegir lo que mejor se adapte a vos\n\n*📊 Ideal para entender cómo manejar tu dinero según tus objetivos.*"},
    {"fecha": "09/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un fondo mutuo?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un fondo mutuo?\nEs un vehículo de inversión donde muchas personas juntan su dinero para invertir en conjunto en acciones, bonos u otros activos.\n\n✅ Administrado por profesionales que eligen las mejores inversiones\n✅ Permite diversificar incluso con poco dinero\n✅ Es más accesible y menos riesgoso que invertir solo\n✅ Podés comprar y vender participaciones fácilmente\n\n*📊 Ideal para quienes quieren invertir sin preocuparse por elegir activos específicos.*"},
    {"fecha": "16/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un índice bursátil?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un índice bursátil?\nEs un indicador que agrupa un conjunto de acciones representativas de un mercado o sector (como el S&P 500 o el Merval) para medir su comportamiento general.\n\n✅ Permite ver cómo va el mercado en general\n✅ Sirve para comparar el rendimiento de tus inversiones\n✅ Se usa como referencia para fondos y ETFs\n✅ Facilita invertir en todo un mercado sin elegir acciones específicas\n\n*📊 Ideal para entender la salud del mercado y diversificar con un solo instrumento.*"},
    {"fecha": "23/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el riesgo financiero?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el riesgo financiero?\nEs la posibilidad de perder dinero o no obtener la ganancia esperada en una inversión.\n\n✅ Puede deberse a cambios en el mercado, economía o empresa\n✅ Cada inversión tiene un nivel distinto de riesgo\n✅ Entenderlo ayuda a tomar decisiones más inteligentes\n✅ Se maneja diversificando y eligiendo inversiones adecuadas\n\n*📊 Ideal para proteger tu dinero y evitar sorpresas desagradables.*"},
    {"fecha": "30/07/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la volatilidad?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la volatilidad?\nEs la medida de cuánto varía el precio de un activo en un período de tiempo.\n\n✅ Alta volatilidad significa cambios rápidos y grandes en el precio\n✅ Baja volatilidad indica precios más estables\n✅ Influye en el riesgo de la inversión\n✅ Entenderla ayuda a manejar mejor tus emociones y decisiones\n\n*📊 Ideal para saber qué esperar y elegir inversiones según tu perfil.*"},
    {"fecha": "03/09/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la liquidez?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la liquidez?\nEs la facilidad y rapidez con la que podés convertir una inversión en efectivo sin perder valor.\n\n✅ Alta liquidez significa que podés vender rápido y sin problemas\n✅ Baja liquidez puede implicar demora o pérdida al vender\n✅ Importante para tener dinero disponible cuando lo necesites\n✅ Afecta la elección de tus inversiones según tus objetivos\n\n*📊 Ideal para manejar bien tu dinero y evitar quedar atrapado en inversiones difíciles de vender.*"},
    {"fecha": "13/08/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un dividendo?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un dividendo?\nEs la parte de las ganancias que una empresa reparte a sus accionistas como recompensa por invertir.\n\n✅ Pueden ser pagos en efectivo o más acciones\n✅ Son una forma de obtener ingresos pasivos\n✅ No todas las empresas pagan dividendos\n✅ Se suelen repartir periódicamente (trimestral, anual)\n\n*📊 Ideal para quienes buscan ingresos adicionales sin vender sus acciones.*"},
    {"fecha": "13/08/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué son las acciones blue chips?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué son las acciones blue chips?\nSon acciones de empresas grandes, reconocidas y sólidas, con buena reputación y estabilidad financiera.\n\n✅ Suelen tener menor riesgo que otras acciones\n✅ Pagán dividendos regulares\n✅ Son líderes en su sector y mercado\n✅ Ideal para inversores que buscan estabilidad y crecimiento seguro\n\n*📊 Perfectas para armar una cartera sólida y confiable.*"},
    {"fecha": "20/08/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el apalancamiento?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el apalancamiento?\nEs usar dinero prestado para aumentar el monto que invertís, buscando multiplicar ganancias, pero también aumentando riesgos.\n\n✅ Permite invertir más de lo que tenés\n✅ Puede amplificar tanto ganancias como pérdidas\n✅ Requiere manejo cuidadoso para evitar grandes pérdidas\n✅ Se usa mucho en inversiones y trading\n\n*📊 Ideal para quienes entienden bien los riesgos y buscan potenciar sus inversiones.*"},
    {"fecha": "27/08/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué son los derivados financieros?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué son los derivados financieros?\nSon contratos cuyo valor depende del precio de otro activo, como acciones, bonos o materias primas.\n\n✅ Se usan para protegerse contra riesgos o para especular\n✅ Incluyen opciones, futuros y swaps\n✅ Pueden aumentar ganancias pero también pérdidas\n✅ Son instrumentos avanzados que requieren conocimiento\n\n*📊 Ideal para quienes quieren gestionar riesgos o diversificar estrategias.*"},
    {"fecha": "03/09/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es una IPO (Oferta Pública Inicial)?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es una IPO?\nEs la primera vez que una empresa ofrece sus acciones al público para financiar su crecimiento y convertirse en una compañía pública.\n\n✅ Permite a la empresa conseguir capital para expandirse\n✅ Los inversores pueden comprar acciones desde el inicio\n✅ Es una oportunidad para participar en empresas nuevas y en crecimiento\n✅ Implica riesgos porque la empresa es nueva en bolsa\n\n*📊 Ideal para quienes quieren invertir en etapas tempranas de empresas.*"},
    {"fecha": "10/09/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un activo financiero?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un activo financiero?\nEs un recurso que representa dinero o derecho a recibir dinero, como acciones, bonos o efectivo.\n\n✅ Generan ingresos o ganancias potenciales\n✅ Se pueden comprar, vender o intercambiar\n✅ Son la base para invertir y crecer tu patrimonio\n✅ Cada tipo tiene características y riesgos distintos\n\n*📊 Ideal para entender qué estás comprando cuando invertís.*"},
    {"fecha": "17/09/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la capitalización de mercado?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la capitalización de mercado?\nEs el valor total de todas las acciones de una empresa en el mercado, calculado multiplicando el precio de la acción por la cantidad de acciones emitidas.\n\n✅ Indica el tamaño y peso de una empresa\n✅ Se usa para clasificar empresas en grandes, medianas o pequeñas\n✅ Ayuda a evaluar riesgos y oportunidades\n✅ Es un dato clave para inversores y analistas\n\n*📊 Ideal para entender la escala de una empresa y comparar inversiones.*"},
    {"fecha": "24/09/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un split de acciones?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un split de acciones?\nEs cuando una empresa divide sus acciones existentes en más unidades, reduciendo el precio por acción pero sin cambiar el valor total de la inversión.\n\n✅ Hace que las acciones sean más accesibles para pequeños inversores\n✅ No cambia el valor total que tenés invertido\n✅ Puede aumentar la liquidez de la acción\n✅ Se usa para mejorar el atractivo de la acción en el mercado\n\n*📊 Ideal para facilitar la compra y venta de acciones.*"},
    {"fecha": "01/10/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el costo promedio ponderado (promedio de compra)?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el costo promedio ponderado?\nEs el precio promedio al que compraste un activo, considerando todas las compras que hiciste y la cantidad adquirida en cada una.\n\n✅ Te ayuda a saber cuánto pagaste realmente por acción o bono\n✅ Útil para calcular ganancias o pérdidas\n✅ Facilita decisiones para comprar o vender\n✅ Es una estrategia para reducir el impacto de la volatilidad\n\n*📊 Ideal para tener claridad y controlar mejor tus inversiones.*"},
    {"fecha": "08/10/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un stop loss?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un stop loss?\nEs una orden que ponés para vender una acción automáticamente cuando su precio baja a un nivel que definiste, para limitar pérdidas.\n\n✅ Ayuda a proteger tu dinero de caídas grandes\n✅ Es una herramienta clave para manejar riesgos\n✅ Se usa mucho en trading e inversiones\n✅ Permite operar sin estar todo el tiempo pendiente del mercado\n\n*📊 Ideal para cuidar tu capital y evitar decisiones emocionales.*"},
    {"fecha": "15/10/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el margen de seguridad en inversión?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el margen de seguridad?\nEs la diferencia entre el valor real de una inversión y su precio de compra, que te protege contra errores o imprevistos.\n\n✅ Te ayuda a minimizar riesgos\n✅ Permite comprar con descuento respecto al valor real\n✅ Es un principio clave para inversores prudentes\n✅ Aumenta las probabilidades de ganar a largo plazo\n\n*📊 Ideal para tomar decisiones más seguras y confiables.*"},
    {"fecha": "22/10/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la gestión pasiva vs gestión activa?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la gestión pasiva?\nInvertir replicando un índice o mercado, sin hacer cambios frecuentes.\n\n🔹 ¿Qué es la gestión activa?\nBuscar superar al mercado seleccionando activos y haciendo cambios frecuentes.\n\n✅ Gestión pasiva: costos bajos y menos esfuerzo\n✅ Gestión activa: busca mayores ganancias pero con más riesgos y costos\n✅ Cada una tiene ventajas según el perfil del inversor\n✅ Importante entender para elegir tu estrategia\n\n*📊 Ideal para definir cómo querés manejar tus inversiones.*"},
    {"fecha": "29/10/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la beta en finanzas?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la beta?\nEs una medida que indica cuánto se mueve el precio de una acción en relación al mercado.\n\n✅ Beta mayor a 1: acción más volátil que el mercado\n✅ Beta menor a 1: acción menos volátil que el mercado\n✅ Beta igual a 1: se mueve igual que el mercado\n✅ Ayuda a evaluar el riesgo relativo de una acción\n\n*📊 Ideal para entender cómo puede variar tu inversión.*"},
    {"fecha": "05/11/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el cash flow (flujo de caja)?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el cash flow?\nEs la cantidad de dinero que entra y sale de una empresa en un periodo determinado.\n\n✅ Muestra la salud financiera real de la empresa\n✅ Importante para saber si puede pagar deudas y crecer\n✅ No es lo mismo que ganancias contables\n✅ Clave para evaluar inversiones en empresas\n\n*📊 Ideal para entender cómo circula el dinero en las compañías donde invertís.*"},
    {"fecha": "12/11/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la deuda pública?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la deuda pública?\nEs el dinero que el Estado pide prestado para financiar gastos y proyectos, pagando con intereses a los que le prestan.\n\n✅ Se financia con bonos y otros instrumentos\n✅ Es clave para mantener servicios y desarrollo\n✅ Puede afectar la economía y la inflación\n✅ Los inversores pueden comprar bonos públicos\n\n*📊 Ideal para entender cómo funciona la economía y las inversiones en bonos del Estado.*"},
    {"fecha": "19/11/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la prima de riesgo?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es la prima de riesgo?\nEs la compensación extra que un inversor pide por asumir un riesgo mayor al invertir en un activo más riesgoso.\n\n✅ Se mide como diferencia entre el rendimiento esperado y el de un activo sin riesgo\n✅ Indica cuánto te pagan por correr riesgos adicionales\n✅ Ayuda a decidir si vale la pena invertir en activos más riesgosos\n✅ Importante para valorar bonos, acciones y proyectos\n\n*📊 Ideal para entender cuánto riesgo estás asumiendo y cómo te compensan por ello.*"},
    {"fecha": "26/11/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es un ETF inverso o apalancado?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es un ETF inverso?\nEs un fondo que busca ganar cuando el mercado baja, invirtiendo en la dirección contraria.\n\n🔹 ¿Qué es un ETF apalancado?\nEs un fondo que usa deuda para multiplicar las ganancias (y pérdidas) en relación al mercado.\n\n✅ Ambos son instrumentos avanzados\n✅ Tienen más riesgo y volatilidad\n✅ Requieren conocimientos y seguimiento constante\n✅ No son recomendados para principiantes\n\n*📊 Ideal para entender riesgos si querés explorar inversiones más complejas.*"},
    {"fecha": "03/12/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el spread en la bolsa?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el spread?\nEs la diferencia entre el precio de compra y el precio de venta de una acción o activo.\n\n✅ Indica el costo oculto de comprar y vender\n✅ Cuanto más pequeño, más fácil es negociar\n✅ Afecta la liquidez del mercado\n✅ Importante para entender costos y rentabilidad\n\n*📊 Ideal para optimizar tus operaciones y reducir gastos.*"},
    {"fecha": "10/12/2025 14:30", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es la cartera de crecimiento vs la cartera conservadora?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es una cartera de crecimiento?\nBusca maximizar ganancias con inversiones más arriesgadas y volátiles.\n\n🔹 ¿Qué es una cartera conservadora?\nPrioriza proteger el capital con inversiones más seguras y estables.\n\n✅ Cartera de crecimiento: más riesgo, mayor potencial de ganancia\n✅ Cartera conservadora: menos riesgo, menor volatilidad\n✅ Elegir depende de tu perfil y objetivos\n✅ Balancear ambas puede ser una buena estrategia\n\n*📊 Ideal para definir cómo querés manejar tus inversiones según tu tolerancia al riesgo.*"},
    {"fecha": "05/06/2025 02:15", "mensaje": "📚 *Miércoles de educación financiera*\n🧠 *Mini clase: ¿Qué es el ratio precio/utilidad (P/U)?*\n\nHola Impulsores! Como todos los miércoles, les dejamos una explicación breve y clave 👇\n\n🔹 ¿Qué es el ratio P/U?\nEs una medida que compara el precio de una acción con las ganancias que genera por acción.\n\n✅ Un P/U alto puede indicar expectativas de crecimiento\n✅ Un P/U bajo puede sugerir que la acción está barata o en problemas\n✅ Útil para comparar empresas dentro de un sector\n✅ Ayuda a tomar decisiones de compra o venta\n\n*📊 Ideal para evaluar si una acción está sobrevaluada o subvaluada.*"},
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
                mensaje_final = generar_mensaje_resumen()
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




# 📌 Ideas para nuevos contenidos semanales
# 1. "Dato Curioso de la Semana" (1 vez por semana)
# Algo breve sobre la historia de una empresa, índice o concepto financiero. Ej:

# “¿Sabías que McDonald's gana más con sus propiedades que con hamburguesas?”

# 2. "Mini Glosario Financiero" (1 concepto por semana)
# Un mini post explicando un término clave. Ej:

# “¿Qué es el Free Cash Flow y por qué importa en un balance?”

# 3. "Empresa para Mirar" (1 vez por semana o quincenal)
# Perfil breve de una empresa poco conocida con potencial. Sin recomendar compra, solo informar. Ej: una small cap interesante.

# 4. "Top 3 del mercado"
# Los 3 activos con más suba o baja en la semana. Puede ser acciones, bonos, ETFs, criptos. Visual y rápido.

# 5. “¿Qué miran los grandes?”
# Resumen rápido de movimientos de grandes fondos o inversores (tipo BlackRock, Buffett, ARK, etc.). Fuente: 13F filings, redes, newsletters.

# 6. "Preguntas de la comunidad"
# Una vez por semana respondé una pregunta que te hayan hecho por WhatsApp o Instagram (aunque la inventes al principio).

# 🧠 Opcional (si querés meter algo más didáctico)
# Mini tutoriales o “hilos” por WhatsApp:
# Cómo leer un balance / Cómo ver ratios clave / Cómo armar una watchlist en TradingView.

# Encuestas o trivias
# Para generar interacción y feedback. Podés hacerla desde Instagram y luego compartir resultados por WhatsApp.