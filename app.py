from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# 1. Abrir a imagem
image = Image.open("images/teste3.jpeg");

# Converter para escala de cinza
image = image.convert("L");

#  Aumentar o constrate
enhancer = ImageEnhance.Contrast(image);
image = enhancer.enhance(2.0)

# Aplicar filtro de nitidez 
image = image.filter(ImageFilter.SHARPEN);

# Salvar imagem tratada
image.save("images/teste2_processed.jpeg");

# 2. Extrair texto com OCR
custom_config = r'--oem 1 --psm 6'
text = pytesseract.image_to_string(image, lang="por", config=custom_config);
print(text)

# 3. Interpretar dados do texto
