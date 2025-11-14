def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecizione della funzione")
        funzione()
        print("Dopo dell'esecizione della funzione")
    return wrapper
@decoratore
def saluta():
    print("Ciao!")
    
saluta()
# funzione agggregativa che modificano il comportamento di altre funzionalità senza modificarne direttamente il codice 

def decoratore_con_argomenti(funzione):
    def wrapper(*args,**kwargs):
        print("Prima")
        risultato = funzione(*args,**kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a,b):
    print(a+b)
    return a + b
print("risultato è: ", somma(3,4))