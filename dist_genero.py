import pandas
import matplotlib.pyplot as plt

dados = pandas.read_csv('dados_alunos.csv')

#distribuição percentual de gêneros
distribuicao_pgenero = dados['Genero'].value_counts()

#converte para percentual
distribuicao_porcentagem = distribuicao_pgenero / len(dados) * 100

#cria um gráfico de pizza para visualizar a distribuição
plt.figure(figsize=(8, 8))
plt.pie(distribuicao_porcentagem, labels=distribuicao_porcentagem.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Distribuição percentual de gêneros')
plt.axis('equal') #para ser um circulo perfeito
plt.show()