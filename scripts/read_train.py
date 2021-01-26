import pandas as pd
import glob
import os

def read_train_neg():
    path = r'C:\Users\dgavi\Python-Projetos\acllmdb-small\train\neg'
    # path = r'C:\Users\dgavi\Python-Projetos\aclImdb\test\neg'
    all_files = glob.glob(os.path.join(path, "*.txt"))

    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter="\t") for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)

    # print(concatenated_df.head(10))
    concatenated_df.to_csv('train_neg.csv', index=False)

def read_train_pos():
    path = r'C:\Users\dgavi\Python-Projetos\acllmdb-small\train\pos'
    all_files = glob.glob(os.path.join(path, "*.txt"))

    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter="\t") for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)
    
    # print(concatenated_df.head(10))
    concatenated_df.to_csv('train_pos.csv', index=False)

def read_train_unsup():
    path = r'C:\Users\dgavi\Python-Projetos\acllmdb-small\train\unsup'
    all_files = glob.glob(os.path.join(path, "*.txt"))

    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter="\t") for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)


    # print(concatenated_df.head(10))
    concatenated_df.to_csv('train_unsup.csv', index=False)