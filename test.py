import easyocr
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches


img = 'images/temp_processed.jpeg'

img = cv2.imread(img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(['pt'])
results = reader.readtext(img, detail=1, paragraph=False, decoder='greedy', add_margin=0.1, width_ths=1.5)

def filtrar_por_coluna(results, x_min_ref, x_max_ref):
    filtrados = []
    for idx, (bbox, text, conf) in enumerate(results):
        x_coords = [p[0] for p in bbox]
        box_x_min = min(x_coords)
        box_x_max = max(x_coords)
        # Mantém caixas que tenham pelo menos uma parte dentro da faixa da coluna
        if box_x_max >= x_min_ref and box_x_min <= x_max_ref:
            filtrados.append((idx, bbox, text, conf))
    return filtrados

# Faixas horizontais da tabela (ajuste os números abaixo conforme a sua imagem)
quantidade_x_min = 400
quantidade_x_max = 600

total_x_min = 600
total_x_max = 800

# Filtrar
quantidade_results = filtrar_por_coluna(results, quantidade_x_min, quantidade_x_max)
total_results = filtrar_por_coluna(results, total_x_min, total_x_max)

# Plotar
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img)

# Quantidade (verde)
for idx, bbox, text, conf in quantidade_results:
    x_min = min([p[0] for p in bbox])
    y_min = min([p[1] for p in bbox])
    width = max([p[0] for p in bbox]) - x_min
    height = max([p[1] for p in bbox]) - y_min
    rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='green', facecolor='none')
    ax.add_patch(rect)
    ax.text(x_min, y_min - 5, f"{idx}", color='green', fontsize=8)

# Total (azul)
for idx, bbox, text, conf in total_results:
    x_min = min([p[0] for p in bbox])
    y_min = min([p[1] for p in bbox])
    width = max([p[0] for p in bbox]) - x_min
    height = max([p[1] for p in bbox]) - y_min
    rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='blue', facecolor='none')
    ax.add_patch(rect)
    ax.text(x_min, y_min - 5, f"{idx}", color='blue', fontsize=8)

plt.show()
