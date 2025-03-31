import pytesseract
from PIL import Image
import cv2
import numpy as np

try:
    # Carregar a imagem
    image_path = input("Digite o nome do arquivo com a extensão: ")  # Caminho da imagem
    image = Image.open(image_path)

    # Converter a imagem para um formato que o OpenCV pode usar
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Pré-processamento: converter para escala de cinza
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Aplicar binarização
    _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

    # Extrair texto da imagem usando OCR com configuração para tabelas
    custom_config = r'--oem 3 --psm 6'  # Modo de segmentação para tabelas
    extracted_text = pytesseract.image_to_string(binary_image, config=custom_config)

    # Exibir o texto extraído
    print(extracted_text)

except Exception as e:
    print(f"Erro: {e}")
