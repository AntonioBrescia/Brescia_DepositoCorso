from studente import Studente
from professore import Professore

def main():
    studenti = []
    nome_prof = input("Nome professore: ")
    materia = input("Materia insegnata: ")
    prof = Professore(nome_prof, 40, materia)  

    print("Benvenuto, Prof.", prof.get_nome())

    while True:
        print("--- MENU ---")
        print("1. Aggiungi studente")
        print("2. Inserisci voto")
        print("3. Visualizza studenti")
        print("4. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                nome = input("Nome studente: ")
                eta = int(input("Età studente: "))
                stud = Studente(nome, eta)
                studenti.append(stud)
                print("Studente", stud.get_nome(), "aggiunto.")

            case "2":
                if len(studenti) == 0:
                    print("Nessuno studente registrato.")
                else:
                    for i in range(len(studenti)):
                        print(i+1, "-", studenti[i].get_nome())
                    idx = int(input("Seleziona studente: ")) - 1
                    voto = int(input("Inserisci voto (0-10): "))
                    prof.inserisci_voto(studenti[idx], voto)

            case "3":
                if len(studenti) == 0:
                    print("Nessuno studente registrato.")
                else:
                    for s in studenti:
                        s.presentazione()

            case "4":
                print("exit..")
                break

            case _:
                print("Opzione non valida.")

main()
