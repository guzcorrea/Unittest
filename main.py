from calculadora import soma

# print(soma(10,20))
# print(soma(-10,20))
# print(soma(-10.5,20.5))
print(soma('15',15))

try:
    print(soma('15',15))
except TypeError as e:
    print(f'Conta inexistente {e}')

print('Conta', soma(25,25))