"""Pantalla 1 · Bienvenida."""
import streamlit as st

from utilidades import datos
from utilidades.textos import INTERESES, t

idioma = st.session_state.p_idioma
ej = t("ejemplo", idioma)

# Datos de la reserva: en la vida real llegarían del sistema de reservas. Aquí se pueden editar.
with st.expander(f"✏️ {t('datos_reserva', idioma)} {ej}"):
    c1, c2 = st.columns(2)
    c1.text_input(t("nombre", idioma), key="p_nombre")
    distrito_ant = st.session_state.p_distrito
    c2.selectbox(t("distrito", idioma), datos.CANDIDATOS, key="p_distrito")
    if st.session_state.p_distrito != distrito_ant or st.session_state.p_piso not in set(
            datos.pisos_familia(st.session_state.p_distrito).id):
        st.session_state.p_piso = int(datos.pisos_familia(st.session_state.p_distrito).iloc[0]["id"])
    opciones = datos.pisos_familia(st.session_state.p_distrito).head(30)
    nombres = dict(zip(opciones.id, opciones.name))
    st.selectbox(t("piso", idioma) + " (anuncio real de Inside Airbnb)", list(nombres), key="p_piso",
                 format_func=lambda i: nombres.get(i, str(i)))
    c3, c4 = st.columns(2)
    c3.date_input(t("llegada", idioma), key="p_llegada", format="DD/MM/YYYY")
    c4.date_input(t("salida", idioma), key="p_salida", format="DD/MM/YYYY")

piso = datos.piso_actual()
noches = max((st.session_state.p_salida - st.session_state.p_llegada).days, 0)
fmt = lambda d: d.strftime("%d/%m/%Y")

col_carta, col_tiempo = st.columns([3, 1])
with col_carta:
    st.title(t("hola", idioma, nombre=st.session_state.p_nombre))
    with st.container(border=True):
        st.markdown(t("carta", idioma, piso=piso["name"], distrito=piso["distrito"],
                      llegada=fmt(st.session_state.p_llegada), salida=fmt(st.session_state.p_salida),
                      noches=noches))
        st.markdown(f"*{t('firma', idioma)}*")
        st.caption(f"🏠 {piso['barrio']}, {piso['distrito']} · {int(piso['accommodates'])} plazas · "
                   f"⭐ {piso['review_scores_rating']:.2f} ({int(piso['number_of_reviews'])} reseñas) — dato real")
with col_tiempo:
    with st.container(border=True):
        st.markdown(f"**{t('tiempo_hoy', idioma)}** {ej}")
        st.metric("☀️", "14 °C")
        st.caption(t("tiempo_desc", idioma))

st.subheader(t("tus_intereses", idioma))
st.caption(t("intereses_ayuda", idioma))
st.pills(t("tus_intereses", idioma), list(INTERESES), key="p_intereses", selection_mode="multi",
         format_func=lambda k: INTERESES[k][idioma], label_visibility="collapsed")

if st.session_state.p_intereses:
    st.page_link("pantallas/que_ver.py", label=t("ir_recomendaciones", idioma), icon="🗺️")
