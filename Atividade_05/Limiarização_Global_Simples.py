from PIL import Image, ImageOps
import numpy as np

nome_imagem = input('Digite o nome da imagem que deseja fazer a Limiarização Global Simples: ')
nome_formatado = nome_imagem.split('.')[0]

imagemRgb = Image.open(f'rgb-imagens/{nome_imagem}')
imagemRgb = ImageOps.exif_transpose(imagemRgb)
imagem = ImageOps.grayscale(imagemRgb)

arrayImagem = np.asarray(imagem)
arraySimples = np.zeros((imagem.height, imagem.width), dtype = np.uint8)

contador_valor_pixel = 0 

for linha_imagem in arrayImagem:
    for pixel in linha_imagem:
        contador_valor_pixel += pixel
    
limiar_geral = int(contador_valor_pixel / arrayImagem.size)

while (True):
    for i in range(imagem.height):
        for j in range(imagem.width):
                if(int(arrayImagem[i][j]) < limiar_geral):
                    arraySimples[i][j] = 0
                if(int(arrayImagem[i][j]) >= limiar_geral):
                    arraySimples[i][j] = 255

    contador_grupo1 = 0
    contador_grupo2 = 0
    qtd_grupo1 = 0
    qtd_grupo2 = 0
    
    for i in range(imagem.height):
        for j in range(imagem.width):
                if(arraySimples[i][j] == 0):
                    contador_grupo1 += int(arrayImagem[i][j])
                    qtd_grupo1 += 1
                if(arraySimples[i][j] == 255):
                    contador_grupo2 += int(arrayImagem[i][j])
                    qtd_grupo2 += 1

    media_intensidade_grupo1 = int(contador_grupo1 / qtd_grupo1)
    media_intensidade_grupo2 = int(contador_grupo2 / qtd_grupo2)
    media_intensidades = int((media_intensidade_grupo1 + media_intensidade_grupo2) / 2)

    if(int(limiar_geral) == int(media_intensidades)):
        break;
    else:
        limiar_geral = media_intensidades

imagem_limiarizacao_global_simples = Image.fromarray(arraySimples, mode='L')
imagem_limiarizacao_global_simples.save(f'imagem_limiarizacao_global_simples/{nome_formatado}.jpg', format='JPEG')
imagem_limiarizacao_global_simples.show()
print(f"Limiarização Global Simples realiado na imagem:",nome_imagem)