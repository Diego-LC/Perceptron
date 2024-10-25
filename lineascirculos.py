import random
# Generadores de imágenes
def generate_line_image():
    row_selector = random.randint(0, 9)
    orientation = random.randint(0, 1)  # 0 para horizontal, 1 para vertical
    line_image = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(random.randint(9, 10)):
        for j in range(random.randint(8, 10)):
            if orientation == 0 and i == row_selector:
                line_image[i][j] = 1
            elif orientation == 1 and j == row_selector:
                line_image[i][j] = 1
    # Asegurar que haya al menos un pixel marcado
    if sum([sum(row) for row in line_image]) == 0:
        line_image[row_selector][random.randint(5, 9)] = 1
    return line_image

def generate_diagonal_image():
    diagonal_image1 = [0]*100
    diagonal_image2 = [0]*100
    for i in range(10):
        diagonal_image1[i*10 + i] = 1
        diagonal_image2[i*10 + 9 - i] = 1
    return [diagonal_image1, diagonal_image2]

def generate_circle_image():
    radius = random.randint(3, 4)  # Limita el radio entre 3 y 4
    center_x = random.randint(radius, 9 - radius)  # Asegura que el círculo no se salga de los bordes
    center_y = random.randint(radius, 9 - radius)
    # Ajusta el grosor del círculo entre 0.5 y 1
    border = (random.randint(0, 1)+0.5)*0.5
    circle_image = [[0 for _ in range(10)] for _ in range(10)]
    
    # Marcar el contorno del círculo (un pixel por cada punto en el círculo)
    for i in range(10):
        for j in range(10):
            # Calcular la distancia al centro
            distance_squared = (i - center_x) ** 2 + (j - center_y) ** 2
            # Verificar si está dentro del borde del círculo
            if (radius - border) ** 2 <= distance_squared <= (radius + border) ** 2:
                circle_image[i][j] = 1  # Marcar el contorno del círculo
    return circle_image

#Combinar la matriz de cada imagen en una sola lista
def flatten_image(image):
    return [pixel for row in image for pixel in row]

# Generar 30 listas de ejemplos de líneas y círculos
lineas = [flatten_image(generate_line_image()) for _ in range(28)] + generate_diagonal_image()
circulos = [flatten_image(generate_circle_image()) for _ in range(30)]

print("Ejemplos de líneas:")
for i, linea in enumerate(lineas):
    print(f"Ejemplo {i+1}:")
    for j in range(0, 100, 10):
        print(" ".join([str(x) for x in linea[j:j+10]]))
    print()

print("Ejemplos de círculos:")
for i, circulo in enumerate(circulos):
    print(f"Ejemplo {i+31}:")
    for j in range(0, 100, 10):
        print(" ".join([str(x) for x in circulo[j:j+10]]))
    print()

# Comprobar si hay ejemplos repetidos

print("Ejemplos repetidos:\n")
for i in range(30):
    if lineas[i] in lineas:
        print(f"Ejemplo {i+1} de línea está repetido")

for i in range(30):
    if circulos[i] in circulos:
        print(f"Ejemplo {i+31} de círculo está repetido")