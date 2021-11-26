# Python Basics list for Nautilus

# Question 1

def as_or_gs(ratio):
    num = 2
    maximum = 50
    result = list()

    while num <= maximum:
        result += [num]
        # if ratio is even, add it to number (making an arithmetic sequence)
        # if not, multiply number by it (making an geometric sequence) 
        num = num + ratio if ratio % 2 == 0 else num * ratio
    return result



# Question 2

def bitCounter(integer):
    # integer is non negative
    # converts int to bin (str)
    # 'binary' format is '0b+binario'
    binary = bin (integer) 
    result = sum([1 for i in binary if i == '1'])
    return result



# Question 3

def ways(maximum = 200, coins = (1, 2, 5, 10, 20, 50, 100, 200)):
    # compute all combinations
    # iterates all the tuple
    result = [1] + [0]*maximum
    for coin in coins:
        for i in range(coin, maximum+1):
            result[i] += result[i-coin]
    return result[maximum]


# Question 4

# series = 11 + 22 + 33 + ... + 1010 = 10405071317
# last 10 digits of the series, 1**2 + 2**2 + 3**2 + ... + 1000**2

def lastTen():
    # sum elements from list
    # list of square numbers from 1 to 1000
    soma = sum ([i**i for i in range(1,1001)])
    return str(soma)[-10:]






