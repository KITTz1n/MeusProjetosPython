#exprecoes regulares
import re

'''
email@dominio.com.br
00 00000 0000
000.000.000.000
'''

texto = 'os gatos sao bonitos'
texto2 = 'o gato, a gata, os gatinhos'
texto3 = 'o gato, a gata, os gatinhos, as gat'
lista_gmail = [' ']

padrao = re.search(r'gat\w',texto) #Raw string
#Econtra uma palavra de um frase comparando com o valor que vc inseriu em sua funcao
padrao2 = re.findall(r'gat\w+',texto2)#combinando o 'W'e o'+' ele achara palavras
# que nesse caso comecam com gat e o resto exemplo: gatoes, nao resumindo apenas em 4 letras
padrao3 = re.findall(r'gat\w*',texto3)#combinando o 'W'e o'*' ele achara palavras
# que nesse caso comecar com gat ou seja apenas gat, exemplo: gat e gatoes

padrao_gmail = re.findall(r'[\w\.-]+@+[\w-]+\.[\w+\.]+',lista_gmail)

if padrao:
    print(padrao.group())
    print(padrao2)
    print(padrao3)
    print(padrao_gmail)
else:
    print("Padrao nao encontrado")