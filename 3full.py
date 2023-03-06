import os
import re

import shutil

# aniversário
aniversario = "aniversario"

# contador de pasta
contador = 341

# caminho da pasta de origem
pasta_origem = "/home/tg/Documentos/arte/v1semtitulodinamico"

# prefixo do nome da pasta de destino
prefixo = "whatsapp"

# lista de extensões de imagem válidas
extensoes = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

# condicionais para definir sufixo do nome da pasta de destino
sufixo = ""
if "forte" in pasta_origem:
    sufixo += "frt"
if "fraco" in pasta_origem:
    sufixo += "frc"
if "matriz" in pasta_origem:
    sufixo += "mtz"

# verificação de cores para adicionar sufixos
cores = {"preto": "pr", "amarelo": "am", "vermelho": "vm", "cinza": "cz", "laranja": "lj", "roxo": "rx", "azul": "az", "verde": "vd", "rosa": "ro", "verde água": "va", "lilas": "li", "branco": "bc"}

# caminho da pasta de destino
contador_str = str(contador).zfill(6)
sufixo_cores = ""
for cor, sufixo_cor in cores.items():
    if cor in pasta_origem:
        sufixo_cores += sufixo_cor
pasta_destino = f"{contador_str}-{prefixo}{sufixo}{sufixo_cores}-{aniversario}"
caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

# cria pasta de destino
os.makedirs(caminho_pasta_destino)

# deveria ordenar por 2 atributos, primeiro pelo nome do arquivo sem número, e depois pelo número no final
def ordena:
    result = re.findall('\d+');
    numero = result[len(result) - 1]
    return (nome_arquivo_sem_numero, numero)

arquivos = sorted(os.listdir(pasta_origem), key=lambda x: ordena(x))
# agrupa as imagens de 2 em 2, ordenando pelo número no final do nome

for i in range(0, len(arquivos), 2):
    # verifica se ambos os arquivos são imagens
    if os.path.isfile(os.path.join(pasta_origem, arquivos[i])) and os.path.splitext(arquivos[i])[1].lower() in extensoes and \
       os.path.isfile(os.path.join(pasta_origem, arquivos[i+1])) and os.path.splitext(arquivos[i+1])[1].lower() in extensoes:
        # incrementa o contador
        contador += 1
        
        # atualiza o nome da pasta de destino com o novo contador
        contador_str = str(contador).zfill(6)
        pasta_destino = f"{contador_str}-{prefixo}{sufixo}{sufixo_cores}-{aniversario}"
        caminho_pasta_destino = os.path.join
# constrói o caminho completo para a pasta de destino
caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

# cria pasta de destino
os.makedirs(caminho_pasta_destino)

# agrupa as imagens de 2 em 2, ordenando pelo número no final do nome
arquivos = sorted(os.listdir(pasta_origem), key=lambda x: int(os.path.splitext(x)[0][-3:]))
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
    
    # constrói o caminho completo para a nova pasta de destino
    caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)
    
    # cria pasta de destino
    os.makedirs(caminho_pasta_destino)
