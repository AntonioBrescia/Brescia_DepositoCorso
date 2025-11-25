from veicoloTrasporto import VeicoloTrasporto
class Furgone(VeicoloTrasporto):
    tipo = "Furgone"
    def __init__(self, targa, peso_massimo, alimentazione):
        super().__init__(targa, peso_massimo)
        self.alimentazione = alimentazione.lower()
        
    def costo_manutenzione(self):
        if self.alimentazione == "elettrico":
            return 200
        else:
            return 150

