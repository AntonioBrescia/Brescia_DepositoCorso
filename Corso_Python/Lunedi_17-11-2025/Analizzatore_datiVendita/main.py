import input_vendite
import calcoli
import stampa_risultati

def main():
    # Leggi le vendite dall'utente
    vendite = input_vendite.leggi_vendite()
    
    if not vendite:
        print("Nessun dato di vendita inserito.")
        return

    # Calcola totale e media
    totale = calcoli.calcola_totale(vendite)
    media = calcoli.calcola_media(vendite)

    # Stampa totale e media
    stampa_risultati.stampa_totale_media(totale, media)

    # Trova i giorni con vendite sopra la media
    giorni = calcoli.giorni_sopra_media(vendite)

    # Stampa i giorni sopra la media
    stampa_risultati.stampa_giorni_sopra_media(giorni, vendite)

    main()
