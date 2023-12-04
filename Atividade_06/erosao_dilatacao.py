from PIL import Image, ImageOps
import numpy as np

nome_imagem = input('Digite o nome da imagem que deseja fazer a Erosão e a Dilatação: ')
nome_formatado = nome_imagem.split('.')[0]

elemento_estruturante = np.array([(0,0,0),(255,255,255),(0,255,0)])
elemento_estruturante_contador = 0

for i in range(3):
    for j in range(3):
        if elemento_estruturante[i][j] == 255:
            elemento_estruturante_contador = elemento_estruturante_contador +1

imagemRgb = Image.open(f'rgb-imagens/{nome_imagem}')
imagemRgb = ImageOps.exif_transpose(imagemRgb)
imagem = ImageOps.grayscale(imagemRgb)

arrayImagem = np.asarray(imagem)
arrayBinarioDilatacao = np.zeros((imagem.height, imagem.width), dtype = np.uint8)
arrayDilatacao = np.zeros((imagem.height, imagem.width), dtype = np.uint8)
arrayErosao = np.zeros((imagem.height, imagem.width), dtype = np.uint8)

for i in range(imagem.height):
    for j in range(imagem.width):
            if(int(arrayImagem[i][j]) < 127):
                arrayBinarioDilatacao[i][j] = 255
            if(int(arrayImagem[i][j]) >= 127):
                arrayBinarioDilatacao[i][j] = 0


for i in range(imagem.height):
    for j in range(imagem.width):
        posicao_pixel = 0
        elemento_estruturante_dentro_imagem = 0
        for posicao_pixel in range(9):
            auxI = i
            auxJ = j

            if(i<=0 or j<=0 or i>=imagem.height-1 or j>=imagem.width-1):
                borda = True
            else:
                if(arrayBinarioDilatacao[auxI, auxJ] == 255):
                    if(posicao_pixel == 0):
                        auxI = auxI -1
                        auxJ = auxJ -1
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[0][0]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[0][0]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 1):
                        auxI = auxI -1
                        auxJ= auxJ
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[1][0]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[1][0]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 2):
                        auxI = auxI -1
                        auxJ= auxJ +1
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ] 
                        if(valor_pixel_atual != elemento_estruturante[2][0]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[2][0]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 3):
                        auxI = auxI
                        auxJ = auxJ +1
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[2][1]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[2][1]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 4):
                        auxI = auxI +1
                        auxJ = auxJ +1
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[2][2]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[2][2]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 5):
                        auxI = auxI +1
                        auxJ= auxJ 
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[1][2]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[1][2]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 6):
                        auxI = auxI +1
                        auxJ= auxJ -1
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[0][2]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[0][2]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 7):
                        auxI = auxI
                        auxJ= auxJ -1
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual != elemento_estruturante[0][1]):
                            arrayDilatacao[auxI, auxJ] = 255
                        if(valor_pixel_atual == elemento_estruturante[0][1]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                    if(posicao_pixel == 8):
                        auxI = auxI
                        auxJ= auxJ
                        valor_pixel_atual = arrayBinarioDilatacao[auxI, auxJ]
                        if(valor_pixel_atual == elemento_estruturante[1][1]):
                            elemento_estruturante_dentro_imagem = elemento_estruturante_dentro_imagem + 1
                else:
                    elemEstruturante = False
        if(elemento_estruturante_contador == elemento_estruturante_dentro_imagem):
            arrayErosao[i][j] = 255
                   
imagem_binaria = Image.fromarray(arrayBinarioDilatacao, mode='L')
imagem_binaria.save(f'imagem_binaria/{nome_formatado}.jpg', format='JPEG')
imagem_binaria.show()

imagem_dilatacao = Image.fromarray(arrayDilatacao, mode='L')
imagem_dilatacao.save(f'dilatacao/{nome_formatado}.jpg', format='JPEG')
imagem_dilatacao.show()

imagem_erosao = Image.fromarray(arrayErosao, mode='L')
imagem_erosao.save(f'erosao/{nome_formatado}.jpg', format='JPEG')
imagem_erosao.show()

