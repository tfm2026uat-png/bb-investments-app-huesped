"""Carga de datos y estado compartido entre pantallas."""
from datetime import date
from math import asin, cos, radians, sin, sqrt
from pathlib import Path
import json

import pandas as pd
import streamlit as st

RAIZ = Path(__file__).resolve().parent.parent
REALES = RAIZ / "datos" / "reales"
EJEMPLO = RAIZ / "datos" / "ejemplo"

CANDIDATOS = ["Barajas", "Moncloa - Aravaca", "Tetuán", "Ciudad Lineal"]


def datos_listos() -> bool:
    return (REALES / "pisos_candidatos.csv").exists()


@st.cache_data
def pisos() -> pd.DataFrame:
    return pd.read_csv(REALES / "pisos_candidatos.csv")


@st.cache_data
def resumen_distritos() -> pd.DataFrame:
    return pd.read_csv(REALES / "resumen_distritos.csv")


@st.cache_data
def menciones() -> pd.DataFrame:
    return pd.read_csv(REALES / "menciones_intereses.csv").set_index("distrito")


@st.cache_data
def temas() -> dict:
    return json.loads((REALES / "temas_tfidf.json").read_text(encoding="utf-8"))


@st.cache_data
def citas() -> pd.DataFrame:
    return pd.read_csv(REALES / "citas_resenas.csv")


@st.cache_data
def lugares() -> pd.DataFrame:
    return pd.read_csv(EJEMPLO / "lugares.csv")


@st.cache_data
def servicios() -> pd.DataFrame:
    return pd.read_csv(EJEMPLO / "servicios.csv")


def km(lat1, lon1, lat2, lon2) -> float:
    """Distancia en línea recta (fórmula de Haversine)."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    a = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    return 6371 * 2 * asin(sqrt(a))


def pisos_familia(distrito: str) -> pd.DataFrame:
    """Pisos reales del distrito para el perfil familia (4-6 plazas), mejor valorados primero."""
    p = pisos()
    p = p[(p.distrito == distrito) & p.accommodates.between(4, 6)]
    if p.empty:
        p = pisos()[pisos().distrito == distrito]
    return p.sort_values(["review_scores_rating", "number_of_reviews"], ascending=False)


def iniciar_estado():
    """Valores iniciales de la reserva de ejemplo. Las claves 'p_' se conservan al cambiar de pantalla."""
    # Truco de Streamlit: reasignar las claves para que no se borren al cambiar de página
    for k in list(st.session_state.keys()):
        if k.startswith("p_"):
            st.session_state[k] = st.session_state[k]
    defaults = {
        "p_idioma": "ES",
        "p_nombre": "Familia Hernández",
        "p_distrito": "Tetuán",
        "p_llegada": date(2026, 12, 10),
        "p_salida": date(2026, 12, 15),
        "p_intereses": [],
        "p_tipo_estancia": "corta",
        "reservas": [],
    }
    for k, v in defaults.items():
        st.session_state.setdefault(k, v)
    if "p_piso" not in st.session_state and datos_listos():
        st.session_state["p_piso"] = int(pisos_familia(st.session_state["p_distrito"]).iloc[0]["id"])


def piso_actual() -> pd.Series:
    p = pisos()
    fila = p[p.id == st.session_state.get("p_piso")]
    if fila.empty:
        fila = pisos_familia(st.session_state["p_distrito"]).head(1)
    return fila.iloc[0]


def marca_ejemplo(texto: str = "") -> str:
    return f"{texto} :orange-badge[ejemplo]"
