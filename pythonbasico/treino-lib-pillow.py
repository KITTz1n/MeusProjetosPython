from PIL import Image

# Abrindo uma imagem
imagem = Image.open('C:\\Users\\Wendel\\PycharmProjects\\pythonbasico\\imagens\\kitt.png')

imagem_cinza = imagem.convert('L')

# Salvando a imagem em outro formato
imagem.save('C:\\Users\\Wendel\\PycharmProjects\\pythonbasico\\imagens\\kitt_comum.png')
imagem_cinza.save('C:\\Users\\Wendel\\PycharmProjects\\pythonbasico\\imagens\\kitt_cinza.png')

tamanho_thumbnail = (1920, 1080)

while True:
    imagem.show()
    imagem_cinza.show()