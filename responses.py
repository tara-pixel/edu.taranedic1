def get_bot_response(message):
    message=message.lower()
    if "zdravo" in message or "cao" in message:
        return "Zdravo! Kako mogu da ti pomognem u vezi nastave?"
    elif "raspored" in message:
        return "Raspored casova se nalazi na oglasnoj tabli skole ili na sajtu."
    elif "učionica" in message:
        return "Koju učionicu tražiš? Mogu da ti pomognem ako znaš broj."
    elif "pravila" in message:
        return "Pravila skole ukljucuju:dolazak na vreme, postovanje nastavnika i drugova,.."
    elif "test" in message:
        return "Ako imas test, preporucujem da ponovis beleske i probas neki online kviz."
    elif "skola" in message:
        return "Nasa skola se zove Tehnicka skola."
    elif "smena" in message:
        return "1.smena pocinje u 7:30, a druga u 13:30."
    else:
        return "Nisam siguran kako da odgovorim. Mozes li da ponovis pitanje?"