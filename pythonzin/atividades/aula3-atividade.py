'''EXERCICIO: faca um programa que pergunte a idade o peso e a altura
de uma pessoa e decide se ela esta apta a ser do exercito para entrar tem que ter
mais de 18 anos pesar mais de ou igual a 60 kilos e medir mais ou igual a 1,70'''
print('\tTeste Exercito')

#variaveis
idade = int(input('Escreva sua idade: '))
peso = int(input('Escreva seu peso: '))
altura = float(input('Escreva sua altura: '))

idade_correta = 18
peso_correto = 60
altura_correta = 1.70

if (idade>=idade_correta and peso>=peso_correto) and (altura>=altura_correta):
# acho que so pode um and fora de parenteses no caso de if
    print('\nIdade sua: ',idade,'\nPeso seu: ',peso,'\nAltura sua: ',altura)
    print('\nIdade Minima: ',idade_correta,'\nPeso Minimo: ',peso_correto,'\nAltura Minima: ',altura_correta)
    print('\n\tResultado:','Parabens voce foi aprovado!')
else:
    print('\nIdade sua: ', idade, '\nPeso seu: ', peso, '\nAltura sua: ', altura)
    print('\nIdade Minima: ', idade_correta, '\nPeso Minimo: ', peso_correto, '\nAltura Minima: ', altura_correta)
    print('\n\tResultado:','Reprovado')