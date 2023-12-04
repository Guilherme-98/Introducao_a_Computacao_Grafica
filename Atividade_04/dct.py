from PIL import Image, ImageOps
import numpy as np

def calculoAlpha(u, n):
    if u == 0:
        return np.sqrt(1 / n)
    else:
        return np.sqrt(2 / n)

def calculoCosseno(x, aux, n):
    calc = ((2 * x + 1) * aux * np.pi) / (2 * n)

    return np.cos(calc)

def calculoTransformadaCossenoDiscreta(matrix, n, m):
    frequenciaArray = np.zeros((n, m), dtype=np.double)
    for u in range(n):
        for v in range(m):
            suma = 0

            for x in range(n):
                for y in range(m):
                    suma += matrix[x, y] * calculoCosseno(x, u, n) * calculoCosseno(y, v, m)
            
            frequenciaArray[u, v] = calculoAlpha(u, n) * calculoAlpha(v, m) * suma

    return frequenciaArray

def transformarArrayCinza(matrix, n, m):
    grayscale = np.zeros((n, m), dtype=np.uint8)

    for i in range(n):
        for j in range(m):
            if matrix[i, j] <= 0:
                grayscale[i, j] = 0
            elif matrix[i, j] >= 255:
                grayscale[i, j] = 255   
            else:
                grayscale[i, j] = matrix[i, j]

    return grayscale

def calculoTransformadaInversaDiscretaCosseno(matrix, n, m):
    array = np.zeros((n, m), dtype=np.double)

    for x in range(n):
        for y in range(m):
            sum = 0

            for u in range(n):
                for v in range(m):
                    sum += calculoAlpha(u, n) * calculoAlpha(v, m) * matrix[u, v] * calculoCosseno(x, u, n) * calculoCosseno(y, v, m)
            
            array[x, y] = sum
    
    return array

def pontosDentroRetangulo(x, y, w, h, px, py):
    if px >= x and px <= x + w and py >= y and py <= y + h:
        return True

    return False

def gerandorRuidos(frequenciaArray, n, m):
    ruidoImage = np.zeros((n, m), dtype=np.double)

    for x in range(n):
        for y in range(m):
            if pontosDentroRetangulo(n / 2, m / 2, 5, 5, x, y):
                ruidoImage[x, y] = 255
            else:
                ruidoImage[x, y] = frequenciaArray[x, y]

    return ruidoImage

def getDist(x, y):
    return np.sqrt(x**2 + y**2)

def passaBaixaFiltroIdeal(frequenciaArray, r, n, m):
    passaBaixarray = np.zeros((n, m), dtype=np.double)

    for x in range(n):
        for y in range(m):
            dist = getDist(x, y)
            
            if dist <= r:
                passaBaixarray[x, y] = frequenciaArray[x, y]
            else:
                passaBaixarray[x, y] = 0
    
    return passaBaixarray

def passaAltaFiltroIdeal(frequenciaArray, r, n, m):
    passaAltaArray = np.zeros((n, m), dtype=np.double)

    for x in range(n):
        for y in range(m):
            dist = getDist(x, y)

            if dist > r:
                passaAltaArray[x, y] = frequenciaArray[x, y]
            else:
                passaAltaArray[x, y] = 0
    
    return passaAltaArray

imgFile = input('Digite o nome da imagem: ')
imgName = imgFile.split('.')[0]

raioPassaBaixa = int(input('Digite o raio do corte para o Filtro Passa-Baixa: '))
raioPassaAlta = int(input('Digite o raio do corte para o Filtro Passa-Alta: '))

img = Image.open(f'imagem_pre_dct/{imgFile}')
img = ImageOps.exif_transpose(img)

imgArray = np.asarray(img)

# Frequência
print('\nCalculando a frequência da imagem através da Transformada Discreta do Cosseno.\n')

frequenciaArray = calculoTransformadaCossenoDiscreta(imgArray, img.height, img.width)
cinzaFrequenciaArray = transformarArrayCinza(frequenciaArray, img.height, img.width)

frequenciaImg = Image.fromarray(cinzaFrequenciaArray, mode='L')
frequenciaImg.save(f'imagens_pos_dct/{imgName}-frequencia-imagem.png', format='PNG')
frequenciaImg.show()

# Frequencia Inversa
print('Gerando a imagem original através da Transformada Inversa Discreta do Cosseno.\n')
frequenciaInversoArray = calculoTransformadaInversaDiscretaCosseno(frequenciaArray, img.height, img.width)
cinzaFrequenciaInversoArray = transformarArrayCinza(frequenciaInversoArray, img.height, img.width)

inversoImg = Image.fromarray(cinzaFrequenciaInversoArray, mode='L')
inversoImg.save(f'imagens_pos_dct/{imgName}-Frequencia-inversa-imagem.png', format='PNG')
inversoImg.show()

# Passa-Baixa
print('Aplicando o filtro Passa-Baixa na frequência.\n')
passaBaixaFreqArray = passaBaixaFiltroIdeal(frequenciaArray, raioPassaBaixa, img.height, img.width)
cinzaPassaBaixaFreqArray = transformarArrayCinza(passaBaixaFreqArray, img.height, img.width)

passaBaixaFreqImg = Image.fromarray(cinzaPassaBaixaFreqArray, mode='L')
passaBaixaFreqImg.save(f'imagens_pos_dct/{imgName}-filtro-passa-baixa-imagem-frequencia-raio{raioPassaBaixa}.png', format='PNG')
passaBaixaFreqImg.show()

# Passa-Baixa (Inversa)
print('Gerando a imagem original com o filtro Passa-Baixa aplicado através da Transformada Inversa Discreta do Cosseno.\n')
passaBaixaImgArray = calculoTransformadaInversaDiscretaCosseno(passaBaixaFreqArray, img.height, img.width)
cinzaPassaBaixaImgArray = transformarArrayCinza(passaBaixaImgArray, img.height, img.width)

passaBaixaImg = Image.fromarray(cinzaPassaBaixaImgArray, mode='L')
passaBaixaImg.save(f'imagens_pos_dct/{imgName}-filtro-passa-baixa-imagem-raio{raioPassaBaixa}.png', format='PNG')
passaBaixaImg.show()

# Passa-Alta
print('Aplicando o filtro Passa-Alta na frequência.\n')
passaAltaFreqArray = passaAltaFiltroIdeal(frequenciaArray, raioPassaAlta, img.height, img.width)
cinzaPassaAltaFreqArray = transformarArrayCinza(passaAltaFreqArray, img.height, img.width)

passaAltaFreqImg = Image.fromarray(cinzaPassaAltaFreqArray, mode='L')
passaAltaFreqImg.save(f'imagens_pos_dct/{imgName}-filtro-passa-alta-imagem-frequencia-raio{raioPassaAlta}.png', format='PNG')
passaAltaFreqImg.show()

# Passa-Alta (Inversa)
print('Gerando a imagem original com o filtro Passa-Alta aplicado através da Transformada Inversa Discreta do Cosseno.\n')
passaAltaImgArray = calculoTransformadaInversaDiscretaCosseno(passaAltaFreqArray, img.height, img.width)
cinzaPassaAltaImgArray = transformarArrayCinza(passaAltaImgArray, img.height, img.width)

passaAltaImg = Image.fromarray(cinzaPassaAltaImgArray, mode='L')
passaAltaImg.save(f'imagens_pos_dct/{imgName}-filtro-passa-alta-imagem-raio{raioPassaAlta}.png', format='PNG')
passaAltaImg.show()

# Geração de ruído na frequência
print('Gerando ruído na frequência da imagem.\n')
ruidoFrequenciaArray = gerandorRuidos(frequenciaArray, img.height, img.width)
cinzaRuidoFreqArray = transformarArrayCinza(ruidoFrequenciaArray, img.height, img.width)

ruidoFrequenciaImg = Image.fromarray(cinzaRuidoFreqArray, mode='L')
ruidoFrequenciaImg.save(f'imagens_pos_dct/{imgName}-ruido-imagem-frequencia.png', format='PNG')
ruidoFrequenciaImg.show()

# Geração da imagem com frequência ruidosa
print('Gerando a nova imagem a partir da frequência ruidosa.\n')
ruidoImgArray = calculoTransformadaInversaDiscretaCosseno(ruidoFrequenciaArray, img.height, img.width)
cinzaRuidoImgArray = transformarArrayCinza(ruidoImgArray, img.height, img.width)

ruidoImg = Image.fromarray(cinzaRuidoImgArray, mode='L')
ruidoImg.save(f'imagens_pos_dct/{imgName}-ruido-imagem.png')
ruidoImg.show()