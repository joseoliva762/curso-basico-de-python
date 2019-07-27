pares = list()
for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)
print('normal: {}'.format(pares))

#List comprenhention
even = [num for num in range(1, 31) if num%2 == 0]
print('list comprenhention: {}'.format(even))

##Dictionary
cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num**2
print('Normal: {}'.format(cuadrados))

# Dictionary comprenhention
squere = {num: num**2 for num in range(1, 11)}
print('Dictionay comprenhention: {}'.format(squere))
