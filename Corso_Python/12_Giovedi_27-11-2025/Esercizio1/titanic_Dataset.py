import pandas as pd
import numpy as np
file_path = r"Corso_Python\12_Giovedi_27-11-2025\Esercizio1\train.csv"
df = pd.read_csv(file_path)
# Visualizzare le prime 5 righe
print("Prime 5 righe:")
print(df.head(5))

# Visualizzare le ultime 5 righe
print("Ultime 5 righe:")
print(df.tail(5))
# Visualizzare i tipi di dati
print(df.dtypes)
media = df.mean(numeric_only=True) 
print("Media")
print(media)
mediana = df.median(numeric_only=True)
print("Mediana")
print(mediana)
dev_std = df.std(numeric_only=True)
print("Deviazione standard")
print(dev_std)
#rimuovere i duplicati 
df = df.drop_duplicates() 




# TODO df['Categoria Età'] = df['Age'] >= 18 # se copresa tra 0-18 giovane, 19-65 adulto, oltre 65 senior


# pulire il file con dropna
df_cleaned = df.dropna()
#sostituisco i valori mancanti con la mediana della colonna
df['Age'] = df['Age'].fillna(df['Age'].median())
print("Dataframe pulito:" , df_cleaned)

output_file = r"Corso_Python\12_Giovedi_27-11-2025\Esercizio1\train_clean.csv"
df_cleaned.to_csv(output_file, index=False)
print(f"DataFrame pulito salvato")