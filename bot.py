import os
import shutil

# aniversário
aniversario = "aniversario"

# contador de pasta
contador = 341

# caminho da pasta de origem
pasta_origem = "/home/suportenaserra/Documentos/template5aniverv1"

# prefixo do nome da pasta de destino
prefixo = "whatsapp"

# lista de extensões de imagem válidas
extensoes = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

# condicionais para definir sufixo do nome da pasta de destino
sufixo = ""
if "forte" in pasta_origem:
    sufixo = "-frt"
elif "fraco" in pasta_origem:
    sufixo = "-frc"
elif "matriz" in pasta_origem:
    sufixo = "-mtz"
else:
    sufixo = "-mtz"

# caminho da pasta de destino
contador_str = str(contador).zfill(6)
pasta_destino = f"{contador_str}-{prefixo}{sufixo}-{aniversario}"
caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

# cria pasta de destino
os.makedirs(caminho_pasta_destino)

# lista todos os arquivos dentro da pasta de origem
arquivos = os.listdir(pasta_origem)

# agrupa as imagens de 2 em 2
for i in range(0, len(arquivos), 2):
    # verifica se ambos os arquivos são imagens
    if os.path.isfile(os.path.join(pasta_origem, arquivos[i])) and os.path.splitext(arquivos[i])[1].lower() in extensoes and \
       os.path.isfile(os.path.join(pasta_origem, arquivos[i+1])) and os.path.splitext(arquivos[i+1])[1].lower() in extensoes:
        # constrói o caminho completo para o arquivo de origem 1
        caminho_arquivo_origem_1 = os.path.join(pasta_origem, arquivos[i])

        # constrói o caminho completo para o arquivo de origem 2
        caminho_arquivo_origem_2 = os.path.join(pasta_origem, arquivos[i+1])

        # constrói o caminho completo para a pasta de destino
        caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

        # move os arquivos para a pasta de destino
        shutil.move(caminho_arquivo_origem_1, caminho_pasta_destino)
        shutil.move(caminho_arquivo_origem_2, caminho_pasta_destino)

        # incrementa o contador
        contador += 1

        # atualiza o nome da pasta de destino com o novo contador
        contador_str = str(contador).zfill(6)
        pasta_destino = f"{contador_str}-{prefixo}{sufixo}-{aniversario}"
        caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

        # cria pasta de destino
        os.makedirs(caminho_pasta_destino)
