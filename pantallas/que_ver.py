"""Pantalla 2 · Qué ver y hacer (recomendaciones personalizadas)."""
import pandas as pd
import streamlit as st

from modelo.recomendador import recomendar
from utilidades import datos
from utilidades.textos import t

idioma = st.session_state.p_idioma
piso = datos.piso_actual()
distrito = piso["distrito"]
intereses = st.session_state.p_intereses

st.title(t("que_ver_titulo", idioma))
st.caption(f"📍 {piso['name']} · {piso['barrio']}, {distrito}")

# Temas del distrito (modelo TF-IDF sobre reseñas reales)
with st.container(border=True):
    st.markdown(f"**{t('temas_distrito', idioma, distrito=distrito)}**")
    palabras = datos.temas().get(distrito, [])[:10]
    st.markdown(" ".join(f":blue-badge[{p}]" for p in palabras))
    st.caption(t("temas_ayuda", idioma))

if not intereses:
    st.info(t("sin_intereses", idioma))
    st.page_link("pantallas/bienvenida.py", label=t("menu_bienvenida", idioma), icon="👋")
    st.stop()

MAX_KM = 3
c1, c2 = st.columns(2)
gratis = c1.toggle(t("solo_gratis", idioma))
cerca = c2.toggle(t("solo_cerca", idioma, km=MAX_KM))

recs = recomendar(intereses, distrito, piso["latitude"], piso["longitude"], idioma,
                  solo_gratis=gratis, max_km=MAX_KM if cerca else None)
if recs.empty:
    st.warning(t("ninguna", idioma))
    st.stop()

col_lista, col_mapa = st.columns([3, 2])
with col_lista:
    desc_col = {"ES": "desc_es", "PT": "desc_pt", "EN": "desc_en"}[idioma]
    for _, r in recs.iterrows():
        with st.container(border=True):
            precio = t("gratis", idioma) if r.gratis and "Gratis" in r.precio_info else r.precio_info
            st.markdown(f"#### {r.nombre}")
            dist = r.km if idioma == "EN" else str(r.km).replace(".", ",")
            st.caption(f"📍 {r.distrito} · {t('a_km', idioma, km=dist)} · 💶 {precio}")
            st.write(r[desc_col])
            with st.expander(t("por_que", idioma), expanded=True):
                for m in r.razones:
                    st.markdown(f"- {m}")
                if isinstance(r.cita, str):
                    st.markdown(f"> *“{r.cita}”*  \n> — {t('opinion_real', idioma)} ({distrito}, Inside Airbnb)")

with col_mapa:
    puntos = pd.concat([
        pd.DataFrame({"lat": [piso["latitude"]], "lon": [piso["longitude"]], "color": ["#E4572E"], "size": [120]}),
        pd.DataFrame({"lat": recs.lat, "lon": recs.lon, "color": "#2E86AB", "size": 60}),
    ])
    st.map(puntos, latitude="lat", longitude="lon", color="color", size="size")
    st.caption("🔴 Su piso · 🔵 Recomendaciones")

st.caption("Los lugares son reales; los precios marcados [ejemplo] son orientativos. "
           "Los porcentajes y las opiniones vienen de reseñas reales de Inside Airbnb (sep 2024 – sep 2026).")
