# Leitura de Texto com Python e OCR

Este script utiliza o Tesseract OCR e a biblioteca `pytesseract` para extrair texto de imagens. Siga as instruções abaixo para instalar e executar o código.

## Pré-requisitos

Antes de executar o script, é recomendado iniciar e ativar seu ambiente virtual python e após isso instalar o Tesseract OCR e as bibliotecas Python necessárias que estão no arquivo `requirements.txt`.

### 1. Instalar o Tesseract OCR
Execute o seguinte comando para instalar o Tesseract OCR no seu sistema:

```bash
sudo apt install tesseract-ocr -y
```

### 2. Instalar as dependências Python
Instale as bibliotecas pytesseract e pillow usando o pip:

```bash
pip install pytesseract pillow
```
### 3. Execute o script `extrair-texto.py`:
siga a instrução que surge no terminal `digite o nome do arquivo com a extensão: `
exemplo: `image.png`
O resultado vai surgir no terminal.

### Como Funciona
1. O código usa a biblioteca Pillow para abrir a imagem.

2. O pytesseract.image_to_string() é responsável por processar a imagem e extrair o texto.

3. O texto extraído é impresso no console.