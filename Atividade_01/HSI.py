from tkinter import N
from PIL import Image, ImageOps
import numpy as np

nomeImagem = input('Digite o nome da imagem que deseja converter para HSI: ')
nome_formatado = nomeImagem.split('.')[0]

imagemRgb = Image.open(f'rgb-imagens/{nomeImagem}')
imagemRgb = ImageOps.exif_transpose(imagemRgb)

arrayRgb = np.asarray(imagemRgb)

arrayHsi = np.zeros((imagemRgb.height, imagemRgb.width, 3), dtype = np.uint8)
arrayH = np.zeros((imagemRgb.height, imagemRgb.width, 3), dtype = np.uint8)
arrayS = np.zeros((imagemRgb.height, imagemRgb.width, 3), dtype = np.uint8)
arrayI = np.zeros((imagemRgb.height, imagemRgb.width, 3), dtype = np.uint8)

i = 0
j = 0

for linha_imagem in arrayRgb:
    for pixel in linha_imagem:

        r = pixel[0] / 255
        g = pixel[1] / 255
        b = pixel[2] / 255
        
        # Cálculo da Matriz
        numerador = [(1/2) * ((r - g) + (r - b))]
        denominador = ((r - g) ** 2 + (r - b) * (g - b)) ** 0.5
        teta = np.degrees(np.arccos(numerador / (denominador +  0.0000000001)))

        if b <= g:
            matriz = teta
        else:
            matriz = 360 - teta

        #Cálculo da saturação
        if r + g + b == 0:
            divisao_saturacao = 1
        else:
            divisao_saturacao = 3 / (r + g + b)

        saturacao = 1 - divisao_saturacao * min(r, g, b)

        # cálculo da Intensidade
        intensidade = (r + g + b) / 3

        arrayHsi[i][j][0] = (matriz / 360) * 255
        arrayHsi[i][j][1] = saturacao * 255
        arrayHsi[i][j][2] = intensidade * 255

    
        arrayH[i][j] = (matriz / 360) * 255
        arrayS[i][j] = saturacao * 255
        arrayI[i][j] = intensidade * 255

        j += 1
    
    j = 0
    i += 1

imgemHsi = Image.fromarray(arrayHsi, mode='HSV')
#imgemHsi.save(f'conversao-hsi-images/{nome_formatado}.jpg', format='JPEG')
imgemHsi.show()

imgemH = Image.fromarray(arrayH, mode='HSV')
#imgemH.save(f'conversao-hsi-images/{nome_formatado}_H.jpg', format='JPEG')
imgemH.show()

imgemS = Image.fromarray(arrayS, mode='HSV')
#imgemS.save(f'conversao-hsi-images/{nome_formatado}_S.jpg', format='JPEG')
imgemS.show()

imgemI = Image.fromarray(arrayI, mode='HSV')
#imgemI.save(f'conversao-hsi-images/{nome_formatado}_I.jpg', format='JPEG')
imgemI.show()

print("Conversão para HSI realizada!.")