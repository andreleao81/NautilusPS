# Lista de Entregaveis Python Básico
# André Leão, Engenharia Eletrônica e de Computação

# Questão 1

def pa_or_pg(ratio):
    num = 2
    maximum = 50
    result = list()

    while num <= maximum:
        result += [num]
        num = num + ratio if ratio % 2 == 0 else num * ratio
    return result

print(pa_or_pg(2))



# Questao 2

def bitCounter(integer):
    # non negative integer
    # converte inteiro para o binario (str)
    # '0b+binario'
    binary = bin (integer) 
    result = sum([1 for i in binary if i == '1'])
    return result



# Questao 3

def ways(amount = 200, maximum = 200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return sum(ways(amount - coin, coin) for coin in coins if coin <= maximum if amount - coin >= 0)


# Questao 4

# series = 11 + 22 + 33 + ... + 1010 = 10405071317
# last 10 digits of the series, 1**2 + 2**2 + 3**2 + ... + 1000**2

def lastTen():
    # soma elementos da lista cujos elementos
    # sao todos os quadrados ate 1000
    soma = sum ([i**i for i in range(1,1001)])
    return str(soma)[-10:]






