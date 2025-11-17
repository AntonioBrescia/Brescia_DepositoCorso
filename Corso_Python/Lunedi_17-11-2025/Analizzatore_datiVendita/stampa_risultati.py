# stampa_risultati.py

def stampa_totale_media(totale, media):
    """Stampa il totale e la media delle vendite."""
    print(f"\nTotale vendite: {totale}€")
    print(f"Media vendite: {media}€")  

def stampa_giorni_sopra_media(giorni, vendite):
    """Stampa i giorni in cui le vendite sono sopra la media."""
    if not giorni:
        print("Nessun giorno con vendite sopra la media.")
    else:
        print("Giorni con vendite sopra la media:")
        for g in giorni:
            print(f"  Giorno {g}: {vendite[g-1]}€")  # g-1 per l'indice nella lista
