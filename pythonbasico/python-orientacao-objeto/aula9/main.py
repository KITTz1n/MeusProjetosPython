from veiculo import Veiculo
from carro import Carro

caminhao_azul = Veiculo('azul',8,'ford',10,70)
carro_cinza = Carro('cinza','Ferrari',30,40)

def caminhao():
      print('\nCaminhao Azul')

      print('Caminhao:',caminhao_azul,'\nTipo:',type(caminhao_azul))
      print('\n\tCaracteristicas:','\nCor:',caminhao_azul.cor,'\nQuantidade de rodas:',caminhao_azul.rodas
            ,'\nMarca:',caminhao_azul.marca,'\nQuantidade de Litros Atual:',caminhao_azul.tanque,
            '\nQuantidade de Litros Maxima:',caminhao_azul.quant_litro_max)

def carro():
      print('\n\tCarro Cinza')

      print('\nCarro:',carro_cinza,'\nTipo:',type(carro_cinza))
      print('\n\tCaracteristicas','\nCor:',carro_cinza.cor,'\nQuantidade de rodas:',carro_cinza.rodas
            ,'\nMarca:',carro_cinza.marca,'\nQuantidade de Litros Atual:',carro_cinza.tanque,
            '\nQuantidade de Litros Maxima:',carro_cinza.quant_litro_max)

escolha = input('Escolha um caminhao ou um carro: ')

if escolha == 'carro':
      carro()
elif escolha == 'caminhao':
      caminhao()
else:
      print('Erro nao temos essa opcao')

print('\n1-Abastecer\n2-Andar\n3-Nada')

def fazer():
      oq_fazer = input('\nOque ira fazer?\n')

      if oq_fazer == 'abastecer':
            quant_abastecer = float(input('Qual a quantidade de litros?\n'))
            if escolha == 'carro':
                  carro_cinza.abastecer(quant_abastecer)
                  print('Quantidade de Litros Atual:',carro_cinza.tanque)
                  print('Quantia que excedeu:',carro_cinza.excedeu)
            if escolha == 'caminhao':
                  caminhao_azul.abastecer(quant_abastecer)
                  print('Quantidade de Litros Atual:',caminhao_azul.tanque)
                  print('Quantia que excedeu:',caminhao_azul.excedeu)
      elif oq_fazer == 'andar':
            quant_andar = float(input('Quantos Km ira rodar com o veiculo?: '))
            if escolha == 'carro':
                  carro_cinza.andar(quant_andar,0.1)
                  print('Quantia gasta:',carro_cinza.quant_gasto)
                  print('Quantidade de Litros Atual:',carro_cinza.tanque)
            if escolha == 'caminhao':
                  caminhao_azul.andar(quant_andar,0.15)
                  print('Quantia gasta:',caminhao_azul.quant_gasto)
                  print('Quantidade de Litros Atual:',caminhao_azul.tanque)
      elif oq_fazer == 'ver combustivel':
            if escolha == 'carro':
                  print('\nQuantidade de Litros Atual:', carro_cinza.tanque,
                        '\nQuantidade de Litros Maxima:', carro_cinza.quant_litro_max)
            if escolha == 'caminhao':
                  print('\nQuantidade de Litros Atual:', caminhao_azul.tanque,
                        '\nQuantidade de Litros Maxima:', caminhao_azul.quant_litro_max)
      elif oq_fazer == 'nada':
            print('okay')
      else:
            print('ERRO! nao temos essa opcao')
      if (oq_fazer == 'ver combustivel' or oq_fazer == 'andar') or (oq_fazer == 'abastecer'):
            fazer()


fazer()