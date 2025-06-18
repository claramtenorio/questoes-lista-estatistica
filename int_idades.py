import pandas
import matplotlib.pyplot as plt

dados = pandas.read_csv('dados_alunos.csv')

#cria a representacao grafica para a idade dos alunos
plt.figure(figsize=(10, 6))
plt.hist(dados['Idade'], bins=5, edgecolor='black')
plt.title('Frequência de idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()