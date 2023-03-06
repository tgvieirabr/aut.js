import os
import shutil

# aniversário
aniversario = "aniversario"

# contador de pasta
contador = 340

# caminho da pasta de origem
pasta_origem = "/home/tg/teste"
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

# agrupa as imagens de 2 em 2, na ordem atual dos arquivos
print(os.listdir(pasta_origem))
print("\n")
print(sorted(os.listdir(pasta_origem)))

