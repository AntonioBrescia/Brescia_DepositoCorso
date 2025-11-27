import pandas as pd


# Dati di esempio

data = {

    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],

    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],

    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],

    'Vendite': [100, 200, 150, 300, 250]

}


df = pd.DataFrame(data)


# Creazione della tabella pivot

pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

# esempio di group by

grouped_df = df.groupby('Prodotto')['Vendite'].sum()
print(grouped_df)
print("-"*60)

print(pivot_df)



# ESEMPIO PRENDENDO I DATI DA CSV 

# CARICO IL CSV E LO LEGGO TRASFORMANDO IN DATAFRAME 
file_path = 'Corso_Python/12_Giovedi_27-11-2025/Esercizio2/prodotti.csv'

df2 = pd.read_csv(file_path)

# CREO LA TABELLA PIVOT 
pivot_prodotti = df2.pivot_table(values='quantita' , index='prodotto', columns='citta', aggfunc='mean', fill_value=0)
print(pivot_prodotti)

# esempio di group by

grouped_df_csv = df2.groupby('quantita')['prezzo_unitario'].sum()
print("-"*60 , "from csv")

print(grouped_df_csv)
print("-"*60)

print(pivot_prodotti)
