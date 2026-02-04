import streamlit as st
import yt_dlp
import os

# Configuración de la página
st.set_page_config(page_title="Descargador Pro", page_icon="🚀")
st.title("🚀 Descargador Universal de Video")
st.markdown("Copia el link de **YouTube, TikTok, Instagram o Twitter** y descárgalo en segundos.")

url = st.text_input("Pega el enlace aquí:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Preparar mi video"):
    if url:
        with st.spinner("Buscando video... esto puede tardar un poco."):
            # Configuración maestra para evitar bloqueos
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'video_provisional.%(ext)s',
                # Estos encabezados engañan a las webs haciéndoles creer que eres un humano en Chrome
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                },
                'extractor_args': {
                    'youtube': {'player_client': ['android', 'web']},
                    'generic': {'impersonate': 'chrome'}
                },
                'nocheckcertificate': True,
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Extraemos la información del video
                    info = ydl.extract_info(url, download=True)
                    # Obtenemos el nombre exacto del archivo que se creó
                    temp_filename = ydl.prepare_filename(info)

                # Abrimos el archivo para que el usuario lo descargue
                with
