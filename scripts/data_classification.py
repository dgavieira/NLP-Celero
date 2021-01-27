from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np


def tfidf_tokenize(df, coluna_texto):
    tfidf = TfidfVectorizer(lowercase=False, ngram_range=(1, 2))
    vetor_tfidf = tfidf.fit_transform(df[coluna_texto])
    return vetor_tfidf


def classifica_texto_lr(vetor_de_palavras, df, coluna_classificacao, mode):
    x_treino, y_treino, x_teste, y_teste = train_test_split(vetor_de_palavras,
                                                            df[coluna_classificacao])
    reg_log = LogisticRegression(solver='lbfgs')
    reg_log.fit(x_treino, y_treino)

    if mode == 'treino':
        reg_log.fit(x_treino, y_treino)
        score_treino = reg_log.fit(x_treino, y_treino)
        score_treino = reg_log.score(x_teste, y_teste)
        return score_treino
    if mode == 'teste':
        predict = reg_log.predict_proba(x_teste)
        predict_bol = predict[:, 1] >= 0.5
        predict_int = predict_bol.astype(np.int)
        score = accuracy_score(y_teste, predict_int)
        return score


