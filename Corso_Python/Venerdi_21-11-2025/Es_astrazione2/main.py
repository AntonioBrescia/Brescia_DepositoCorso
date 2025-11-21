from camion import Camion
from furgone import Furgone
from motocarro import Motocarro
from gestoreFlotta import GestoreFlotta

flotta = GestoreFlotta()

v1 = Camion("123456", 10000, 3)
v2 = Furgone("123456", 3000, "diesel")
v3 = Motocarro("123456", 800, 3)

flotta.aggiungi_veicolo(v1)
flotta.aggiungi_veicolo(v2)
flotta.aggiungi_veicolo(v3)

v1.carica(2000)
v1.carica(500)

v1.scarica()

v1.carica(500)


flotta.stampa_veicoli()


print("Costo totale manutenzione:", flotta.costo_totale_manutenzione(), "€")
