from PIL import Image, ImageOps
import numpy as np

nome_imagem = input('Digite o nome da imagem que deseja fazer a Limiarização Global Ótima: ')
nome_formatado = nome_imagem.split('.')[0]

imagemRgb = Image.open(f'rgb-imagens/{nome_imagem}')
imagemRgb = ImageOps.exif_transpose(imagemRgb)
imagem = ImageOps.grayscale(imagemRgb)

arrayImagem = np.asarray(imagem)

# Histograma
histograma = np.zeros((256))

for linha_imagem in arrayImagem:
    for pixel in linha_imagem:
        histograma[pixel] += 1

#Histograma Normalizado
histograma_normalizado = np.zeros((256))

for valor in range(len(histograma)):
    histograma_normalizado[valor] = (histograma[valor] / (imagem.width * imagem.height))

variancia = np.zeros((256))
#variancia = []

maxVariancia = 1
intencidade_media_geral = 0

for(i) in range(256):
    intencidade_media_geral += i * histograma_normalizado[i]

for(limiar_geral) in range(1, 256):
    probabilidade_pixel_classe1 = 0
    numerador_classe1 = 0
    for i in range(limiar_geral):
        probabilidade_pixel_classe1 += histograma_normalizado[i]

        numerador_classe1 += i * histograma_normalizado[i]
            
    probabilidade_pixel_classe2 = 1 - probabilidade_pixel_classe1

    numerador_classe2 = 0
    for(i) in range(limiar_geral + 1, 256):
        numerador_classe2 += i * histograma_normalizado[i]

    if(probabilidade_pixel_classe1 != 0):
        intencidade_media_classe1 = (1 / probabilidade_pixel_classe1) * numerador_classe1
    else:
        intencidade_media_classe1 = numerador_classe1

    if(probabilidade_pixel_classe2 != 0):
        intencidade_media_classe2 = (1 / probabilidade_pixel_classe2) * numerador_classe2
    else:
        intencidade_media_classe2 = numerador_classe2

    variancia[limiar_geral] = (probabilidade_pixel_classe1 * (intencidade_media_classe1 - intencidade_media_geral) ** 2 + probabilidade_pixel_classe2 * (intencidade_media_classe2 - intencidade_media_geral) ** 2)
    #variancia.append(probabilidade_pixel_classe1 * (intencidade_media_classe1 - intencidade_media_geral) ** 2 + probabilidade_pixel_classe2 * (intencidade_media_classe2 - intencidade_media_geral) ** 2)
    if(maxVariancia < variancia[limiar_geral]):
        maxVariancia = variancia[limiar_geral]
        threshold = limiar_geral

#maxVariance = max(variancia)
#threshold = variancia.index(maxVariance)
    
arrayOtimo = np.zeros((imagem.height, imagem.width), dtype=np.uint8)
contador = 0
for i in range(imagem.height):
    for j in range(imagem.width):
        if arrayImagem[i, j] <= threshold:
            arrayOtimo[i, j] = 0
            contador += 1
        else:
            arrayOtimo[i, j] = 255

imagem_limiarizacao_global_otima = Image.fromarray(arrayOtimo, mode='L')
imagem_limiarizacao_global_otima.save(f'imagem_limiarizacao_global_otima/{nome_formatado}.jpg', format='JPEG')
imagem_limiarizacao_global_otima.show()
print(f"Limiarização Global Ótima realiado na imagem:",nome_imagem)