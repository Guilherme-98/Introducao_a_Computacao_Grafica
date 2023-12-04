from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

nome_imagem = input('Digite o nome da imagem para equalização de histograma:')
nome_formatado = nome_imagem.split('.')[0]

imagemRgb = Image.open(f'rgb-imagens/{nome_imagem}')
imagemRgb = ImageOps.exif_transpose(imagemRgb)

arrayRgb = np.asarray(imagemRgb)
# print(arrayRgb.shape)
# print(arrayRgb.size)
# print(arrayRgb.ndim)

# Histograma

histograma = np.zeros((3, 256))

for linha_imagem in arrayRgb:
    for pixel in linha_imagem:
        histograma[0, pixel[0]] += 1
        histograma[1, pixel[1]] += 1
        histograma[2, pixel[2]] += 1

plt.plot(histograma[0], color='red')
plt.plot(histograma[1], color='green')
plt.plot(histograma[2], color='blue')

plt.title('HISTOGRAMA')
plt.xlabel('Valor da cor')
plt.ylabel('Frequência')
plt.show()

#Histograma Normalizado

histograma_normalizado = np.zeros((3, 256))

for cor in range(len(histograma)):
    for valor in range(len(histograma[cor])):
        histograma_normalizado[cor, valor] = (histograma[cor, valor] / (imagemRgb.width * imagemRgb.height))

plt.plot(histograma_normalizado[0], color='red')
plt.plot(histograma_normalizado[1], color='green')
plt.plot(histograma_normalizado[2], color='blue')

plt.title('HISTOGRAMA NORMALIZADO')
plt.xlabel('Valor da cor')
plt.ylabel('Frequência')
plt.show()

# Histograma Acumulado

histograma_acumulado = np.zeros((3, 256))

for cor in range(len(histograma_normalizado)):
    for frequencia in range(len(histograma_normalizado[cor])):
        if frequencia != 0:
            histograma_acumulado[cor, frequencia] = histograma_acumulado[cor, frequencia - 1] + histograma_normalizado[cor, frequencia]
        else:
            histograma_acumulado[cor, frequencia] = histograma_normalizado[cor, frequencia]

plt.plot(histograma_acumulado[0], color='red')
plt.plot(histograma_acumulado[1], color='green')
plt.plot(histograma_acumulado[2], color='blue')

plt.title('HISTOGRAMA ACUMULADO')
plt.xlabel('Valor da cor')
plt.ylabel('Frequência')
plt.show()

# Imagem equalizada

array_equalizado = np.zeros((imagemRgb.height, imagemRgb.width, 3), dtype = np.uint8)

for i in range(imagemRgb.height):
    for j in range(imagemRgb.width):
        for k in range(3):
            array_equalizado[i, j, k] = round(255 * histograma_acumulado[k, arrayRgb[i, j, k]])

imagem_equalizada = Image.fromarray(array_equalizado, mode='RGB')
imagem_equalizada.save(f'imagem_equalizada/{nome_formatado}.jpg', format='JPEG')
imagem_equalizada.show()

# Histograma Após Equalização

for linha_imagem in array_equalizado:
    for pixel in linha_imagem:
        histograma[0, pixel[0]] += 1
        histograma[1, pixel[1]] += 1
        histograma[2, pixel[2]] += 1

plt.plot(histograma[0], color='red')
plt.plot(histograma[1], color='green')
plt.plot(histograma[2], color='blue')

plt.title('HISTOGRAMA APÓS EQUALIZAÇÃO')
plt.xlabel('Valor da cor')
plt.ylabel('Frequência')
plt.show()

print("Equalização de histograma realizado com sucesso")