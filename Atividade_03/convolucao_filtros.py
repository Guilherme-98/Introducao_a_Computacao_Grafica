from cmath import pi
from genericpath import exists
from PIL import Image, ImageOps
import numpy as np

def filtro_media(i, j, valor_pixel_atual, posicao_pixel):
    matriz_media = np.array([(1,1,1),(1,1,1),(1,1,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_media[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_media[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_media[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_media[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_media[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_media[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_media[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_media[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_media[1, 1] * valor_pixel_atual
    

def filtro_passa_alta_norte(i, j, valor_pixel_atual, posicao_pixel):
    matriz_norte = np.array([(1,1,1),(1,-2,1),(-1,-1,-1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_norte[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_norte[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_norte[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_norte[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_norte[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_norte[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_norte[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_norte[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_norte[1, 1] * valor_pixel_atual

def filtro_passa_alta_sul(i, j, valor_pixel_atual, posicao_pixel):
    matriz_sul = np.array([(-1,-1,-1),(1,-2,1),(1,1,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_sul[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_sul[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_sul[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_sul[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_sul[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_sul[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_sul[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_sul[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_sul[1, 1] * valor_pixel_atual


def filtro_passa_alta_leste(i, j, valor_pixel_atual, posicao_pixel):
    matriz_leste = np.array([(-1,1,1),(-1,-2,1),(-1,1,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_leste[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_leste[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_leste[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_leste[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_leste[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_leste[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_leste[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_leste[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_leste[1, 1] * valor_pixel_atual


def filtro_passa_alta_oeste(i, j, valor_pixel_atual, posicao_pixel):
    matriz_oeste = np.array([(1,1,-1),(1,-2,-1),(1,1,-1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_oeste[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_oeste[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_oeste[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_oeste[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_oeste[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_oeste[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_oeste[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_oeste[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_oeste[1, 1] * valor_pixel_atual


def filtro_passa_alta_nordeste(i, j, valor_pixel_atual, posicao_pixel):
    matriz_nordeste = np.array([(1,1,1),(-1,-2,1),(-1,-1,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_nordeste[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_nordeste[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_nordeste[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_nordeste[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_nordeste[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_nordeste[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_nordeste[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_nordeste[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_nordeste[1, 1] * valor_pixel_atual


def filtro_passa_alta_noroeste(i, j, valor_pixel_atual, posicao_pixel):
    matriz_noroeste = np.array([(1,1,1),(1,-2,-1),(1,-1,-1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_noroeste[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_noroeste[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_noroeste[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_noroeste[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_noroeste[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_noroeste[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_noroeste[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_noroeste[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_noroeste[1, 1] * valor_pixel_atual


def filtro_passa_alta_sudeste(i, j, valor_pixel_atual, posicao_pixel):
    matriz_sudeste = np.array([(-1,-1,1),(-1,-2,1),(1,1,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_sudeste[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_sudeste[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_sudeste[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_sudeste[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_sudeste[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_sudeste[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_sudeste[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_sudeste[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_sudeste[1, 1] * valor_pixel_atual


def filtro_passa_alta_sudoeste(i, j, valor_pixel_atual, posicao_pixel):
    matriz_sudoeste = np.array([(1,-1,-1),(1,-2,-1),(1,1,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_sudoeste[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_sudoeste[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_sudoeste[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_sudoeste[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_sudoeste[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_sudoeste[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_sudoeste[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_sudoeste[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_sudoeste[1, 1] * valor_pixel_atual


def filtro_passa_alta_horizontais(i, j, valor_pixel_atual, posicao_pixel):
    matriz_horizontal = np.array([(-0.5,-0.5,-0.5),(1,1,1),(-0.5,-0.5,-0.5)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_horizontal[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_horizontal[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_horizontal[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_horizontal[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_horizontal[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_horizontal[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_horizontal[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_horizontal[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_horizontal[1, 1] * valor_pixel_atual


def filtro_passa_alta_verticais(i, j, valor_pixel_atual, posicao_pixel):
    matriz_vertical = np.array([(-0.5,1,-0.5),(-0.5,1,-0.5),(-0.5,1,-0.5)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_vertical[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_vertical[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_vertical[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_vertical[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_vertical[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_vertical[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_vertical[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_vertical[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_vertical[1, 1] * valor_pixel_atual


def filtro_passa_alta_mais_quarenta_cinco(i, j, valor_pixel_atual, posicao_pixel):
    matriz_mais_quarenta_cinco = np.array([(-1,-1,2),(-1,2,-1),(2,-1,-1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_mais_quarenta_cinco[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_mais_quarenta_cinco[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_mais_quarenta_cinco[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_mais_quarenta_cinco[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_mais_quarenta_cinco[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_mais_quarenta_cinco[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_mais_quarenta_cinco[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_mais_quarenta_cinco[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_mais_quarenta_cinco[1, 1] * valor_pixel_atual


def filtro_passa_alta_menos_quarenta_cinco(i, j, valor_pixel_atual, posicao_pixel):
    matriz_menos_quarenta_cinco = np.array([(2,-1,-1),(-1,2,-1),(-1,-1,2)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_menos_quarenta_cinco[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_menos_quarenta_cinco[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_menos_quarenta_cinco[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_menos_quarenta_cinco[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_menos_quarenta_cinco[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_menos_quarenta_cinco[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_menos_quarenta_cinco[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_menos_quarenta_cinco[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_menos_quarenta_cinco[1, 1] * valor_pixel_atual

def filtro_sobel_horizontal(i, j, valor_pixel_atual, posicao_pixel):
    matriz_sobel_horizontal = np.array([(-1,-2,-1),(0,0,0),(1,2,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_sobel_horizontal[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_sobel_horizontal[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_sobel_horizontal[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_sobel_horizontal[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_sobel_horizontal[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_sobel_horizontal[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_sobel_horizontal[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_sobel_horizontal[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_sobel_horizontal[1, 1] * valor_pixel_atual


def filtro_sobel_vertical(i, j, valor_pixel_atual, posicao_pixel):
    matriz_sobel_vertical = np.array([(-1,0,1),(-2,0,2),(-1,0,1)]) * (1/9) #filtro (3X3)
    if(posicao_pixel == 0):
        return matriz_sobel_vertical[0, 0] * valor_pixel_atual
    if(posicao_pixel == 1):
        return matriz_sobel_vertical[1, 0] * valor_pixel_atual
    if(posicao_pixel == 2):
        return matriz_sobel_vertical[2, 0] * valor_pixel_atual
    if(posicao_pixel == 3):
        return matriz_sobel_vertical[2, 1] * valor_pixel_atual
    if(posicao_pixel == 4):
        return matriz_sobel_vertical[2, 2] * valor_pixel_atual
    if(posicao_pixel == 5):
        return matriz_sobel_vertical[1, 2] * valor_pixel_atual
    if(posicao_pixel == 6):
        return matriz_sobel_vertical[0, 2] * valor_pixel_atual
    if(posicao_pixel == 7):
        return matriz_sobel_vertical[0, 1] * valor_pixel_atual
    if(posicao_pixel == 8):
        return matriz_sobel_vertical[1, 1] * valor_pixel_atual

def menu():
    print("\nSelecione um determinado filtro:")
    print("1 - filtro media")
    print("2 - filtro passa alta norte")
    print("3 - filtro passa alta sul")
    print("4 - filtro passa alta leste")
    print("5 - filtro passa alta oeste")
    print("6 - filtro passa alta nordeste")
    print("7 - filtro passa alta noroeste")
    print("8 - filtro passa alta sudeste")
    print("9 - filtro passa alta sudoeste")
    print("10 - filtro passa alta horizontais")
    print("11 - filtro passa alta verticais")
    print("12 - filtro passa alta +45°")
    print("13 - filtro passa alta -45°")
    print("14 - filtro sobel horizontal")
    print("15 - filtro sobel vertical")
    print("16 - filtro sobel soma horizontal e vertical")

def main():
    
    menu()
    op = int(input())

    nome_imagem = input('Digite o nome da imagem será aplicado o filtro selecionado:')
    nome_formatado = nome_imagem.split('.')[0]

    imagemRgb = Image.open(f'rgb-imagens/{nome_imagem}')
    imagemRgb = ImageOps.exif_transpose(imagemRgb)

    arrayRgb = np.asarray(imagemRgb)
    imagem_filtro = np.zeros((imagemRgb.height, imagemRgb.width, 3), dtype = np.uint8)

    altura = imagemRgb.height 
    largura = imagemRgb.width 

    # Convolução
    for i in range(altura):
        for j in range(largura):
            for k in range(3):
                pixel_somatorio = 0
                posicao_pixel = 0
                for posicao_pixel in range(9):
                    auxI = i
                    auxJ = j

                    if(i<=0 or j<=0 or i>=altura-1 or j>=largura-1):
                        borda = True
                    else:
                        if(posicao_pixel == 0):
                            auxI = auxI -1
                            auxJ = auxJ -1
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]
                        if(posicao_pixel == 1):
                            auxI = auxI -1
                            auxJ= auxJ
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]
                        if(posicao_pixel == 2):
                            auxI = auxI -1
                            auxJ= auxJ +1
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k] 
                        if(posicao_pixel == 3):
                            auxI = auxI
                            auxJ = auxJ +1
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]
                        if(posicao_pixel == 4):
                            auxI = auxI +1
                            auxJ = auxJ +1
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]
                        if(posicao_pixel == 5):
                            auxI = auxI +1
                            auxJ= auxJ 
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]
                        if(posicao_pixel == 6):
                            auxI = auxI +1
                            auxJ= auxJ -1
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]
                        if(posicao_pixel == 7):
                            auxI = auxI
                            auxJ= auxJ -1
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]    
                        if(posicao_pixel == 8):
                            auxI = auxI
                            auxJ= auxJ
                            valor_pixel_atual = arrayRgb[auxI, auxJ, k]

                        if op == 1:  #Calculo da média
                                nome_filtro = "filtro_media"
                                pixel = filtro_media(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                        
                        elif op == 2: 
                            nome_filtro = "filtro_passa_alta_norte"
                            pixel = filtro_passa_alta_norte(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                
                        elif op == 3:
                            nome_filtro = "filtro_passa_alta_sul"
                            pixel = filtro_passa_alta_sul(auxI, auxJ, valor_pixel_atual, posicao_pixel)
    
                        elif op == 4: 
                            nome_filtro = "filtro_passa_alta_leste"
                            pixel = filtro_passa_alta_leste(auxI, auxJ, valor_pixel_atual, posicao_pixel)
        
                        elif op == 5:
                            nome_filtro = "filtro_passa_alta_oeste" 
                            pixel = filtro_passa_alta_oeste(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                
                        elif op == 6: 
                            nome_filtro = "filtro_passa_alta_nordeste" 
                            pixel = filtro_passa_alta_nordeste(auxI, auxJ, valor_pixel_atual, posicao_pixel)
        
                        elif op == 7: 
                            nome_filtro = "filtro_passa_alta_noroeste" 
                            pixel = filtro_passa_alta_noroeste(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                
                        elif op == 8: 
                            nome_filtro = "filtro_passa_alta_sudeste" 
                            pixel = filtro_passa_alta_sudeste(auxI, auxJ, valor_pixel_atual, posicao_pixel)
            
                        elif op == 9: 
                            nome_filtro = "filtro_passa_alta_sudoeste" 
                            pixel = filtro_passa_alta_sudoeste(auxI, auxJ, valor_pixel_atual, posicao_pixel)
            
                        elif op == 10: 
                            nome_filtro = "filtro_passa_alta_horizontais" 
                            pixel = filtro_passa_alta_horizontais(auxI, auxJ, valor_pixel_atual, posicao_pixel)
            
                        elif op == 11: 
                            nome_filtro = "filtro_passa_alta_verticais" 
                            pixel = filtro_passa_alta_verticais(auxI, auxJ, valor_pixel_atual, posicao_pixel)
            
                        elif op == 12: 
                            nome_filtro = "filtro_passa_alta_mais_quarenta_cinco" 
                            pixel = filtro_passa_alta_mais_quarenta_cinco(auxI, auxJ, valor_pixel_atual, posicao_pixel)

                        elif op == 13: 
                            nome_filtro = "filtro_passa_alta_menos_quarenta_cinco"
                            pixel = filtro_passa_alta_menos_quarenta_cinco(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                    
                        elif op == 14: 
                            nome_filtro = "filtro_sobel_horizontal"
                            pixel = filtro_sobel_horizontal(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                
                        elif op == 15: 
                            nome_filtro = "filtro_sobel_vertical"
                            pixel = filtro_sobel_vertical(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                        
                        elif op == 16: 
                            nome_filtro = "filtro_sobel_soma"
                            pixel = filtro_sobel_horizontal(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                            pixel_somatorio = pixel_somatorio + pixel
                            pixel = filtro_sobel_vertical(auxI, auxJ, valor_pixel_atual, posicao_pixel)
                            #pixel_somatorio = pixel_somatorio + pixel
                                                
                        pixel_somatorio = pixel_somatorio + pixel

                imagem_filtro[i, j, k] = pixel_somatorio     
                           
    imagem_convertida = Image.fromarray(imagem_filtro, mode='RGB')
    imagem_convertida.save(f'filtros_selecionados/{nome_formatado}_{nome_filtro}.jpg', format='JPEG')
    imagem_convertida.show()
    print(f"Programa finalizado, {nome_filtro} realizado com sucesso na imagem {nome_formatado}.")
    return

main()  