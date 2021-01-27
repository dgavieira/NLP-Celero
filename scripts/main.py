from concat_data import *
from data_classification import *
from data_process import *
from read_test import *
from read_train import *

# path defining

path_test_pos = str(input('Insert test path for positive data'))
path_test_neg = str(input('Insert test path for negative data'))

path_train_pos = str(input('Insert train path for positive data'))
path_train_neg = str(input('Insert train path for negative data'))
path_train_unsup = str(input('Insert train path for unsuposed data'))

# Data Extraction

read_test_pos(path_test_pos)
read_test_neg(path_test_neg)

read_train_pos(path_train_pos)
read_train_neg(path_train_neg)
read_train_unsup(path_train_unsup)

# Data Transform

# Load data from data extraction
df_test_neg = pd.read_csv('test_neg.csv', encoding='utf8', header=None)
df_test_pos = pd.read_csv('test_pos.csv', encoding='utf8', header=None)

df_train_neg = pd.read_csv('train_neg.csv', encoding='utf8', header=None)
df_train_pos = pd.read_csv('train_pos.csv', encoding='utf8', header=None)
df_train_unsup = pd.read_csv('train_unsup.csv', encoding='utf8', header=None)

# Transpose dataframes
df_test_neg = transpose_data(df_test_neg)
df_test_pos = transpose_data(df_test_pos)

df_train_pos = transpose_data(df_train_pos)
df_train_neg = transpose_data(df_train_neg)
df_train_unsup = transpose_data(df_train_unsup)

# Concatenate DataFrames
df_train = concat_train(df_train_neg, df_train_pos, df_train_unsup)
df_test = concat_test(df_test_neg, df_test_pos)

# Save datasets
df_train.to_csv('train.csv', index=False)
df_test.to_csv('test.csv', index=False)

# Concatenate full dataframe
df = concat_all(df_train, df_test)

df.to_csv('dataset.csv', index=False)

# Data Processing

df = pd.read_csv('IMDB-Dataset.csv', encoding='utf8')

df = acrescenta_classificacao(df)

df = remove_stopwords(df)

df = remove_tags(df)

df = remove_pontuacao(df)

df = stemming(df)

df.to_csv('imdb_dataset_tratado.csv', index=False)

print(df.head(10))

# Data Classification
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
