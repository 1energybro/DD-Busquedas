import streamlit as st
import urllib.parse

# --- Configuración de acceso ---
st.set_page_config(page_title="Buscador de DD", layout="centered")
st.title("🔎 Generador de Búsquedas de Debida Diligencia")

# --- Validación de correo ---
email = st.text_input("Introduce tu correo corporativo para continuar:")

if email.endswith("@grupomexgas.com"):
    st.success("Acceso concedido")

    # --- Formulario para ingresar nombre y categoría ---
    nombre = st.text_input("Nombre de la empresa o persona a buscar:")
    categoria = st.selectbox("Categoría de búsqueda:", [
        "Corrupción", "Lavado de dinero", "Fraude", "Sanciones", "Litigios", "Vínculos políticos", "Medio ambiente", "Laboral"
    ])

    if st.button("Generar links") and nombre:
        # --- Generación de términos booleanos ---
        categorias_booleanas = {
            "Corrupción": ["soborno", "corrupción", "cohecho"],
            "Lavado de dinero": ["lavado de dinero", "blanqueo de capitales"],
            "Fraude": ["fraude", "engaño", "estafa"],
            "Sanciones": ["sanción", "sanciones", "multado"],
            "Litigios": ["demanda", "litigio", "juicio"],
            "Vínculos políticos": ["vínculo político", "partido", "funcionario"],
            "Medio ambiente": ["daño ambiental", "contaminación", "sanción ambiental"],
            "Laboral": ["huelga", "violación laboral", "condiciones de trabajo"]
        }

        terminos = categorias_booleanas.get(categoria, [])
        cadena_busqueda = f'"{nombre}" AND (' + ' OR '.join([f'"{t}"' for t in terminos]) + ')'
        url_google = f"https://www.google.com/search?q={urllib.parse.quote(cadena_busqueda)}"
        url_bing = f"https://www.bing.com/search?q={urllib.parse.quote(cadena_busqueda)}"

        st.markdown("### 🔗 Enlaces generados")
        st.markdown(f"[Buscar en Google]({url_google})")
        st.markdown(f"[Buscar en Bing]({url_bing})")

else:
    if email:
        st.error("Acceso denegado: usa un correo @grupomexgas.com")
