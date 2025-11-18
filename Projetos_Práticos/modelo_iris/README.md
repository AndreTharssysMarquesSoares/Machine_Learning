Utilize o algoritmo K-Means para agrupar as amostras do conjunto de dados Iris, otimizando os hiperparâmetros do modelo com o auxílio da biblioteca Optuna. O dataset Iris possui 150 amostras de flores, divididas em três espécies (Setosa, Versicolor e Virginica), cada uma descrita por quatro atributos numéricos:

Comprimento da sépala (sepal length)
Largura da sépala (sepal width)
Comprimento da pétala (petal length)
Largura da pétala (petal width)
Target:

0: setosa
1: versicolor
2: virginica

Código Base
Você pode importar o dataset diretamente do scikit-learn com o seguinte código:

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data         # Atributos das flores
y = iris.target       # Classes reais (usadas apenas para avaliação)