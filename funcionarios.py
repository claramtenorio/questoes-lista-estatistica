import csv
import statistics
from collections import Counter #para calcular num de filhos

def dados_sobre_funcionarios(file_path='funcionarios.csv'):
    
    funcionarios = []
        #abre e lê o arquivo
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            funcionarios.append(row)

    #Quantos funcionários existem na empresa? Quais são as informações que constam no cadastro?
    num_funcionarios = len(funcionarios)
    print("i. Quantos funcionários existem na empresa? Quais são as informações que constam no cadastro?")
    print(f"   Existem {num_funcionarios} funcionários na empresa.")
    print("   As informações que constam no cadastro são:")
    for key in funcionarios[0].keys():
        print(f"   - {key}")
    
    salario = []
    idade = []
    filhos = []

    for emp in funcionarios:
        if 'salario' in emp and emp['salario']:
            salario.append(float(emp['salario']))
        if 'idade' in emp and emp['idade']:
            idade.append(int(emp['idade']))
        if 'filhos' in emp and emp['filhos']:
            filhos.append(int(emp['filhos']))
        
    #Calcule média, variância, desvio padrão dos salários dos funcionários.
    print("\nii. Calcule média, variância, desvio padrão dos salários dos funcionários.")
    media_salario = statistics.mean(salario)
    variancia_salario = statistics.variance(salario)
    desv_salario = statistics.stdev(salario)
    print(f"    Média dos salários: R$ {media_salario:.2f}")
    print(f"    Variância dos salários: R$ {variancia_salario:.2f}")
    print(f"    Desvio Padrão dos salários: R$ {desv_salario:.2f}")
    
    #Que idade tem o funcionário mais jovem?
    print("\niii. Que idade tem o funcionário mais jovem?")
    mais_novo = min(idade)
    print(f"    O funcionário mais jovem tem {mais_novo} anos.")
    
    #Qual é a quantidade máxima de filhos dos funcionários?
    print("\niv. Qual é a quantidade máxima de filhos dos funcionários?")
    max_filhos = max(filhos)
    print(f"    A quantidade máxima de filhos entre os funcionários é: {max_filhos}")
    
    #Qual é a quantidade de filhos mais comum?
    print("\nv. Qual é a quantidade de filhos mais comum?")
    comum_filhos = statistics.mode(filhos)
    print(f"    A quantidade de filhos mais comum entre os funcionários é: {comum_filhos}")     

dados_sobre_funcionarios('funcionarios.csv')
