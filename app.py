import streamlit as st
import urllib.parse

st.set_page_config(page_title="Buscador de DD", layout="centered")
st.title("🔎 Generador de Búsquedas de Debida Diligencia")

email = st.text_input("Introduce tu correo corporativo para continuar:")

if email.endswith("@grupomexgas.com"):
    st.success("Acceso concedido")

    nombre = st.text_input("Nombre de la empresa o persona a buscar:")
    categoria = st.selectbox("Categoría de búsqueda:", [
        "Corrupción",
        "Delitos financieros",
        "Delitos penales",
        "Sanciones y regulación",
        "Derechos humanos y condiciones laborales",
        "Terrorismo y financiamiento ilícito",
        "Litigios y problemas legales",
        "Insolvencia y problemas financieros",
        "Justicia penal y cooperación",
        "Riesgo político y conexiones gubernamentales"
    ])

    if st.button("Generar links") and nombre:
        criterios = {
            "Corrupción": "(\"corrupción\" OR \"soborno\" OR \"cohecho\" OR \"DOF\" OR \"SEC\" OR \"escándalo\" OR \"mordida\" OR \"comisión ilegal\" OR \"pago indebido\")",
            "Delitos financieros": "(\"fraude\" OR \"lavado de dinero\" OR \"evasión de impuestos\" OR \"paraíso fiscal\" OR \"información privilegiada\" OR \"manipulación\" OR \"falsificación\" OR \"malversación\" OR \"desfalco\" OR \"estafa\" OR \"blanqueo de capitales\" OR \"facturero\")",
            "Delitos penales": "(\"actividades ilegales\" OR \"crimen organizado\" OR \"narcotráfico\" OR \"drogas\" OR \"delito\" OR \"cártel\" OR \"tráfico\" OR \"criminal\" OR \"procesado\" OR \"acusado\" OR \"condenado\" OR \"crimen de guerra\" OR \"huachicol\")",
            "Sanciones y regulación": "(\"sancionado\" OR \"sancionada\" OR \"penalización\" OR \"suspendido\" OR \"multa\" OR \"inhabilitación\" OR \"advertencia\" OR \"regulador\" OR \"irregular\" OR \"irregularidad\" OR \"incumplimiento\" OR \"violación regulatoria\")",
            "Derechos humanos y condiciones laborales": "(\"derechos humanos\" OR \"violación de derechos\" OR \"esclavitud\" OR \"trabajo forzado\" OR \"explotación\" OR \"condiciones inhumanas\" OR \"condiciones insalubres\" OR \"violación ambiental\" OR \"discriminación\" OR \"acoso\" OR \"abuso\")",
            "Terrorismo y financiamiento ilícito": "(\"terrorismo\" OR \"financiamiento del terrorismo\" OR \"extremismo\" OR \"grupo terrorista\" OR \"radicalización\" OR \"financiamiento ilícito\" OR \"sanción internacional\" OR \"lista negra\" OR \"lista de vigilancia\" OR \"OFAC\")",
            "Litigios y problemas legales": "(\"demanda judicial\" OR \"demandado\" OR \"litigio\" OR \"pleito legal\" OR \"impugnar\" OR \"apelar\" OR \"queja\" OR \"citación\" OR \"infracción de patentes\" OR \"infracción de propiedad intelectual\" OR \"disputa\" OR \"conflicto legal\")",
            "Insolvencia y problemas financieros": "(\"bancarrota\" OR \"insolvencia\" OR \"insolvente\" OR \"quiebra\" OR \"suspensión de pagos\" OR \"reestructuración\" OR \"dificultades financieras\" OR \"coacción financiera\" OR \"embargo\" OR \"liquidación\" OR \"concurso de acreedores\")",
            "Justicia penal y cooperación": "(\"investigación criminal\" OR \"policía federal\" OR \"fiscalía\" OR \"proceso penal\" OR \"negociación de la condena\" OR \"acuerdo de clemencia\" OR \"testigo protegido\" OR \"colaboración eficaz\" OR \"delación premiada\")",
            "Riesgo político y conexiones gubernamentales": "(\"político\" OR \"gobierno\" OR \"servicio público\" OR \"funcionario\" OR \"cargo público\" OR \"partido político\" OR \"congreso\" OR \"senado\" OR \"legislador\" OR \"donación política\" OR \"vínculo político\" OR \"conflicto de interés\")"
        }

        cadena_busqueda = f'"{nombre}" AND ' + criterios[categoria]
        url_google = f"https://www.google.com/search?q={urllib.parse.quote(cadena_busqueda)}"
        url_bing = f"https://www.bing.com/search?q={urllib.parse.quote(cadena_busqueda)}"

        st.markdown("### 🔗 Enlaces generados")
        st.markdown(f"[Buscar en Google]({url_google})")
        st.markdown(f"[Buscar en Bing]({url_bing})")

else:
    if email:
        st.error("Acceso denegado: usa un correo @grupomexgas.com")
