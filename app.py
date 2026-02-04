import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Universal", page_icon="📥")
st.title("📥 Descargador de Video Universal")
st.write("Pega el link de YouTube, TikTok, Instagram o Twitter.")

url = st.text_input("Enlace del video:")

if st.button("Preparar descarga"):
    if url:
        with st.spinner("Procesando... esto puede tardar un poco dependiendo del tamaño."):
            # Configuración para que funcione en la web (Streamlit)
         ydl_opts = {
                'format': 'best',
                'outtmpl': 'video_provisional.%(ext)s',
                'extractor_args': {'generic': {'impersonate': 'chrome'}},
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    # El nombre real que puso yt-dlp
                    filename = ydl.prepare_filename(info)
                
                with open(filename, "rb") as file:
                    st.download_button(
                        label="✅ ¡Todo listo! Descargar archivo",
                        data=file,
                        file_name=f"{info['title']}.mp4",
                        mime="video/mp4"
                    )
                os.remove(filename) # Borramos del servidor para no ocupar espacio
            except Exception as e:
                st.error(f"Hubo un problema: {e}")
    else:
        st.warning("Escribe un enlace primero.")
