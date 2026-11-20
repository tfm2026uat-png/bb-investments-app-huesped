"""Pantalla 3 · Servicios extra de pago."""
import streamlit as st

from utilidades import datos
from utilidades.textos import t

idioma = st.session_state.p_idioma
ej = t("ejemplo", idioma)

st.title(t("serv_titulo", idioma))
st.write(t("serv_intro", idioma))
st.caption(f"Precios {ej}")

serv = datos.servicios()
cols = st.columns(3)
for i, (_, s) in enumerate(serv.iterrows()):
    with cols[i % 3].container(border=True):
        st.markdown(f"### {s.icono}")
        st.markdown(f"**{t(s.clave, idioma)}**")
        st.caption(t(s.clave + "_d", idioma))
        st.markdown(f"**{s.precio_eur} €** {ej}")
        if st.button(t("reservar", idioma), key=f"btn_{s.clave}", type="primary", use_container_width=True):
            st.session_state.reservas.append({"clave": s.clave, "precio": int(s.precio_eur)})
            st.toast(t("reservado_ok", idioma, serv=t(s.clave, idioma)), icon="✅")

if st.session_state.reservas:
    st.subheader(t("mis_reservas", idioma))
    total = 0
    for r in st.session_state.reservas:
        st.markdown(f"- {t(r['clave'], idioma)} · {r['precio']} €")
        total += r["precio"]
    st.markdown(f"**{t('total', idioma)}: {total} €** {ej}")
    if st.button(t("cancelar_todo", idioma)):
        st.session_state.reservas = []
        st.rerun()
