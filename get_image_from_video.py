# imports
import cv2
import os

# função para extrair imagens do vídeo

def extract_frames(video_path, output_directory, max_frames=None):
    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Carregar o vídeo
    video = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        # Ler o próximo frame
        ret, frame = video.read()

        # Verificar se o frame foi lido corretamente
        if not ret:
            break

        # Salvar o frame como uma imagem
        frame_path = os.path.join(output_directory, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        # Incrementar o contador de frames
        frame_count += 1

        # Verificar se o limite de imagens foi atingido
        if max_frames is not None and frame_count >= max_frames:
            break

    # Liberar o vídeo e fechar as janelas abertas
    video.release()
    cv2.destroyAllWindows()


video_path = '/home/eric/projetos pessoais/computer-vision/Train Custom Key Point Detection Model/vídeo/soft robots.mp4'
output_directory = 'Train Custom Key Point Detection Model/imagens_annotation'
max_frames = 100  # Defina o número máximo de imagens a serem extraídas

extract_frames(video_path, output_directory, max_frames)