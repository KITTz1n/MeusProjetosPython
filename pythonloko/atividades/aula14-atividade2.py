''''
faca um programa que mostre em tempo real a previsao do tempo
'''

from clima import Clima

apikey = 'bd52c47783991ed037de97c070ea65e8'
lang = 'pt_br'

while True:
    Clima.printar(50,apikey,lang)