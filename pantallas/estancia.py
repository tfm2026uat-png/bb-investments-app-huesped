"""Pantalla 4 · Mi estancia (corta o media estancia)."""
import streamlit as st

from utilidades import datos
from utilidades.textos import CONDICIONES, t

idioma = st.session_state.p_idioma
piso = datos.piso_actual()

st.title(t("estancia_titulo", idioma))
st.segmented_control(t("tipo_estancia", idioma), ["corta", "media"], key="p_tipo_estancia",
                     format_func=lambda k: t(k, idioma))
tipo = st.session_state.p_tipo_estancia or "corta"

st.subheader(t("condiciones", idioma))
reglas = CONDICIONES["corta"] + (CONDICIONES["media_extra"] if tipo == "media" else [])
with st.container(border=True):
    for r in reglas:
        st.markdown(r[idioma])

if tipo == "media":
    res = datos.resumen_distritos().set_index("distrito")
    pct = res.loc[piso["distrito"], "pct_media_estancia"]
    p = f"{pct:.1f}" if idioma == "EN" else f"{pct:.1f}".replace(".", ",")
    d = piso["distrito"]
    st.info({
        "ES": f"📊 En {d}, el {p} % de los pisos enteros activos de Airbnb piden 28 noches o más "
              "(dato real, Inside Airbnb sep 2026).",
        "PT": f"📊 Em {d}, {p} % dos apartamentos inteiros ativos no Airbnb exigem 28 noites ou mais "
              "(dado real, Inside Airbnb set 2026).",
        "EN": f"📊 In {d}, {p}% of active entire homes on Airbnb require 28 nights or more "
              "(real data, Inside Airbnb Sep 2026).",
    }[idioma])
