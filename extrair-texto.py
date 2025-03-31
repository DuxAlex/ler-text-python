import pytesseract
from PIL import Image

try:
    # Carregar a imagem
    image_path = (input("digite o nome do arquivo com a extensão: ")) # Caminho da imagem
    image = Image.open(image_path)

    # Extrair texto da imagem usando OCR
    extracted_text = pytesseract.image_to_string(image)

    # Exibir o texto extraído
    print(extracted_text)
    
except Exception as e:
    print(f"Erro: {e}")
