import cv2
import glob
import sys
import json

# Função para lidar com o clique do mouse
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Marcar o ponto-chave
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
        # Atualizar a exibição da imagem
        cv2.imshow('Image', image)
        # Armazenar as coordenadas do ponto-chave
        key_points.append([x, y])  # Converter para uma lista ao invés de tupla

# Caminho do diretório de imagens
image_directory = "Train Custom Key Point Detection Model/imagens_annotation"

# Padrão de correspondência para as extensões de imagem
image_pattern = "*.jpg"  # ou "*.png", "*.jpeg", etc.

# Lista de caminhos de imagens
image_paths = glob.glob(f"{image_directory}/{image_pattern}")

# Variável de controle para acompanhar a escolha do usuário
stop_execution = False

# Loop para processar cada imagem
for image_path in image_paths:
    # Lista para armazenar as coordenadas dos pontos-chave
    key_points = []

    # Carregar a imagem
    image = cv2.imread(image_path)

    # Criar uma janela para exibir a imagem
    cv2.namedWindow('Image')

    # Associar a função de callback do mouse à janela
    cv2.setMouseCallback('Image', mouse_callback)

    # Loop principal
    while True:
        # Exibir a imagem
        cv2.imshow('Image', image)

        # Aguardar pela tecla 'Esc' para sair do loop atual
        key = cv2.waitKey(1)
        if key == 27:  # Tecla Esc
            break

        # Aguardar pela tecla 'q' para encerrar completamente a execução do programa
        if key == ord('q'):
            stop_execution = True
            break

    if stop_execution:
        break

    # Salvar as coordenadas dos pontos-chave em um arquivo JSON
    json_filename = f"{image_path}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(key_points, json_file)

    # Fechar a janela atual antes de prosseguir para a próxima imagem
    cv2.destroyAllWindows()
