from PIL import Image, ImageOps
import numpy as np

nome_imagem = input('Digite o nome da imagem que deseja converter para CMYk: ')
nome_formatado = nome_imagem.split('.')[0]

imagemRgb = Image.open(f'rgb-imagens/{nome_imagem}')
imagemRgb = ImageOps.exif_transpose(imagemRgb)

arrayRgb = np.asarray(imagemRgb)
#print(arrayRgb.shape)
#print(arrayRgb.size)
#print(arrayRgb.ndim)
#print(imagemRgb.height)
#print(imagemRgb.width)

arrayCmyk = np.zeros((imagemRgb.height, imagemRgb.width, 4), dtype = np.uint8)
#print(arrayCmyk)
#print(arrayCmyk.shape)
#print(arrayCmyk.size)
#print(arrayCmyk.ndim)
arrayC = np.zeros((imagemRgb.height, imagemRgb.width, 4), dtype = np.uint8)
arrayM = np.zeros((imagemRgb.height, imagemRgb.width, 4), dtype = np.uint8)
arrayY = np.zeros((imagemRgb.height, imagemRgb.width, 4), dtype = np.uint8)
arrayK = np.zeros((imagemRgb.height, imagemRgb.width, 4), dtype = np.uint8)

#contador_linha = 0
#linhaXcoluna = 0

i = 0
j = 0

for linha_imagem in arrayRgb:

    #contador_linha = contador_linha + 1 

    for pixel in linha_imagem:

        #linhaXcoluna = linhaXcoluna + 1

        r = 1 - pixel[0] / 255
        g = 1 - pixel[1] / 255
        b = 1 - pixel[2] / 255

        k = min(r, g, b)

        if k != 1:
            c = (r - k) / (1 - k)
            m = (g - k) / (1 - k)
            y = (b - k) / (1 - k)

        else:
            c = 0
            m = 0
            y = 0

        # Imagem completa - CMYK
        arrayCmyk[i][j][0] = c * 255
        arrayCmyk[i][j][1] = m * 255
        arrayCmyk[i][j][2] = y * 255
        arrayCmyk[i][j][3] = k * 255

        # Camada de Ciano
        arrayC[i][j][0] = c * 255

        # Camada de Magenta
        arrayM[i][j][1] = m * 255

        # Camada de Amarelo
        arrayY[i][j][2] = y * 255

        # Camada de Preto
        arrayK[i][j][3] = k * 255

        j += 1

    j = 0
    i += 1

#print(contador_linha)
#print(linhaXcoluna)

imgemCmyk = Image.fromarray(arrayCmyk, mode='CMYK')
imgemCmyk.save(f'conversao-cmyk-images/{nome_formatado}.jpg', format='JPEG')
imgemCmyk.show()

imgemC = Image.fromarray(arrayC, mode='CMYK')
imgemC.save(f'conversao-cmyk-images/{nome_formatado}_C.jpg', format='JPEG')
imgemC.show()

imgemM = Image.fromarray(arrayM, mode='CMYK')
imgemM.save(f'conversao-cmyk-images/{nome_formatado}_M.jpg', format='JPEG')
imgemM.show()

imgemY = Image.fromarray(arrayY, mode='CMYK')
imgemY.save(f'conversao-cmyk-images/{nome_formatado}_Y.jpg', format='JPEG')
imgemY.show()

imgemK = Image.fromarray(arrayK, mode='CMYK')
imgemK.save(f'conversao-cmyk-images/{nome_formatado}_K.jpg', format='JPEG')
imgemK.show()

print("Conversão para CMYK realizada!.")