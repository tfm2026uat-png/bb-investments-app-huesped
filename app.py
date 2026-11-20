"""
B&B Investments · Prototipo de app para huéspedes + dashboard del gestor (TFM INESDI).
Abrir con:  .venv/bin/streamlit run app.py
"""
import streamlit as st

from utilidades import datos
from utilidades.textos import IDIOMAS, t

st.set_page_config(page_title="B&B Investments · App huésped", page_icon="🏠", layout="wide")
datos.iniciar_estado()

if not datos.datos_listos():
    st.error("Faltan los datos preparados. En la Terminal, dentro de Test-App, ejecuten:\n\n"
             "`.venv/bin/python datos/preparar_datos.py`")
    st.stop()

with st.sidebar:
    st.markdown("### 🏠 B&B Investments")
    st.radio(t("idioma", st.session_state.p_idioma), list(IDIOMAS), key="p_idioma",
             format_func=lambda k: IDIOMAS[k], horizontal=True)

idioma = st.session_state.p_idioma
paginas = {
    "Huésped": [
        st.Page("pantallas/bienvenida.py", title=t("menu_bienvenida", idioma), icon="👋", default=True),
        st.Page("pantallas/que_ver.py", title=t("menu_que_ver", idioma), icon="🗺️"),
        st.Page("pantallas/servicios.py", title=t("menu_servicios", idioma), icon="🛎️"),
        st.Page("pantallas/estancia.py", title=t("menu_estancia", idioma), icon="📋"),
    ],
    "Gestor": [
        st.Page("pantallas/dashboard.py", title="Dashboard del gestor", icon="📊"),
    ],
}
nav = st.navigation(paginas)

with st.sidebar:
    st.divider()
    st.caption("Prototipo TFM · Máster BI & IA (INESDI). Datos reales: Inside Airbnb, Madrid, sep 2026. "
               "Lo marcado como **[ejemplo]** son valores ilustrativos, no reales.")

nav.run()
