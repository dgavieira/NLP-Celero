from concat_data import *
import pandas as pd

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

#Save datasets
df_train.to_csv('train.csv', index=False)
df_test.to_csv('test.csv', index=False)

#Concatenate full dataframe
df = concat_all(df_train, df_test)

df.to_csv('dataset.csv', index=False)

