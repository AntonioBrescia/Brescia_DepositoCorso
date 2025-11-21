from veicoloTrasporto import VeicoloTrasporto

class Camion(VeicoloTrasporto):
    tipo = "Camion"

    def __init__(self, targa, peso_massimo, numero_assi):
        super().__init__(targa, peso_massimo)
        self.numero_assi = numero_assi

    def costo_manutenzione(self):
        return 100 * self.numero_assi + self._peso_massimo