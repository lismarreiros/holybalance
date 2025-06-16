import easyocr
import cv2
from matplotlib import pyplot as plt
import matplotlib.patches as patches

img = 'images/temp_processed.jpeg'

img = cv2.imread(img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(['pt'])
results = reader.readtext(img)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img_rgb)

for idx, (bbox, text, conf) in enumerate(results):
    # transforma coordenadas de caixa em (x, y, largura, altura)
    x_coords = [point[0] for point in bbox]
    y_coords = [point[1] for point in bbox]

    x_min = min(x_coords)
    y_min = min(y_coords)
    width = max(x_coords) - x_min
    heigth = max(y_coords) - y_min

    # desenha o retângulo
    rect = patches.Rectangle(
        (x_min, y_min), width, heigth,
        linewidth=2, edgecolor='red', facecolor='none'
    )
    ax.add_patch(rect)

    # adiciona número da caixa
    ax.text(
        x_min, y_min - 5, str(idx),
        fontsize=12, color='red', weight='bold'
    )


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off') # desativa os eixos para uma visualização mais limpa
plt.show()

caixa6_texto = results[8][1]

print(caixa6_texto);