from libreria import Libreria

mia_libreria = Libreria()

while True:
    print("\n--- Menu Libreria ---")
    print("1. Aggiungi libro")
    print("2. Rimuovi libro")
    print("3. Mostra catalogo")
    print("4. Cerca per titolo")
    print("5. Esci")

    scelta = input("Seleziona un'opzione: ")

    match scelta:
        case "1":
            isbn = input("Inserisci ISBN: ")
            titolo = input("Inserisci titolo: ")
            autore = input("Inserisci autore: ")
            mia_libreria.aggiungi_libro(isbn, titolo, autore)
            print("Libro aggiunto con successo.")

        case "2":
            isbn = input("Inserisci ISBN del libro da rimuovere: ")
            if mia_libreria.rimuovi_libro(isbn):
                print("Libro rimosso con successo.")
            else:
                print("Libro non trovato.")

        case "3":
            print("Catalogo completo:")
            mia_libreria.mostra_catalogo()

        case "4":
            titolo = input("Inserisci il titolo da cercare: ")
            print(f"Risultati per '{titolo}':")
            mia_libreria.cerca_per_titolo(titolo)

        case "5":
            print("Arrivederci!")
            break

        case _:
            print("Opzione non valida, riprova.")
