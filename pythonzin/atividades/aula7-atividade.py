''''
Exercicio: escreva uma funcao que recebe um objeto de colecao(uma lista,um conjunto,uma tupla)
e retorna o valor do maior numero dentro dessa colecao
faca outra funcao que retorna o menor numero dessa colecao
'''

lista = [1,2,4,5,50]
def maior():
    resp = max(lista)
    return resp
def menor():
    resp = min(lista)
    return resp

print('Maior:',maior(),'\nMenor:',menor())