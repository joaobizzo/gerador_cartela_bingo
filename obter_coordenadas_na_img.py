import cv2
import matplotlib.pyplot as plt

# Carregar a imagem original
imagem_original_reduzida = cv2.imread('imagem_original_reduzida.png')

# Converter de BGR para RGB
imagem_rgb = cv2.cvtColor(imagem_original_reduzida, cv2.COLOR_BGR2RGB)

# Exibir a imagem original usando a biblioteca matplotlib
plt.imshow(imagem_rgb)
plt.axis('off')
plt.show()

# Função de callback para obter as coordenadas do clique do mouse
def obter_coordenadas(event):
    if event.button == 1:  # Botão esquerdo do mouse
        x = event.xdata
        y = event.ydata
        print(f'Posição (x, y): ({x}, {y})')

# Registrar a função de callback para eventos de clique do mouse
cid = plt.gcf().canvas.mpl_connect('button_press_event', obter_coordenadas)

# Aguardar até que a janela seja fechada
plt.show()
