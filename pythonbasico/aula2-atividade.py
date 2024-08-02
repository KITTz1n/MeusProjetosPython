'''
EXERCICIO: faca um formulario que pergunte o nome, cpf, endereco, idade, altura e telefone
e imprima isso em um relatorio organizado
'''

print('\tFormulario') # Titulo

# Variaveis
nome = input('Escreva seu nome: ')
cpf = input('Escreva seu cpf: ')
endereco = input('Escreva seu endereco: ')
idade = input('Escreva sua idade: ')
altura = input('Escreva sua altura: ')
telefone = input('Escreva seu telefone: ')

print('\n\n\tFormulario Completo') # Titulo

print('\nSeu nome:',nome,
      '\nSeu cpf:',cpf,
      '\nSeu endereco:',endereco,
      '\nSua idade:',idade,
      '\nSua altura:',altura,
      '\nSeu telefone:',telefone)

print('\n\tMuito Obrigado!\nDados Registrados Com Sucesso')