#tratamento de erros
import time

try:
    a = 10 / 0
    asas()
except ZeroDivisionError:
    print('divisao por 0, tente de novo')
except NameError:
    print('voce digitou algo errado')
except Exception as erro:
    print('algum erro acoteceu, veja qual foi:',erro)

def abrir_arquivo():
    try:
        arquivo = open('C:\\Users\\Wendel\\Documents\\GitHub\\TreinoPython\\pythonloko\\arquivo.txt')
        for i in arquivo:
            if i != ' ':
                print(i)
    except Exception as erro:
        print('Nao achamos o arquivo, Erro:',erro)

while not abrir_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print('arquivo encontrado')
