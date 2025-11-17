def leggi_vendite():
    while True:
        input_utente = input("Inserisci gli importi delle vendite separati da spazi: ")
        if not input_utente.strip():  # input vuoto
            print("Non hai inserito nulla. Riprova.")
            continue

        valori = input_utente.split()
        vendite = []

        input_valido = True  # flag per controllare se tutti i valori sono numeri

        for v in valori:
            if v.lstrip("-").isdigit():  # consente anche numeri negativi
                vendite.append(int(v))
            else:
                print(f"Errore: '{v}' non è un numero intero. Riprova.")
                input_valido = False
                break  # esci dal ciclo e chiedi di reinserire tutto

        if input_valido:
            return vendite
