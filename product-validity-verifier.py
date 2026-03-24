# Input que pede o dia atual
actual_day = int(input("Digite o dia do mês atual: "))
# Input que pede o dia de expiração
expired_day = int(input("Agora digite o dia de vencimento do produto: "))

# Definição da variável de categoria do produto
product_category = ""

# Condicional para checar se o produto venceu
if expired_day <= actual_day:
    product_category = "descartado"

# Condicional para checar se o produto está perto de vencer(valor arbitrário definido como 5)
elif (expired_day - actual_day) <= 5:
    product_category = "Promoção Relâmpago"

# Caso nenhuma condição seja atendida, o else é chamado
else:
    product_category = "comum"

# Resposta ao usuário sobre a categoria do produto
print(f"O produto deve ir para a prateleira: {product_category}")
