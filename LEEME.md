# B&B Investments · Prototipo de app para huéspedes + dashboard del gestor

Prototipo funcional del TFM (Máster BI & IA, INESDI), hecho con **Streamlit** (Python).
No es una app de producción: sirve para enseñar la idea en la entrega del 10 de diciembre.

## Cómo abrir la app en el Mac

1. Abran la app **Terminal** (búsquenla con ⌘ + espacio y escriban "Terminal").
2. Copien y peguen este comando y pulsen Enter. Entra en la carpeta del prototipo:

   ```bash
   cd ~/Library/CloudStorage/OneDrive-Personal/TFM-INESDI/Test-App
   ```

3. Copien y peguen este otro comando. Abre la app:

   ```bash
   .venv/bin/streamlit run app.py
   ```

4. Se abrirá el navegador en `http://localhost:8501`. Si no se abre solo, copien esa dirección en Chrome o Safari.
5. Para **cerrar** la app, vuelvan a la Terminal y pulsen `Control + C`.

## Solo la primera vez (ya está hecho)

Estos pasos ya se hicieron al crear el prototipo. Repítanlos solo si borran la carpeta `.venv` o `datos/reales`:

```bash
python3 -m venv .venv
```

```bash
.venv/bin/pip install -r requirements.txt
```

```bash
.venv/bin/python datos/preparar_datos.py
```

- El 1.º crea el **entorno virtual**: una carpeta aislada con los programas que usa la app.
- El 2.º instala esos programas: streamlit, pandas, scikit-learn y plotly.
- El 3.º **lee** los datos de Inside Airbnb de `Madrid/Data Sep 2026` (sin modificarlos) y guarda versiones pequeñas en `datos/reales/`. Tarda unos minutos.

## Qué hay en cada pantalla

| Pantalla | Qué hace | Datos |
|---|---|---|
| 👋 Bienvenida | Carta personalizada, el tiempo, idioma ES/PT/EN e intereses | Piso **real** (Inside Airbnb); huésped, fechas y tiempo **[ejemplo]** |
| 🗺️ Qué ver y hacer | Recomendaciones según intereses y distrito, con "Por qué se lo recomendamos". Filtros: gratis y cerca del piso | % de reseñas por tema, palabras TF-IDF y opiniones **reales**; lugares reales con precios **[ejemplo]** |
| 🛎️ Servicios | Extras de pago con botón Reservar | Precios **[ejemplo]** |
| 📋 Mi estancia | Corta o media estancia: cambian las condiciones | % de media estancia por distrito **real**; wifi, fianza y suministros **[ejemplo]** |
| 📊 Dashboard del gestor | KPIs, tabla y mapa de pisos, temas de reseñas, origen del segmento y servicios | Ocupación y valoración **reales**; ingresos por extras y % de uso de la app **[ejemplo]**; origen del segmento: INE 2025 (cifras aportadas por la autora) |

## Cómo funciona el "modelo" de recomendación

1. Se toma una muestra de hasta 3.000 reseñas reales por distrito (sep 2024 – sep 2026).
2. **Palabras clave**: se cuenta qué % de reseñas habla de cada interés (comida, museos, fútbol, parques, compras, vida nocturna, metro, tranquilidad) en español, inglés y portugués.
3. **TF-IDF**: se buscan las palabras más características de las reseñas de cada distrito frente a los otros 20.
4. Cada lugar recibe una puntuación según tres cosas: si coincide con un interés del huésped, cuánto hablan de ese tema las reseñas del distrito y lo cerca que está del piso. Si es gratis, suma un poco más.
5. Esas mismas razones se muestran en el recuadro "Por qué se lo recomendamos".

## Carpetas

```
Test-App/
├── app.py                 ← menú principal (abre esto)
├── pantallas/             ← las 5 pantallas
├── modelo/recomendador.py ← modelo de recomendación
├── utilidades/            ← textos ES/PT/EN y carga de datos
├── datos/
│   ├── preparar_datos.py  ← prepara los datos reales
│   ├── reales/            ← datos reales ya resumidos
│   └── ejemplo/           ← lugares y servicios [ejemplo]
├── requirements.txt
└── .venv/                 ← entorno virtual (no tocar)
```

## Avisos

- Lo marcado como **[ejemplo]** son valores ilustrativos, no datos reales.
- La "ocupación aprox. 30 días" son las noches **no disponibles** en el calendario. Incluye las que bloquea el anfitrión, así que sale más alta que la ocupación real (≈ 50 % en el TFM).
- Las reservas de servicios solo duran mientras la app está abierta. Es una demo.
