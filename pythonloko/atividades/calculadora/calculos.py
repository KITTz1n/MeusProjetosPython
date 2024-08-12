from colorama import Fore#serve para colorir algumas strings

class Calculos:#classe chamada Calculos
    
    def __init__(self):#funcao init para quando chamar
        pass

    def pergunta():
        try:
            num = float(input('\tEscreva algum numero: '))
            return num
        except:
            pass

    def soma(v1,v2):
        try:
            resp = v1+v2
            return resp
        except:
            return '0'
        
    def subtracao(v1,v2):
        try:
            resp = v1-v2
            return resp
        except:
            return '0'
        
    def multiplicacao(v1,v2):
        try:
            resp = v1*v2
            return resp
        except:
            return '0'
        
    def divisao(v1,v2):
        try:
            resp = v1/v2
            return resp
        except ZeroDivisionError:
            print(f'\n\t{Fore.BLUE}Opss erro! Divisao por 0{Fore.RESET}')
            return '0'
        except:
            return 'Error!'