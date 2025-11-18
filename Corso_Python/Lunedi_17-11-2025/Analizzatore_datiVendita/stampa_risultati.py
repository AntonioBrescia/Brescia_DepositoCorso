def stampa_totale_media(totale, media):
    print(f"\nTotale vendite: {totale}€")
    print(f"Media vendite: {media}€")  

def stampa_giorni_sopra_media(giorni, vendite):
    if not giorni:
        print("Nessun giorno con vendite sopra la media.")
    else:
        print("Giorni con vendite sopra la media:")
        for g in giorni:
            print(f"  Giorno {g}: {vendite[g-1]}€")  
