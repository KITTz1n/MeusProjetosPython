from PIL import Image

#entrada e saida de arquivos

escrever = open('escrita.txt','w')#cria o arquivo.txt
ler = open('leitura.txt','r')#le o arquivo.txt
imagem = open('imagens/kitt.png', 'rb')#le imagens

imagem_pil = Image.open('imagens/kitt.png')#aprendi fora do curso a usar essa lib

print(type(escrever))
print(escrever)

for i in range(0,101):
    escrever.write(f'{i}\n')
for i in ler:
    print(i)

print(imagem.read())
imagem_pil.show()