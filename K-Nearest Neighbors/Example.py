from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Um classificador KNN (K-Nearest Neighbors) é um algoritmo de aprendizado de máquina supervisionado que é utilizado tanto para tarefas de classificação quanto de regressão.
# Classificação:
# Definição: A tarefa de classificação envolve atribuir uma instância ou objeto a uma classe pré-definida a partir de um conjunto finito de classes. Em outras palavras, o objetivo é prever a categoria ou classe à qual uma nova instância pertence.
# Exemplo: Classificar e-mails como "spam" ou "não spam", prever se um paciente tem uma doença específica com base em dados médicos, ou identificar se uma imagem contém um gato ou um cachorro.
# Saída do Modelo: A saída do modelo é uma classe ou categoria discreta.
# Regressão:
# Definição: A tarefa de regressão envolve prever um valor numérico ou contínuo com base nas características de uma instância. Em vez de categorias, o objetivo é estimar uma quantidade real.
# Exemplo: Prever o preço de uma casa com base em suas características (número de quartos, área, etc.), estimar a receita de vendas de um produto em um determinado mês, ou prever a temperatura com base em variáveis meteorológicas.
# Saída do Modelo: A saída do modelo é um valor numérico contínuo.

# Exemplo de dados de entrada (substitua isso pelos seus dados reais)
dados = [
    [1, 2, 3, 4, 5],   # Exemplo 1
    [2, 3, 4, 5, 6],   # Exemplo 2
    [5, 4, 3, 2, 1],   # Exemplo 3
]

# Rótulos correspondentes aos exemplos (substitua isso pelos seus rótulos reais)
rotulos = ['Classe_A', 'Classe_B', 'Classe_A']  # Substitua pelos seus rótulos reais

# Divida os dados em conjuntos de treinamento e teste
dados_treinamento, dados_teste, rotulos_treinamento, rotulos_teste = train_test_split(dados, rotulos, test_size=0.2, random_state=42)

# Certifique-se de que há pelo menos n_neighbors amostras no conjunto de treinamento
n_neighbors = min(3, len(dados_treinamento))

# Crie um classificador KNN
knn = KNeighborsClassifier(n_neighbors=n_neighbors)

# Treine o modelo
knn.fit(dados_treinamento, rotulos_treinamento)

# Faça previsões no conjunto de teste
previsoes = knn.predict(dados_teste)

# Calcule a acurácia
acuracia = accuracy_score(rotulos_teste, previsoes)
print(f'Acurácia do KNN: {acuracia:.2f}')

# Exemplo de previsão para uma nova instância
nova_instancia = [[3, 4, 5, 2, 1]]  # Substitua isso pelos valores da nova instância
previsao_nova_instancia = knn.predict(nova_instancia)
print(f'Previsão para a nova instância: {previsao_nova_instancia[0]}')