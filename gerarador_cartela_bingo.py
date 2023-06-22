import cv2
import numpy as np
import random

quantidade = 5

# Definir posição dos números na imagem (ajuste conforme necessário)
x = 150
y = 870

x_aumento = 90
y_aumento = 90

posicoes = []

primeira_linha = [(x, y), (x + x_aumento, y), (x + x_aumento*2, y), (x + x_aumento*3, y), (x + x_aumento*4, y)]
segunda_linha = [(x, y - y_aumento), (x + x_aumento, y - y_aumento), (x + x_aumento*2, y - y_aumento), (x + x_aumento*3, y - y_aumento), (x + x_aumento*4, y - y_aumento)]
terceira_linha = [(x, y - y_aumento*2), (x + x_aumento, y - y_aumento*2), (x + x_aumento*2, y - y_aumento*2), (x + x_aumento*3, y - y_aumento*2), (x + x_aumento*4, y - y_aumento*2)]
quarta_linha = [(x, y - y_aumento*3), (x + x_aumento, y - y_aumento*3), (x + x_aumento*2, y - y_aumento*3), (x + x_aumento*3, y - y_aumento*3), (x + x_aumento*4, y - y_aumento*3)]
quinta_linha = [(x, y - y_aumento*4), (x + x_aumento, y - y_aumento*4), (x + x_aumento*2, y - y_aumento*4), (x + x_aumento*3, y - y_aumento*4), (x + x_aumento*4, y - y_aumento*4)]
todas_linhas = [primeira_linha, segunda_linha, terceira_linha, quarta_linha, quinta_linha]

for i in todas_linhas:
    for j in i:
        posicoes.append(j)

# Lista de números a serem adicionados
numeros_b = list(range(1, 16))
numeros_i = list(range(16, 31))
numeros_n = list(range(31, 46))
numeros_g = list(range(46, 61))
numeros_o = list(range(61, 76))
print(numeros_o)

# Gerar 60 cópias da imagem
for i in range(quantidade):
    # Carregar imagem original em formato PNG
    imagem_original_reduzida = cv2.imread('imagem_original_reduzida.png')

    # Gerar uma cópia da imagem
    imagem_processada = np.copy(imagem_original_reduzida)

    numeros_disponiveis = numeros_b + numeros_i + numeros_n + numeros_g + numeros_o
    numeros_adicionados = []


    # Adicionar os números na imagem
    for j, posicao in enumerate(posicoes):
        if j != 12:
            # Verificar restrições para os números nas posições específicas
            if j % 5 == 0:
                numeros_disponiveis = [num for num in numeros_b if num not in numeros_adicionados]
            elif j % 5 == 1:
                numeros_disponiveis = [num for num in numeros_i if num not in numeros_adicionados]
            elif j % 5 == 2:
                numeros_disponiveis = [num for num in numeros_n if num not in numeros_adicionados]
            elif j % 5 == 3:
                numeros_disponiveis = [num for num in numeros_g if num not in numeros_adicionados]
            elif j % 5 == 4:
                numeros_disponiveis = [num for num in numeros_o if num not in numeros_adicionados]

            # Verificar se ainda existem números disponíveis
            if numeros_disponiveis:
                # Selecionar um número aleatório disponível
                numero_selecionado = random.choice(numeros_disponiveis)

                # Converter o número selecionado para string
                numero_str = str(numero_selecionado)

                # Desenhar o número na imagem
                cv2.putText(imagem_processada, numero_str, posicao, cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 255), 3, cv2.LINE_AA)

                # Adicionar o número selecionado à lista de números adicionados
                numeros_adicionados.append(numero_selecionado)

    # Salvar a imagem processada
    cv2.imwrite(f'imagens_prontas/imagem_processada_{i+1}.png', imagem_processada)
