"""Pantalla 5 · Dashboard del gestor de pisos (en español)."""
import pandas as pd
import plotly.express as px
import streamlit as st

from utilidades import datos
from utilidades.textos import INTERESES

st.title("📊 Dashboard del gestor")
st.caption("Distritos candidatos: Barajas, Moncloa - Aravaca, Tetuán y Ciudad Lineal · "
           "Datos reales: Inside Airbnb, Madrid, septiembre 2026 (pisos enteros activos, precio 20-2.000 €).")

pisos = datos.pisos()
serv = datos.servicios()
filtro = st.multiselect("Distritos", datos.CANDIDATOS, default=datos.CANDIDATOS)
p = pisos[pisos.distrito.isin(filtro)]
if p.empty:
    st.warning("Elijan al menos un distrito.")
    st.stop()

# ---------- KPIs ----------
no_disp = 100 - p.availability_30.mean() / 30 * 100
ingresos_ejemplo = int((serv.precio_eur * serv.reservas_mes_ejemplo).sum())
ingresos_sesion = sum(r["precio"] for r in st.session_state.reservas)

k1, k2, k3, k4 = st.columns(4)
with k1.container(border=True):
    st.metric("Ocupación (30 días)", f"{no_disp:.1f} %".replace(".", ","))
    st.caption("Real · % de noches no disponibles en el calendario de los próximos 30 días (incluye bloqueos).")
with k2.container(border=True):
    st.metric("Valoración media", f"{p.review_scores_rating.mean():.2f} / 5".replace(".", ","))
    st.caption(f"Real · media de {p.review_scores_rating.notna().sum():,} pisos con valoración.".replace(",", "."))
with k3.container(border=True):
    st.metric("Ingresos extras / mes", f"{ingresos_ejemplo + ingresos_sesion:,} €".replace(",", "."),
              delta=f"+{ingresos_sesion} € reservados en esta demo" if ingresos_sesion else None)
    st.markdown(":orange-badge[ejemplo] precios y volumen simulados")
with k4.container(border=True):
    st.metric("Uso de la app", "62 %")
    st.markdown(":orange-badge[ejemplo] % de huéspedes que la usan; la app aún no está en uso")

# ---------- Tabla por distrito ----------
st.subheader("Pisos en los distritos candidatos")
res = datos.resumen_distritos()
res = res[res.distrito.isin(filtro)].copy()
res["ocupacion_aprox_30d_pct"] = (100 - res.dias_libres_30_media / 30 * 100).round(1)
tabla = res[["distrito", "pisos", "precio_noche_mediana", "valoracion_media", "plazas_mediana",
             "resenas_12m", "ocupacion_aprox_30d_pct", "pct_media_estancia"]].rename(columns={
    "distrito": "Distrito", "pisos": "Pisos enteros activos", "precio_noche_mediana": "Precio/noche (mediana, €)",
    "valoracion_media": "Valoración media", "plazas_mediana": "Plazas (mediana)", "resenas_12m": "Reseñas 12 meses",
    "ocupacion_aprox_30d_pct": "Ocupación aprox. 30 días (%)", "pct_media_estancia": "% media estancia (≥28 noches)"})
st.dataframe(tabla, hide_index=True, use_container_width=True)
st.caption("Todo real (Inside Airbnb sep 2026). En el análisis del TFM la ocupación medida es ≈ 50 %; "
           "la de 30 días es más alta porque incluye noches bloqueadas.")

c1, c2 = st.columns(2)
with c1:
    st.markdown("**Mapa de pisos (real)**")
    st.map(p.rename(columns={"latitude": "lat", "longitude": "lon"})[["lat", "lon"]], size=20)
with c2:
    st.markdown("**De qué hablan las reseñas por distrito (% de reseñas, real)**")
    men = datos.menciones().loc[[d for d in filtro if d in datos.menciones().index]]
    cols = list(INTERESES) + ["metro_transporte", "tranquilo"]
    nombres = {k: v["ES"] for k, v in INTERESES.items()} | {"metro_transporte": "🚇 Metro / transporte",
                                                           "tranquilo": "🤫 Tranquilo"}
    heat = men[cols].rename(columns=nombres)
    fig = px.imshow(heat, text_auto=".1f", color_continuous_scale="Blues", aspect="auto")
    fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=330, coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

# ---------- Segmento óptimo ----------
st.subheader("Origen del segmento óptimo")
origen = pd.DataFrame({"País": ["México", "Colombia", "Brasil", "Argentina"],
                       "Porcentaje": [23.9, 16.4, 15.4, 15.0]})
c3, c4 = st.columns([2, 1])
with c3:
    fig2 = px.bar(origen, x="Porcentaje", y="País", orientation="h", text="Porcentaje",
                  color_discrete_sequence=["#2E86AB"])
    fig2.update_traces(texttemplate="%{text:.1f} %")
    fig2.update_layout(yaxis=dict(autorange="reversed"), margin=dict(l=0, r=0, t=10, b=0), height=260,
                       xaxis_title="% del segmento")
    st.plotly_chart(fig2, use_container_width=True)
with c4:
    st.markdown("Fuente: **INE 2025** (cifras aportadas por la autora del TFM).")
    st.markdown("👉 Por eso la app ofrece **español** y **portugués** además de inglés.")

# ---------- Servicios ----------
st.subheader("Servicios extra más pedidos")
st.markdown(":orange-badge[ejemplo] reservas simuladas + las que hagan en esta demo")
s = serv.copy()
nombres_serv = {"traslado": "Traslado aeropuerto", "llegada_temprana": "Llegada temprana",
                "limpieza_extra": "Limpieza extra", "sabanas": "Cambio de sábanas", "equipaje": "Guarda equipaje"}
demo = pd.Series([r["clave"] for r in st.session_state.reservas]).value_counts()
s["reservas"] = s.reservas_mes_ejemplo + s.clave.map(demo).fillna(0).astype(int)
s["ingresos_eur"] = s.reservas * s.precio_eur
s["Servicio"] = s.clave.map(nombres_serv)
st.dataframe(s[["Servicio", "precio_eur", "reservas", "ingresos_eur"]].rename(columns={
    "precio_eur": "Precio (€)", "reservas": "Reservas (mes)", "ingresos_eur": "Ingresos (€)"}),
    hide_index=True, use_container_width=True)
