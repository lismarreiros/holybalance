import easyocr
import cv2
from matplotlib import pyplot as plt

reader = easyocr.Reader(['pt'])
img = 'images/temp_processed.jpeg'
results = reader.readtext(img)

img = cv2.imread(img)

caixa6_texto = results[6][1]
caixa9_texto = results[9][1]
caixa12_texto = results[12][1]

texto_junto = caixa9_texto + ' ' + caixa12_texto

print(caixa6_texto);