#strings e listas

frase = 'Eu gosto de jogos!'
lista = ['Abacaxi','Alface','Batata','Beterraba']
lista.append('Uva')
lista.remove('Beterraba')
#lista.clear()
lista.insert(1,'Amora')
lista[0]= 'Couve Flor'
contador_Amora = lista.count('Amora')
frase_separada = frase.split(' ')#separa a frase, catando de espaco em espaco
frase_nova = frase + ' para passar tempo!'

print(frase_separada[0])#imprime a frase separadamente
print(frase.lower())#deixa a frase em minusculo nessa linha
print(frase[0])#quebra de frase
print(frase[0:10])#quebra de 0 ate a letra 10
print(frase[0:10:2])#quebra de 0 ate a letra ate a 5 pois 10:2 e 5
print(frase)
print(frase_nova)
print('Numero de letras da frase:',len(frase))
print(lista)
print(lista[0])#quebra de lista
print('Tipo da frase:',type(frase))
print('Tipo da lista:',type(lista))
print(lista[-1])#comeca de tras para frente
print('Contador de Amoras: ',contador_Amora)
print(lista.pop())#cata o ultimo da lista mostra ele e retira ele da lista