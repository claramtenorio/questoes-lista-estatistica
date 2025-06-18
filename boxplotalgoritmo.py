import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn

#dados da imagem
dados_a = [12, 15, 18, 22, 25, 26, 28, 30, 32, 35, 38, 40, 42, 45, 50, 52, 55, 60, 65, 70]
dados_b = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 45, 50, 60, 80]

#item i.

#para o algoritmo A
q1_a = numpy.percentile(dados_a, 25)
median_a = numpy.percentile(dados_a, 50)
q3_a = numpy.percentile(dados_a, 75)
iqr_a = q3_a - q1_a
min_a = numpy.min(dados_a)
max_a = numpy.max(dados_a)
lower_bound_a = q1_a - 1.5 * iqr_a
upper_bound_a = q3_a + 1.5 * iqr_a
outliers_a = [x for x in dados_a if x < lower_bound_a or x > upper_bound_a]

#para o algoritmo B
q1_b = numpy.percentile(dados_b, 25)
median_b = numpy.percentile(dados_b, 50)
q3_b = numpy.percentile(dados_b, 75)
iqr_b = q3_b - q1_b
min_b = numpy.min(dados_b)
max_b = numpy.max(dados_b)
lower_bound_b = q1_b - 1.5 * iqr_b
upper_bound_b = q3_b + 1.5 * iqr_b
outliers_b = [x for x in dados_b if x < lower_bound_b or x > upper_bound_b]

print("i. componentes boxplot")
print("\Algoritmo A:")
print(f"  Mínimo: {min_a}")
print(f"  Q1: {q1_a}")
print(f"  Mediana (Q2): {median_a}")
print(f"  Q3: {q3_a}")
print(f"  Máximo: {max_a}")
print(f"  Outliers: {outliers_a}")
print(f"  IQR (Q3 - Q1): {iqr_a:.2f}")

print("\Algoritmo B:")
print(f"  Mínimo: {min_b}")
print(f"  Q1: {q1_b}")
print(f"  Mediana (Q2): {median_b}")
print(f"  Q3: {q3_b}")
print(f"  Máximo: {max_b}")
print(f"  Outliers: {outliers_b}")
print(f"  IQR (Q3 - Q1): {iqr_b:.2f}")


#para fazer o gráfico
df = pandas.DataFrame({
    'Algoritmo': ['A'] * len(dados_a) + ['B'] * len(dados_b),
    'Tempo de resposta (ms)': dados_a + dados_b
})

plt.figure(figsize=(10, 6))
seaborn.boxplot(x='Algoritmo', y='Tempo de resposta (ms)', data=df, palette='viridis')
plt.title('Bboxplot dos tempos de resposta')
plt.ylabel('Tempo de resposta (ms)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
