import pandas as pd
import glob
import os


# método que lê os dados marcados como teste e avaliação negativa
# considera-se a estrutura da pasta

def read_test_neg(path):
    # essa seção lê todos os arquivos presentes em uma pasta os abre
    all_files = glob.glob(os.path.join(path, "*.txt"))

    # cada arquivo de texto da pasta gera um Pandas DataFrame
    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter='\t') for f in all_files)

    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)

    # aqui prefere-se não colocar outros valores por termos de performance do glob.
    concatenated_df.to_csv('test_neg.csv', index=False)


def read_test_pos(path):
    # para esse método utiliza-se a mesma lógica do anterior, focando nos arquivos marcados como
    # test/neg

    all_files = glob.glob(os.path.join(path, "*.txt"))

    df_from_each_file = (pd.read_csv(f, encoding='utf8', delimiter='\t') for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True, axis=0)
