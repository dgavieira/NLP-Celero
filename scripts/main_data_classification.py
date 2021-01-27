import pandas as pd
from data_classification import *

df = pd.read_csv('imdb_dataset_tratado.csv', encoding='utf8')
# print(df.columns)

vetor = tfidf_tokenize(df, 'stemming')

treino = 'treino'
teste = 'teste'
coluna_classificacao = 'classificacao'

acuracia_treino = classifica_texto_lr(vetor, df, coluna_classificacao, treino)
print("Acurácia de Treino LR: {:.2f}%".format(acuracia_treino))

acuracia_teste = classifica_texto_lr(vetor, df, coluna_classificacao, teste)
print("Acurácia de Teste LR: {:.2f}%".format(acuracia_teste))
