import os
from PIL import Image

# diretório das imagens
diretorio ="/home/tg/Documentos/v2comtitulodinamico"


# limite de tamanho em pixels para as imagens menores
limite_tamanho = 140

# loop para renomear as imagens
contador = 1
for arquivo in os.listdir(diretorio):
    caminho_arquivo = os.path.join(diretorio, arquivo)
    
    # verifica se o arquivo é uma imagem
    if os.path.isfile(caminho_arquivo) and imghdr.what(caminho_arquivo):
        # abre a imagem com a biblioteca Pillow
        imagem = Image.open(caminho_arquivo)
        
        # obtém as dimensões da imagem
        largura, altura = imagem.size
        
        # verifica se a imagem é maior que o limite definido
        if largura > limite_tamanho and altura > limite_tamanho:
            # renomeia a imagem com o prefixo "thumb"
            novo_nome = f"thumb{contador}.png"
            os.rename(caminho_arquivo, os.path.join(diretorio, novo_nome))
            contador += 1
        else:
            # renomeia a imagem com o sufixo "fundo"
            nome, extensao = os.path.splitext(arquivo)
            novo_nome = f"{nome}-fundo{extensao}"
            os.rename(caminho_arquivo, os.path.join(diretorio, novo_nome))
