"""
Modelo sencillo de recomendación.

Para cada lugar se calcula una puntuación:
  1. Tiene que coincidir con al menos uno de los intereses del huésped.
  2. + cuánto hablan de ese interés las reseñas reales de su distrito (% de reseñas, Inside Airbnb).
  3. + cercanía al piso (más cerca = más puntos).
  4. + un pequeño extra si es gratis.
Además se genera el texto "Por qué se lo recomendamos" con esas mismas razones.
"""
import pandas as pd

from utilidades import datos
from utilidades.textos import INTERESES, t


def recomendar(intereses, distrito, lat, lon, idioma, solo_gratis=False, max_km=None) -> pd.DataFrame:
    lug = datos.lugares().copy()
    lug = lug[lug.interes.isin(intereses)]
    if lug.empty:
        return lug
    lug["km"] = lug.apply(lambda r: round(datos.km(lat, lon, r.lat, r.lon), 1), axis=1)
    if solo_gratis:
        lug = lug[lug.gratis]
    if max_km is not None:
        lug = lug[lug.km <= max_km]

    men = datos.menciones()
    pct_distrito = men.loc[distrito] if distrito in men.index else None
    citas = datos.citas()

    # Ordenamos antes para que la opinión real salga en la tarjeta mejor puntuada de cada interés
    lug["_pre"] = lug.interes.map(lambda k: float(pct_distrito[k]) if pct_distrito is not None else 0) / 10 \
        + 3 / (1 + lug.km) + lug.gratis.astype(float) * 0.5
    lug = lug.sort_values("_pre", ascending=False).drop(columns="_pre")
    usadas = set()

    puntos, razones, citas_lugar = [], [], []
    for _, r in lug.iterrows():
        pct = float(pct_distrito[r.interes]) if pct_distrito is not None else 0.0
        score = pct / 10 + 3 / (1 + r.km) + (0.5 if r.gratis else 0)
        motivos = [t("razon_interes", idioma, interes=INTERESES[r.interes][idioma])]
        if pct > 0:
            motivos.append(t("razon_resenas", idioma, pct=str(pct).replace(".", ",") if idioma != "EN" else pct,
                             distrito=distrito))
        if r.km <= 2:
            motivos.append(t("razon_cerca", idioma, km=str(r.km).replace(".", ",") if idioma != "EN" else r.km))
        if r.gratis:
            motivos.append(t("razon_gratis", idioma))
        c = citas[(citas.distrito == distrito) & (citas.interes == r.interes)]
        if not c.empty and r.interes not in usadas:
            citas_lugar.append(c.cita.iloc[0])
            usadas.add(r.interes)
        else:
            citas_lugar.append(None)
        puntos.append(round(score, 2))
        razones.append(motivos)

    lug["puntuacion"] = puntos
    lug["razones"] = razones
    lug["cita"] = citas_lugar
    return lug.sort_values("puntuacion", ascending=False)
