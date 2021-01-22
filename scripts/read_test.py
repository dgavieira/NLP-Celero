import pandas as pd
import glob
import os

# método que lê os dados marcados como teste e avaliação negativa
# considera-se a estrutura da pasta

def read_test_neg():
    #essa seção lê todos os arquivos presentes em uma pasta os abre
    path = r'C:\Users\dgavi\Python-Projetos\acllmdb-small\test\neg'
    all_files = glob.glob(os.path.join(path, "*.txt"))

    #cada arquivo de texto da pasta gera um Pandas DataFrame
    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter='\t') for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=1)
    #aqui prefere-se não colocar outros valores por termos de performance do glob.

    concatenated_df.to_csv('test_neg.csv', index=False)

def read_test_pos():
    # para esse método utiliza-se a mesma lógica do anterior, focando nos arquivos marcados como
    # test/neg

    path = r'C:\Users\dgavi\Python-Projetos\acllmdb-small\test\pos'
    all_files = glob.glob(os.path.join(path, "*.txt"))

    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter='\t') for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=1)
    concatenated_df.to_csv('test_pos.csv', index=False)