import os
import shutil

# pasta que será organizada
pasta = "arquivos"

# categorias de arquivos
categorias = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov"],
    "Compactados": [".zip", ".rar"]
}

# criar pasta principal se não existir
if not os.path.exists(pasta):
    os.mkdir(pasta)

for arquivo in os.listdir(pasta):

    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):

        extensao = os.path.splitext(arquivo)[1].lower()

        for categoria, extensoes in categorias.items():

            if extensao in extensoes:

                pasta_destino = os.path.join(pasta, categoria)

                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)

                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))

                print(f"{arquivo} movido para {categoria}")
