import pandas as pd


def transpose_data(df):
    df = df.T
    return df


def concat_train(df_neg, df_pos, df_unsup):
    df_neg.columns = ['reviews']
    df_pos.columns = ['reviews']
    df_unsup.columns = ['reviews']

    df_neg.loc[:, 'sentiment'] = 'negative'
    df_pos.loc[:, 'sentiment'] = 'positive'
    df_unsup.loc[:, 'sentiment'] = 'unsuposed'

    df_train = pd.concat([df_neg, df_pos, df_unsup], axis=0, ignore_index=True)
    return df_train


def concat_test(df_neg, df_pos):
    df_neg.columns = ['reviews']
    df_pos.columns = ['reviews']

    df_neg.loc[:, 'sentiment'] = 'negative'
    df_pos.loc[:, 'sentiment'] = 'positive'

    df_test = pd.concat([df_neg, df_pos], axis=0, ignore_index=True)
    return df_test


def concat_all(df_train, df_test):
    df = pd.concat([df_train, df_test], axis=0, ignore_index=True)
    return df
