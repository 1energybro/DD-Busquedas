import streamlit as st
import urllib.parse
from PIL import Image

st.set_page_config(page_title="Buscador de DD", layout="wide")

# Cargar logo
logo = Image.open("logo_mgi.png")
st.columns([6, 1])[0].image(logo, width=300)
st.columns([6, 1])[1].markdown("<p style='text-align: right;'>¿Dudas o sugerencias? <a href='mailto:hugo.cervantes@grupomexgas.com'>Contáctanos</a></p>", unsafe_allow_html=True)

# Introducción explicativa
st.title("🔎 Generador de Búsquedas de Debida Diligencia")
st.markdown("""
El presente programa fue elaborado por la **Gerencia de Planeación Estratégica** y la **Gerencia de Compliance** de **Mex Gas Internacional**.

Su propósito es facilitar la verificación digital de antecedentes públicos sobre personas físicas y morales mediante términos de búsqueda estructurados en **10 categorías temáticas**.

El presente ejercicio identifica **112 términos** seleccionados por su frecuencia de aparición en litigios, sanciones, investigaciones periodísticas y regulatorias.

La aplicación genera enlaces de búsqueda en **Google** y **Bing**, que permiten consultar fuentes públicas rápidamente con criterios homogéneos y auditables.
""")

email = st.text_input("Introduce tu correo de Mex Gas y continúa presionando Enter:")

if email.endswith("@grupomexgas.com"):
    st.success("Acceso concedido")

    nombre = st.text_input("Introduce el nombre de la empresa o persona a buscar y presiona enter:")

    if nombre:
        criterios_es = {...}  # Conservamos tu diccionario completo tal como lo tienes definido
        criterios_en = {...}  # Conservamos tu diccionario completo tal como lo tienes definido

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("### 🇲🇽 Enlaces en Español")
            for categoria, expresion in criterios_es.items():
                cadena_busqueda = f'"{nombre}" AND {expresion}'
                url_google = f"https://www.google.com/search?q={urllib.parse.quote(cadena_busqueda)}"
                url_bing = f"https://www.bing.com/search?q={urllib.parse.quote(cadena_busqueda)}"
                st.markdown(f"**{categoria}**")
                st.markdown(f"- [Buscar en Google]({url_google})")
                st.markdown(f"- [Buscar en Bing]({url_bing})")

        with col2:
            st.markdown("### 🇺🇸 Links in English")
            for categoria, expresion in criterios_en.items():
                cadena_busqueda = f'"{nombre}" AND {expresion}'
                url_google = f"https://www.google.com/search?q={urllib.parse.quote(cadena_busqueda)}"
                url_bing = f"https://www.bing.com/search?q={urllib.parse.quote(cadena_busqueda)}"
                st.markdown(f"**{categoria}**")
                st.markdown(f"- [Search on Google]({url_google})")
                st.markdown(f"- [Search on Bing]({url_bing})")

else:
    if email:
        st.error("Acceso denegado: usa un correo @grupomexgas.com")
