# -atv_regressao_linear_multipla_llm
Desafio modulo regressa linear multipla rocketseat

O objetivo deste exercício é construir um modelo de machine learning capaz de prever o valor do aluguel de um imóvel com base em suas características. Através da análise de um dataset de imóveis, você irá:

1. **Explorar os dados:** Realizar uma análise exploratória dos dados para entender a distribuição das variáveis, identificar possíveis outliers e correlações.
2. **Preparar os dados:** Limpar os dados, tratar valores ausentes e codificar variáveis categóricas.
3. **Construir um modelo:** Utilizar um algoritmo de regressão linear para construir um modelo que relacione as características do imóvel com o valor do aluguel.
4. **Avaliar o modelo:** Avaliar a performance do modelo utilizando métricas adequadas e analisar os resíduos para verificar a qualidade das previsões.
5. **Interpretar os resultados:** Analisar os coeficientes do modelo para entender a importância de cada variável na previsão do valor do aluguel.

**Etapas:**

1. **Carregar e explorar o dataset:** Carregue o arquivo CSV fornecido e explore os dados utilizando as funções do pandas.
2. **Pré-processamento:** Realize as seguintes tarefas:
    - Identifique e trate valores ausentes.
    - Remova outliers.
    - Codifique as variáveis categóricas.
    - Escale as variáveis numéricas (se necessário).
3. **Construção do modelo:**
    - Divida os dados em conjuntos de treino e teste.
    - Crie um pipeline para pré-processar os dados e treinar o modelo de regressão linear.
    - Treine o modelo utilizando o conjunto de treino.
4. **Avaliação do modelo:**
    - Faça previsões sobre o conjunto de teste.
    - Calcule métricas de desempenho (R², MAE, RMSE).
    - Analise os resíduos para verificar a qualidade do modelo.
5. **Interpretação dos resultados:**
    - Analise os coeficientes do modelo para entender a importância de cada variável.
    - Discuta as limitações do modelo e sugira possíveis melhorias.
