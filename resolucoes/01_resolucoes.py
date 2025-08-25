# minhas resoluções são possíveis soluções para os exercícios propostos
# você pode ter outras soluções, o importante é que funcione!

# resolução da sessão sobre variáveis e tipos de dados
# practice time #1

# Exemplo de aplicação dos tipos de dados em um contexto contábil
# print("Exemplos de tipos de dados em contabilidade: \n")
# print("Practice time #1\n")
# # int: Representando a quantidade de notas fiscais emitidas no mês.
# quantidade_notas = 150
# print(f"Dado: {quantidade_notas}, Tipo: {type(quantidade_notas)}")

# # float: Representando o valor de um imposto a pagar.
# valor_imposto_pis = 1250.75
# print(f"Dado: {valor_imposto_pis}, Tipo: {type(valor_imposto_pis)}")

# # bool: Indicando se uma empresa é optante pelo Simples Nacional.
# optante_simples = False
# print(f"Dado: {optante_simples}, Tipo: {type(optante_simples)}")

# # str: Armazenando a razão social de um cliente.
# razao_social_cliente = "Consultoria Financeira ABC Ltda"
# print(f"Dado: '{razao_social_cliente}', Tipo: {type(razao_social_cliente)}")


# practice time #2
# print("Practice time #2\n")

# # Exemplo: Cálculo de imposto de renda simplificado
# salario = float(input("Digite o salário mensal: "))

# # Operações matemáticas
# imposto = salario * 0.075  # alíquota de 7,5% (exemplo)
# salario_liquido = salario - imposto

# # Operações lógicas
# if salario < 2000:
#     print("Isento de imposto de renda.")
# else:
#     print("Imposto calculado:", imposto)
#     print("Salário líquido:", salario_liquido)


# practice time #3.1
print("Practice time #3.1\n")


total = 0  # acumulador de despesas

print("Digite o valor das despesas. Digite 0 para encerrar.")

while True:
    despesa = float(input("Informe a despesa: "))
    
    if despesa == 0:  # condição de parada
        break
    
    total += despesa  # acumula as despesas

print("Total gasto no mês: R$", total)

# practice time #3.2
print("Practice time #3.2\n")

soma_liquidos = 0  # acumulador para calcular a média

for i in range(0, 5):  # de 0 até 5
    salario_bruto = float(input(f"Digite o salário bruto do funcionário {i}: "))
    
    imposto = salario_bruto * 0.10  # 10% de imposto
    salario_liquido = salario_bruto - imposto
    
    print(f"Funcionário {i} → Salário líquido: R$ {salario_liquido:.2f}")
    
    soma_liquidos += salario_liquido  # acumula para calcular a média

media = soma_liquidos / 5
print("Média salarial líquida da empresa: R$", round(media, 2))
