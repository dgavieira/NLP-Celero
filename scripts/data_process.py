from string import punctuation

import nltk
from nltk import *
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


def acrescenta_classificacao(df):
    classificacao = df['sentiment'].replace(['negative', 'positive'], [0, 1])
    df['classificacao'] = classificacao
    return df


def remove_stopwords(df):
    palavras_irrelevantes = nltk.corpus.stopwords.words('english')
    frase_processada = list()
    token_espaco = tokenize.WhitespaceTokenizer()

    for opiniao in df['review']:
        nova_frase = list()
        palavras_texto = token_espaco.tokenize(opiniao)
        for palavra in palavras_texto:
            if palavra not in palavras_irrelevantes:
                nova_frase.append(palavra)
        frase_processada.append(' '.join(nova_frase))

    df['stopwords'] = frase_processada

    return df


def remove_tags(df):
    df['stopwords'] = df['stopwords'].str.replace(r'<br />', '')
    df['stopwords'] = df['stopwords'].str.replace(r'\'style\'', '')

    return df


def remove_pontuacao(df):
    palavras_irrelevantes = nltk.corpus.stopwords.words('english')
    token_pontuacao = tokenize.WordPunctTokenizer()
    pontuacao = list()
    for ponto in punctuation:
        pontuacao.append(ponto)

    pontuacao_stopwords = pontuacao + palavras_irrelevantes
    frase_processada = list()
    for opiniao in df['stopwords']:
        nova_frase = list()
        opiniao = opiniao.lower()
        palavras_texto = token_pontuacao.tokenize(opiniao)
        for palavra in palavras_texto:
            if palavra not in pontuacao_stopwords:
                nova_frase.append(palavra)
        frase_processada.append(' '.join(nova_frase))

    df['punctuation'] = frase_processada
    '''
    df['punctuation'] = df['punctuation'].str.replace(r' .. ', ' ')
    df['punctuation'] = df['punctuation'].str.replace(r' ... ', ' ')
    df['punctuation'] = df['punctuation'].str.replace(r' .... ', ' ')
    '''
    return df


def stemming(df):
    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    palavras_irrelevantes = nltk.corpus.stopwords.words('english')
    token_pontuacao = tokenize.WordPunctTokenizer()
    pontuacao = list()
    for ponto in punctuation:
        pontuacao.append(ponto)

    pontuacao_stopwords = pontuacao + palavras_irrelevantes
    frase_processada = list()
    for opiniao in df['stopwords']:
        nova_frase = list()
        opiniao = opiniao.lower()
        palavras_texto = token_pontuacao.tokenize(opiniao)
        for palavra in palavras_texto:
            if palavra not in pontuacao_stopwords:
                nova_frase.append(stemmer.stem(palavra))
        frase_processada.append(' '.join(nova_frase))

    df['stemming'] = frase_processada

    return df

