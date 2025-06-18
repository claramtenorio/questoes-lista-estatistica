import pandas
import matplotlib.pyplot as plt

dados = pandas.read_csv('dados_alunos.csv')

#cria a representacao grafica com as notas e cursos
plt.figure(figsize=(12, 7))
dados.boxplot(column='Nota', by='Curso', grid=False)
plt.title('Notas por curso')
#parametros do gráfico
plt.xlabel('Curso')
plt.ylabel('Nota')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()