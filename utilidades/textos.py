"""Textos de la app en español latino (ES), portugués (PT) e inglés (EN)."""

IDIOMAS = {"ES": "Español", "PT": "Português", "EN": "English"}

INTERESES = {
    "comer_barato": {"ES": "🍽️ Comer barato", "PT": "🍽️ Comer barato", "EN": "🍽️ Cheap eats"},
    "museos": {"ES": "🏛️ Museos", "PT": "🏛️ Museus", "EN": "🏛️ Museums"},
    "futbol": {"ES": "⚽ Fútbol", "PT": "⚽ Futebol", "EN": "⚽ Football"},
    "parques": {"ES": "🌳 Parques", "PT": "🌳 Parques", "EN": "🌳 Parks"},
    "compras": {"ES": "🛍️ Compras", "PT": "🛍️ Compras", "EN": "🛍️ Shopping"},
    "vida_nocturna": {"ES": "🌙 Vida nocturna", "PT": "🌙 Vida noturna", "EN": "🌙 Nightlife"},
}

T = {
    # Menú
    "menu_bienvenida": {"ES": "Bienvenida", "PT": "Boas-vindas", "EN": "Welcome"},
    "menu_que_ver": {"ES": "Qué ver y hacer", "PT": "O que ver e fazer", "EN": "Things to do"},
    "menu_servicios": {"ES": "Servicios", "PT": "Serviços", "EN": "Services"},
    "menu_estancia": {"ES": "Mi estancia", "PT": "Minha estadia", "EN": "My stay"},
    "idioma": {"ES": "Idioma", "PT": "Idioma", "EN": "Language"},
    "ejemplo": {"ES": "[ejemplo]", "PT": "[exemplo]", "EN": "[sample]"},

    # Bienvenida
    "hola": {"ES": "¡Hola, {nombre}! Bienvenidos a Madrid",
             "PT": "Olá, {nombre}! Bem-vindos a Madri",
             "EN": "Hi {nombre}! Welcome to Madrid"},
    "carta": {
        "ES": "Nos alegra mucho recibirlos en **{piso}**, en el distrito de **{distrito}**. "
              "Su llegada está prevista para el **{llegada}** y la salida para el **{salida}** "
              "({noches} noches). Esta app les ayudará a aprovechar su estancia: recomendaciones "
              "pensadas para ustedes, servicios extra y toda la información del piso.",
        "PT": "Ficamos muito felizes em recebê-los em **{piso}**, no distrito de **{distrito}**. "
              "A chegada está prevista para **{llegada}** e a saída para **{salida}** "
              "({noches} noites). Este app vai ajudar vocês a aproveitar a estadia: recomendações "
              "pensadas para vocês, serviços extras e todas as informações do apartamento.",
        "EN": "We're delighted to host you at **{piso}**, in the **{distrito}** district. "
              "Check-in is on **{llegada}** and check-out on **{salida}** ({noches} nights). "
              "This app will help you make the most of your stay: tailored tips, extra services "
              "and everything about the apartment.",
    },
    "firma": {"ES": "Con cariño, el equipo de B&B Investments",
              "PT": "Com carinho, a equipe da B&B Investments",
              "EN": "Warm regards, the B&B Investments team"},
    "tiempo_hoy": {"ES": "El tiempo hoy en Madrid", "PT": "O tempo hoje em Madri", "EN": "Today's weather in Madrid"},
    "tiempo_desc": {"ES": "Soleado, mínima 6 °C", "PT": "Ensolarado, mínima 6 °C", "EN": "Sunny, low 6 °C"},
    "tus_intereses": {"ES": "¿Qué les gustaría hacer en Madrid?",
                      "PT": "O que vocês gostariam de fazer em Madri?",
                      "EN": "What would you like to do in Madrid?"},
    "intereses_ayuda": {"ES": "Elijan uno o varios. Usaremos esto para personalizar sus recomendaciones.",
                        "PT": "Escolham um ou vários. Usaremos isso para personalizar as recomendações.",
                        "EN": "Pick one or more. We'll use this to personalise your tips."},
    "datos_reserva": {"ES": "Datos de la reserva (los completa el gestor)",
                      "PT": "Dados da reserva (preenchidos pelo gestor)",
                      "EN": "Booking details (filled in by the manager)"},
    "nombre": {"ES": "Nombre del huésped", "PT": "Nome do hóspede", "EN": "Guest name"},
    "distrito": {"ES": "Distrito", "PT": "Distrito", "EN": "District"},
    "piso": {"ES": "Piso", "PT": "Apartamento", "EN": "Apartment"},
    "llegada": {"ES": "Llegada", "PT": "Chegada", "EN": "Check-in"},
    "salida": {"ES": "Salida", "PT": "Saída", "EN": "Check-out"},
    "ir_recomendaciones": {"ES": "Ver mis recomendaciones →", "PT": "Ver minhas recomendações →",
                           "EN": "See my recommendations →"},

    # Qué ver y hacer
    "que_ver_titulo": {"ES": "Qué ver y hacer cerca de ustedes", "PT": "O que ver e fazer perto de vocês",
                       "EN": "Things to do near you"},
    "sin_intereses": {"ES": "Todavía no eligieron intereses. Vayan a **Bienvenida** para elegirlos.",
                      "PT": "Vocês ainda não escolheram interesses. Vão em **Boas-vindas** para escolher.",
                      "EN": "You haven't picked any interests yet. Go to **Welcome** to choose."},
    "solo_gratis": {"ES": "Solo gratis", "PT": "Só gratuitos", "EN": "Free only"},
    "solo_cerca": {"ES": "Cerca del piso (≤ {km} km)", "PT": "Perto do apartamento (≤ {km} km)",
                   "EN": "Near the apartment (≤ {km} km)"},
    "por_que": {"ES": "💡 Por qué se lo recomendamos", "PT": "💡 Por que recomendamos", "EN": "💡 Why we recommend it"},
    "a_km": {"ES": "a {km} km del piso", "PT": "a {km} km do apartamento", "EN": "{km} km from the apartment"},
    "gratis": {"ES": "Gratis", "PT": "Grátis", "EN": "Free"},
    "ninguna": {"ES": "No hay recomendaciones con estos filtros. Prueben a quitar alguno.",
                "PT": "Não há recomendações com esses filtros. Tentem tirar algum.",
                "EN": "No tips match these filters. Try removing one."},
    "razon_interes": {"ES": "Coincide con su interés: {interes}.", "PT": "Combina com seu interesse: {interes}.",
                      "EN": "Matches your interest: {interes}."},
    "razon_resenas": {"ES": "El {pct} % de las reseñas de pisos en {distrito} hablan de este tema (dato real, Inside Airbnb).",
                      "PT": "{pct} % das avaliações de apartamentos em {distrito} falam desse tema (dado real, Inside Airbnb).",
                      "EN": "{pct}% of reviews of apartments in {distrito} mention this topic (real data, Inside Airbnb)."},
    "razon_cerca": {"ES": "Está muy cerca: a {km} km del piso.", "PT": "Fica muito perto: a {km} km do apartamento.",
                    "EN": "It's very close: {km} km from the apartment."},
    "razon_gratis": {"ES": "Es gratis.", "PT": "É grátis.", "EN": "It's free."},
    "temas_distrito": {"ES": "Lo que más destacan los huéspedes de {distrito}",
                       "PT": "O que os hóspedes mais destacam em {distrito}",
                       "EN": "What guests highlight most about {distrito}"},
    "temas_ayuda": {"ES": "Palabras más características de las reseñas reales del distrito (modelo TF-IDF).",
                    "PT": "Palavras mais características das avaliações reais do distrito (modelo TF-IDF).",
                    "EN": "Most distinctive words in real reviews from the district (TF-IDF model)."},
    "opinion_real": {"ES": "Lo que dijo un huésped", "PT": "O que disse um hóspede", "EN": "What a guest said"},

    # Servicios
    "serv_titulo": {"ES": "Servicios extra", "PT": "Serviços extras", "EN": "Extra services"},
    "serv_intro": {"ES": "Reserven lo que necesiten y lo dejamos listo para ustedes.",
                   "PT": "Reservem o que precisarem e deixamos tudo pronto para vocês.",
                   "EN": "Book what you need and we'll have it ready for you."},
    "reservar": {"ES": "Reservar", "PT": "Reservar", "EN": "Book"},
    "reservado_ok": {"ES": "¡Listo! Reservaron: {serv}. El gestor recibirá el aviso.",
                     "PT": "Pronto! Vocês reservaram: {serv}. O gestor receberá o aviso.",
                     "EN": "Done! You booked: {serv}. The manager has been notified."},
    "mis_reservas": {"ES": "Mis reservas", "PT": "Minhas reservas", "EN": "My bookings"},
    "total": {"ES": "Total", "PT": "Total", "EN": "Total"},
    "cancelar_todo": {"ES": "Vaciar reservas", "PT": "Esvaziar reservas", "EN": "Clear bookings"},
    "traslado": {"ES": "Traslado al aeropuerto", "PT": "Traslado ao aeroporto", "EN": "Airport transfer"},
    "traslado_d": {"ES": "Coche privado entre el piso y Barajas (T1-T4).", "PT": "Carro privado entre o apartamento e Barajas (T1-T4).",
                   "EN": "Private car between the apartment and Barajas (T1-T4)."},
    "llegada_temprana": {"ES": "Llegada temprana", "PT": "Check-in antecipado", "EN": "Early check-in"},
    "llegada_temprana_d": {"ES": "Entren al piso desde las 11:00.", "PT": "Entrem no apartamento a partir das 11:00.",
                           "EN": "Get into the apartment from 11:00."},
    "limpieza_extra": {"ES": "Limpieza extra", "PT": "Limpeza extra", "EN": "Extra cleaning"},
    "limpieza_extra_d": {"ES": "Una limpieza completa durante su estancia.", "PT": "Uma limpeza completa durante a estadia.",
                         "EN": "A full clean during your stay."},
    "sabanas": {"ES": "Cambio de sábanas y toallas", "PT": "Troca de lençóis e toalhas", "EN": "Fresh sheets and towels"},
    "sabanas_d": {"ES": "Juego completo para todas las camas.", "PT": "Jogo completo para todas as camas.",
                  "EN": "A full set for every bed."},
    "equipaje": {"ES": "Guarda equipaje", "PT": "Guarda-volumes", "EN": "Luggage storage"},
    "equipaje_d": {"ES": "Dejen sus maletas el día de salida hasta las 20:00.", "PT": "Deixem as malas no dia da saída até as 20:00.",
                   "EN": "Leave your bags on check-out day until 20:00."},

    # Mi estancia
    "estancia_titulo": {"ES": "Mi estancia", "PT": "Minha estadia", "EN": "My stay"},
    "tipo_estancia": {"ES": "Tipo de estancia", "PT": "Tipo de estadia", "EN": "Type of stay"},
    "corta": {"ES": "Estancia corta (turística)", "PT": "Estadia curta (turística)", "EN": "Short stay (tourist)"},
    "media": {"ES": "Media estancia (temporada, 28 noches o más)", "PT": "Média estadia (temporada, 28 noites ou mais)",
              "EN": "Mid-term stay (seasonal, 28+ nights)"},
    "condiciones": {"ES": "Condiciones de su estancia", "PT": "Condições da sua estadia", "EN": "Your stay conditions"},
}

CONDICIONES = {
    "corta": [
        {"ES": "🔑 **Entrada:** desde las 15:00 (llegada temprana disponible en Servicios).",
         "PT": "🔑 **Entrada:** a partir das 15:00 (check-in antecipado em Serviços).",
         "EN": "🔑 **Check-in:** from 15:00 (early check-in available under Services)."},
        {"ES": "🚪 **Salida:** antes de las 11:00. Dejen las llaves en la caja de seguridad.",
         "PT": "🚪 **Saída:** até as 11:00. Deixem as chaves no cofre.",
         "EN": "🚪 **Check-out:** by 11:00. Leave the keys in the lockbox."},
        {"ES": "📶 **Wifi:** red `BB_Madrid` · clave `bienvenidos2026` [ejemplo].",
         "PT": "📶 **Wi-fi:** rede `BB_Madrid` · senha `bienvenidos2026` [exemplo].",
         "EN": "📶 **Wi-Fi:** network `BB_Madrid` · password `bienvenidos2026` [sample]."},
        {"ES": "🤫 **Horario de silencio:** de 22:00 a 08:00, por respeto a los vecinos.",
         "PT": "🤫 **Horário de silêncio:** das 22:00 às 08:00, por respeito aos vizinhos.",
         "EN": "🤫 **Quiet hours:** 22:00 to 08:00, out of respect for neighbours."},
        {"ES": "🚫 **No se permiten fiestas ni eventos** en el piso.",
         "PT": "🚫 **Não são permitidas festas nem eventos** no apartamento.",
         "EN": "🚫 **No parties or events** in the apartment."},
    ],
    "media_extra": [
        {"ES": "📄 **Contrato de temporada:** se firma un contrato por escrito que indica el motivo de la estancia "
               "(trabajo, estudios, salud…), como exige la normativa.",
         "PT": "📄 **Contrato de temporada:** assina-se um contrato por escrito indicando o motivo da estadia "
               "(trabalho, estudos, saúde…), como exige a lei.",
         "EN": "📄 **Seasonal lease:** a written contract stating the reason for the stay (work, studies, health…), "
               "as required by law."},
        {"ES": "💶 **Fianza:** una mensualidad, que se devuelve al final si el piso queda en buen estado [ejemplo].",
         "PT": "💶 **Caução:** um mês de aluguel, devolvido no final se o apartamento estiver em bom estado [exemplo].",
         "EN": "💶 **Deposit:** one month's rent, refunded at the end if the apartment is in good condition [sample]."},
        {"ES": "💡 **Suministros:** luz, agua, gas e internet incluidos hasta 80 €/mes; el exceso se cobra aparte [ejemplo].",
         "PT": "💡 **Contas:** luz, água, gás e internet incluídos até 80 €/mês; o excedente é cobrado à parte [exemplo].",
         "EN": "💡 **Utilities:** electricity, water, gas and internet included up to €80/month; any excess is billed [sample]."},
        {"ES": "🧹 **Limpieza:** una limpieza incluida cada dos semanas [ejemplo].",
         "PT": "🧹 **Limpeza:** uma limpeza incluída a cada duas semanas [exemplo].",
         "EN": "🧹 **Cleaning:** one clean included every two weeks [sample]."},
    ],
}


def t(clave: str, idioma: str, **kw) -> str:
    texto = T[clave].get(idioma, T[clave]["ES"])
    return texto.format(**kw) if kw else texto
