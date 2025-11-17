class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self):
        dx = float(input("Inserisci lo spostamento in x (dx): "))
        dy = float(input("Inserisci lo spostamento in y (dy): "))
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return (self.x**2 + self.y**2)**0.5


p = Punto(3, 4)
print("Distanza dall'origine:", p.distanza_da_origine())

p.muovi()  
print("Nuove coordinate:", p.x, p.y)
print("Nuova distanza dall'origine:", p.distanza_da_origine())
