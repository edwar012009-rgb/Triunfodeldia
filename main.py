import os
import requests
from datetime import datetime
import pytz

# ==========================================
# CONFIGURACIÓN DE CREDENCIALES Y ENTORNO
# ==========================================
TELEGRAM_TOKEN = os.getenv("8761282998:AAFGXLn8-fVQE11rY9Icc9CkxQiI6vd4rp4", "8761282998:AAFGXLn8-fVQE11rY9Icc9CkxQiI6vd4rp4")
CHAT_ID = os.getenv("6622432626", "6622432626")

tz_ve = pytz.timezone("America/Caracas")
fecha_hoy_ve = datetime.now(tz_ve).strftime("%Y-%m-%d")

def enviar_alerta_telegram(mensaje):
    """Envía la notificación         f"📌 *Mercado:* {opcion_nombre} (@{cuota_tb})\n\n"
        f"1️⃣ *RECOPILACIÓN Y ANÁLISIS DE GOLES Y ATAQUE:*\n"
        f"▫️ Promedios: {stats['prom_goles']}\n"
        f"▫️ xG y Tiros a Puerta (SOT): {stats['xg_sot']}\n"
        f"▫️ Tendencias: {stats['btts_over']}\n\n"
        f"2️⃣ *RECOPILACIÓN Y ANÁLISIS DISCIPLINARIO (Tarjetas):*\n"
        f"▫️ Tarjetas Equipos: {stats['tarjetas']}\n"
        f"▫️ Árbitro Principal: {stats['arbitro']}\n\n"
        f"3️⃣ *RECOPILACIÓN Y ANÁLISIS DE CÓRNERS:*\n"
        f"▫️ {stats['corners']}\n\n"
        f"4️⃣ *DINÁMICA ACTUAL, RELEVANCIA Y BAJAS:*\n"
        f"▫️️ Forma y Ausencias: {stats['forma_bajas']}\n"
        f"▫️ Motivación: {stats['motivacion']}\n\n"
        f"📊 *Probabilidad Implícita de la cuota:* {prob_implicita}%\n"
        f"⚠️ *Nota:* Análisis con datos estadísticos reales verificados."
    )

# ==========================================
# EJECUCIÓN PRINCIPAL SIN FILTROS
# ==========================================
def ejecutar_bot():
    print("🚀 Procesando TODOS los partidos del día en Béisbol y Fútbol...")
    partidos = obtener_partidos_triunfobet()
    
    if not partidos:
        print("⚠️ No se encontraron eventos en la parrilla.")
        enviar_alerta_telegram(f"ℹ️ *Reporte:* No hay partidos programados en Triunfobet para la fecha ({fecha_hoy_ve}).")
        return

    total_analizados = 0
    for partido in partidos:
        local = partido.get("home_team", partido.get("local", "Local"))
        visitante = 
