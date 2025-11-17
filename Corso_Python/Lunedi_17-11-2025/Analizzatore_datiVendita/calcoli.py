
def calcola_totale(vendite):
    return sum(vendite)

def calcola_media(vendite):
    if len(vendite) == 0:
        return 0
    return sum(vendite) / len(vendite)

def giorni_sopra_media(vendite):
    media = calcola_media(vendite)
    giorni = []
    for i in range(len(vendite)):
        if vendite[i] > media:
            giorni.append(i + 1)  
    return giorni