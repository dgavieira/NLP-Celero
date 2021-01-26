import pandas as pd
from data_process import *

df = pd.read_csv('IMDB-Dataset.csv', encoding='utf8')

df = acrescenta_classificacao(df)

df = remove_stopwords(df)

df = remove_tags(df)

df = remove_pontuacao(df)

df = stemming(df)

df.to_csv('imdb_dataset_tratado.csv', index=False)

print(df.head(10))
