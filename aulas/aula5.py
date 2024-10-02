#Estruturas de laco
ingredientes = ['Macarrao', 'Massa de Tomate', 'Alho', 'Oleo']
lista_ingre_catado = []
lista_de_numeros = range(0, 10, 2)# range comecando no 0 indo ate o 10 de 2 em 2
numeros_de_ingredientes = range(1,len(ingredientes)+1)
palavra = 'Eu sabo! '
valor = 0
contador = 0
numero = 0
i = 0

for x in ingredientes:
    contador += 1
    print('Catado ingrediente:',x)
    lista_ingre_catado.append(x)
    if len(lista_ingre_catado) == len(ingredientes):
        print('Lista de ingredientes catados:',lista_ingre_catado)

for item in lista_de_numeros:
    print('Lista de numeros: ',item)

for numero in numeros_de_ingredientes:
    print(numero)

for letra in palavra:
    print(letra)

while valor < 10:
    print('Valor e menor do que 10: ',valor)
    valor += 1
print('Acabou o while, Valor ficou igual a:',valor)
print('Tem:',contador,'ingredientes.')
