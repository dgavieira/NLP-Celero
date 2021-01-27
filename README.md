# NLP-Celero
Projeto de desenvolvimento em Natural Language Processing utilizando a base de dados do IMDB

O projeto tem por objetivo tratar a base de dados aciimdb <a href="http://ai.stanford.edu/~amaas/data/sentiment/" target="_top">Download Page</a> e em seguida desenvolver um analisador de sentimento para as avaliações de filme.

O idioma da base de dados é inglês.

## Tecnologias Utilizadas
Linguagem de Programação Python Bibliotecas:

    * Pandas - Leitura de dados.
    * Numpy - Manipulação de dados.
    * nltk - Ferramenta para tratamento de dados em Natural Language Processing.
    * sklearn - Ferramenta para treinamento de modelos estatísticos e medida de performance.
    * matplotlib - Ferramenta para visualização de dados.
    * wordcloud - Ferramenta para construção de nuvem de dados.
    * Seaborn - Ferramenta para visualização de dados com recursos mais esteticamente agradáveis.

## Como rodar o código?
É possível rodar o código de três maneiras:

### Google Colab Notebook
Por essa maneira é possível verificar toda a análise exploratória até a definição do modelo a ser implementado.
Abra o arquivo NLP_teste.ipynb em uma instância do Jupyter Notebook ou no [Google Colab](http://colab.research.google.com/) para executá-lo. (É necessário login no google).

### Arquivos Python separados
Os arquivos Python separados na pasta scripts são possíveis de executar cada um dos trechos do processamento de forma separada:

   * Data Extraction - Extrai os arquivos de texto para um csv - data_extract.py
   * Data Transform - Converte o csv em um pandas dataframe possível de analisar - data_trasform.py
   * Data Process - Aplica técnicas de processamento de linguagem natural - main_data_process.py
   * Data Classification - Classifica os dados em formato de treino ou teste conforme solicitado - main_data_classification.py

Execute o código na sequência indicada acima para verificar o funcionamento do pipeline.

### Arquivo python main.py
Coloca o pipeline em funcionamento em um único script.

