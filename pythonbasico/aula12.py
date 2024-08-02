#requisicoes web
import requests
import bs4 # Beautiful soup 4

texto = None
cabecalho = {'User-agent':'Windows 88','Referer':'onde e que eu to, sera que eu to na lagoinha',
             'Server-name':'Jubileu','HTTP-CF-IPCOUNTRY':'US'}

meus_cookies = {'Ultima-Visita':'10-10-2020'}
dados = {'usename':'kitt','password':'kitt123'}

try:
    requisicao = requests.post('https://putsreq.com/vtQKnrTaeRFKeyNdrFoa',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as erro:
    print('requisicao deu erro:', erro)

print(texto)