import cv2

# Carregar a imagem original
imagem_original = cv2.imread('imagem_original.png')

# Obter a largura e altura da imagem original
largura_original = imagem_original.shape[1]
altura_original = imagem_original.shape[0]

# Calcular a nova largura e altura reduzidas em 50%
nova_largura = int(largura_original * 0.5)
nova_altura = int(altura_original * 0.5)

# Redimensionar a imagem para a nova largura e altura
imagem_reduzida = cv2.resize(imagem_original, (nova_largura, nova_altura))
cv2.imwrite(f'imagem_original_reduzida.png', imagem_reduzida)

# Exibir a imagem reduzida
cv2.imshow('Imagem Reduzida', imagem_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows()
