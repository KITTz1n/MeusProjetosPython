#Estruturas de dados

lista = ['Macarrao','Tomate'] #Lista (list) / dinamica e coordenada
tupla = ('Macarrao','Tomate') #Tupla (tuple) / nao e dinamica / numero definido de coisas
dicionario = {'nome':'Wellington','idade':'15 anos'} #Dicionario (dict)
conjunto = {'Wellington','15 anos'} #Conjunto (set) / nao tem indice dentro dele

print('\n\tTupla')

for i in tupla:
    print(i)
if 'Macarrao' in tupla:
    print('Macarrao esta na tupla')

#para substituir tupla tem que subtistui-la inteira / mas normalmente nao e
                                                    # mt utilizado a mudanca de tupla.

print('\n\tDicionario')

print(dicionario['nome'])#especifica a chave no dicionario
print(dicionario['idade'])
print(len(dicionario))#duas pois cata o tamanho de indices/chaves

if 'Wellington' in dicionario.values(): #procura se wellington esta dentro do dicionario
    print('Wellington esta no dicionario')
for valores in dicionario.values(): #mostra os valores das chaves no dicionario
    print(valores)

dicionario['nome'] = 'Wendel' #posso modificar os valores
dicionario['idade'] = '20 anos'
print(dicionario['nome'])
print(dicionario['idade'])

dicionario['data de nascimento'] = '20/12/2003' #posso adicionar chaves e valores
print(dicionario['data de nascimento'])

print('\n\tConjunto')

conjunto.add('26/05/2009')#posso adicionar coisas ao conjunto
conjunto.add('Wellington')#junta todos os iguais

if 'Wellington' in conjunto:#conjunto usa uma tabela hash sendo mais facil e rapido de
                            #econtrar itens dentro dele.
    print('Wellington foi encontrado dentro do conjunto')

conjunto.remove('26/05/2009')

print(conjunto)

#COMO INICIALIZAR VAZIO

minha_lista = []
minha_tupla = ()
meu_dicionario = {}
meu_conjunto = set()

#possibilidades
print('\n\tLoucura')
loucura = [(1,2),(3,4),(5,6),({'A','B'},{'C'})]
print(loucura)