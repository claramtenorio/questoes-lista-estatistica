import pandas
import matplotlib.pyplot as plt

dados = pandas.read_csv('dados_alunos.csv')

#conta quantos alunos estão em cada curso
distribuicao_pcurso = dados['Curso'].value_counts()

#cria um gráfico de barras para visualizar a distribuição
plt.figure(figsize=(10, 6))
#grafico de barras
distribuicao_pcurso.plot(kind='bar')
plt.title('Distribuição de alunos por curso')
#parametros do gráfico
plt.xlabel('Curso')
plt.ylabel('Número de Alunos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()