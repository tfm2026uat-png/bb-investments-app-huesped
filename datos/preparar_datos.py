"""
Prepara los datos del prototipo a partir de tus archivos de Inside Airbnb (sep 2026).

- SOLO LEE los archivos originales de "Madrid/Data Sep 2026". No los modifica.
- Guarda versiones pequeñas en "Test-App/datos/reales/" para que la app abra rápido.

Ejecutar una sola vez (desde la carpeta Test-App):
    .venv/bin/python datos/preparar_datos.py
"""
from pathlib import Path
import json
import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

AQUI = Path(__file__).resolve().parent
ORIGEN = AQUI.parent.parent / "Madrid" / "Data Sep 2026"
SALIDA = AQUI / "reales"
SALIDA.mkdir(exist_ok=True)

CANDIDATOS = ["Barajas", "Moncloa - Aravaca", "Tetuán", "Ciudad Lineal"]
RESENAS_POR_DISTRITO = 3000  # muestra para el modelo de temas

# Palabras que indican cada interés en las reseñas (español, inglés y portugués)
INTERESES = {
    "comer_barato": r"\b(?:barat\w*|econ[oó]mic\w*|cheap|affordable|supermerca\w*|supermarket\w*|mercado|market|restaurant\w*|tapas|comida|food|comer)\b",
    "museos": r"\b(?:muse\w*|prado|reina sof[ií]a|thyssen|arte|art)\b",
    "futbol": r"\b(?:bernab[eé]u|estadio|stadium|metropolitano|f[uú]tbol|football|soccer|real madrid|atl[eé]tico)\b",
    "parques": r"\b(?:parques?|parks?|casa de campo|dehesa|jard[ií]n(?:es)?|gardens?)\b",
    "compras": r"\b(?:tienda\w*|shop\w*|centro comercial|mall|compras|lojas?)\b",
    "vida_nocturna": r"\b(?:nightlife|vida nocturna|bares|bars|pubs?|copas|discoteca\w*|fiesta|party|ambiente|noite)\b",
    "metro_transporte": r"\b(?:metro|subway|underground|bus|autob[uú]s|transporte|transport\w*|aeropuerto|airport|aeroporto)\b",
    "tranquilo": r"\b(?:tranquil\w*|quiet|silencios\w*|calm\w*|sosseg\w*)\b",
}

STOP = set("""
a al algo algunas algunos ante antes como con contra cual cuando de del desde donde durante e el ella ellas ellos en entre era
es esa esas ese eso esos esta estaba estado estamos estar este esto estos estuvo fue fueron gran ha habia han hasta hay la las le les
lo los mas me mi mis mucho muy muchas muchos nada ni no nos nosotros o os otra otro para pero poco por porque que quien se ser si
sin sobre son su sus tambien te tiene todo todos tu un una uno unos y ya estancia piso apartamento casa anfitrion lugar todo
madrid sitio genial perfecto excelente bien recomiendo recomendable muy bueno buena limpio volveria gracias
the and to was is in of for it we very with a an this that our at as be had place stay great apartment flat host
would again everything really nice good well also there were has you all from but not are so recommend clean perfect
de do da os as um uma com para em no na que nao muito foi tudo bem otimo excelente lugar recomendo apartamento
""".split())


def cargar_pisos() -> pd.DataFrame:
    ruta = ORIGEN / "analisis_perfil_target" / "ingesta_listings" / "listings_analisis.csv.gz"
    cols = ["id", "name", "distrito", "barrio", "latitude", "longitude", "accommodates", "bedrooms",
            "precio_noche", "review_scores_rating", "number_of_reviews", "number_of_reviews_ltm",
            "minimum_nights", "availability_30", "availability_365", "host_name"]
    df = pd.read_csv(ruta, usecols=cols, low_memory=False)
    return df


def main():
    print("1/3 Leyendo anuncios limpios (listings_analisis.csv.gz)...")
    pisos = cargar_pisos()
    cand = pisos[pisos.distrito.isin(CANDIDATOS)].copy()
    cand.to_csv(SALIDA / "pisos_candidatos.csv", index=False)
    print(f"   {len(cand)} pisos enteros activos en los 4 distritos candidatos")

    # Resumen por distrito (todos los distritos, para comparar)
    resumen = pisos.groupby("distrito").agg(
        pisos=("id", "size"),
        precio_noche_mediana=("precio_noche", "median"),
        valoracion_media=("review_scores_rating", "mean"),
        plazas_mediana=("accommodates", "median"),
        resenas_12m=("number_of_reviews_ltm", "sum"),
        dias_libres_30_media=("availability_30", "mean"),
        pct_media_estancia=("minimum_nights", lambda s: (s >= 28).mean() * 100),
    ).round(2).reset_index()
    resumen.to_csv(SALIDA / "resumen_distritos.csv", index=False)

    print("2/3 Leyendo reseñas (reviews.csv.gz, puede tardar 1-3 minutos)...")
    mapa = pd.read_csv(ORIGEN / "listings.csv", usecols=["id", "neighbourhood_group"])
    mapa = dict(zip(mapa.id, mapa.neighbourhood_group))
    trozos = []
    for ch in pd.read_csv(ORIGEN / "reviews.csv.gz", usecols=["listing_id", "date", "comments"],
                          chunksize=200_000):
        ch = ch[ch.date >= "2024-09-01"].dropna(subset=["comments"])  # últimos 2 años
        ch["distrito"] = ch.listing_id.map(mapa)
        trozos.append(ch.dropna(subset=["distrito"]))
    rev = pd.concat(trozos)
    rev = rev.sample(frac=1, random_state=42).groupby("distrito").head(RESENAS_POR_DISTRITO)
    rev["texto"] = rev.comments.str.lower().str.replace(r"<br\s*/?>", " ", regex=True)
    print(f"   {len(rev)} reseñas en la muestra (máx. {RESENAS_POR_DISTRITO} por distrito, desde sep 2024)")

    print("3/3 Calculando temas por distrito...")
    # a) % de reseñas que mencionan cada interés
    filas = []
    for d, g in rev.groupby("distrito"):
        fila = {"distrito": d, "n_resenas": len(g)}
        for k, patron in INTERESES.items():
            fila[k] = round(g.texto.str.contains(patron, regex=True).mean() * 100, 1)
        filas.append(fila)
    menciones = pd.DataFrame(filas)
    menciones.to_csv(SALIDA / "menciones_intereses.csv", index=False)

    # b) TF-IDF: un "documento" por distrito -> palabras más características de cada uno
    docs = rev.groupby("distrito").texto.apply(" ".join)
    # Quitamos los nombres de los anfitriones (las reseñas los mencionan mucho y no son "temas")
    nombres = pd.read_csv(ORIGEN / "listings.csv", usecols=["host_name"]).host_name.dropna()
    nombres = {w for n in nombres.str.lower() for w in re.findall(r"[^\W\d_]+", n) if len(w) >= 3}
    vec = TfidfVectorizer(stop_words=list(STOP | nombres), token_pattern=r"(?u)\b[^\W\d_]{4,}\b",
                          min_df=2, max_df=0.8, ngram_range=(1, 2), max_features=30000)
    X = vec.fit_transform(docs.values)
    terminos = vec.get_feature_names_out()
    temas = {}
    for i, d in enumerate(docs.index):
        fila = X[i].toarray().ravel()
        top = fila.argsort()[::-1][:15]
        temas[d] = [terminos[j] for j in top if fila[j] > 0]
    (SALIDA / "temas_tfidf.json").write_text(json.dumps(temas, ensure_ascii=False, indent=1), encoding="utf-8")

    # c) Frases reales cortas que mencionan cada interés (para el "Por qué")
    citas = []
    for d in CANDIDATOS:
        g = rev[rev.distrito == d]
        for k, patron in INTERESES.items():
            ok = g[g.texto.str.contains(patron, regex=True) & (g.comments.str.len().between(40, 220))]
            for c in ok.comments.head(2):
                citas.append({"distrito": d, "interes": k, "cita": re.sub(r"<br\s*/?>", " ", c).strip()})
    pd.DataFrame(citas).to_csv(SALIDA / "citas_resenas.csv", index=False)

    for d in CANDIDATOS:
        print(f"   {d}: {', '.join(temas.get(d, [])[:8])}")
    print("Listo. Archivos en datos/reales/")


if __name__ == "__main__":
    main()
