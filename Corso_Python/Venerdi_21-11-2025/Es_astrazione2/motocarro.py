from veicoloTrasporto import VeicoloTrasporto
class Motocarro(VeicoloTrasporto):
    tipo = "Motocarro"
    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo)
        self.anni_servizio = anni_servizio
        
    def costo_manutenzione(self):
        return 50 * self.anni_servizio

