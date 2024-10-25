from lineas_y_circulos import lineas as ln, circulos as circ
# Definición de la función de activación escalón
def step_activation(suma):
    return 1 if suma >= 0 else 0

# Definición de la función softmax para la capa de salida
def softmax(salidas):
    max_val = max(salidas)
    exps = [pow(2.718281828459045, o - max_val) for o in salidas]  # Usando e≈2.71828
    sum_exps = sum(exps)
    salida = [exp / sum_exps for exp in exps]
    return salida

# Definición de la estructura del perceptrón
class Perceptron:
    def __init__(self, input_size, hidden_size=10, output_size=2):
        # Inicialización de pesos por defecto
        self.weights_input_hidden = []
        for _ in range(hidden_size):
            # Puedes ajustar estos pesos manualmente
            self.weights_input_hidden.append([0.5 for _ in range(input_size)])
        
        # Pesos de la capa oculta a la capa de salida
        self.weights_hidden_output = []
        for _ in range(output_size):
            # Puedes ajustar estos pesos manualmente
            self.weights_hidden_output.append([0.5 for _ in range(hidden_size)])
        
        # Bias para la capa oculta y salida
        self.bias_hidden = 0.0
        self.bias_output = 0.0

    def forward(self, x):
        # Capa oculta
        hidden_sums = []
        neurona = 1
        for neuron_weights in self.weights_input_hidden:
            suma = sum([xi * wi for xi, wi in zip(x, neuron_weights)]) + self.bias_hidden
            #print(f"Suma de pesos de la neurona {neurona}: {suma}")  # Para debuguear
            activated = step_activation(suma)
            hidden_sums.append(activated)
            neurona += 1
        
        print(f"Salida capa oculta: {hidden_sums}")  # Para debuguear
        
        # Capa de salida
        output_sums = []
        for neuron_weights in self.weights_hidden_output:
            suma = sum([hi * whi for hi, whi in zip(hidden_sums, neuron_weights)]) + self.bias_output
            output_sums.append(suma)
        
        print(f"Salida capa de salida (antes de softmax): {output_sums}")  # Para debuguear
        
        # Aplicar softmax
        output_probs = softmax(output_sums)
        print(f"Salida de la capa de salida (softmax): {output_probs}")  # Para debuguear
        
        return output_probs



# Conjunto de prueba
lineas = ln
circulos = circ

# Etiquetas: Valores reales esperados. 1 para línea, 2 para círculo
etiquetas = [1] * 30 + [2] * 30  # 30 líneas y 30 círculos

# Crear el perceptrón
input_size = 100  # Neuronas de entrada. 10x10 píxeles
hidden_size = 10  # Tamaño de la capa oculta
output_size = 2   # Capa de salida: Línea o Círculo

perceptron = Perceptron(input_size, hidden_size, output_size)

# Ajuste manual de pesos y bias (ejemplo)
perceptron.weights_input_hidden = [
    # Neurona 1 de la capa oculta (detecta líneas horizontales)
    [1 if 34 <= i < 72 else -0.4 for i in range(100)],  
    
    # Neurona 2 de la capa oculta (detecta líneas verticales)
    [1 if i%10==5 or i%10==4 or i%10==6 else -0.1 for i in range(100)],  
    
    # Neurona 3 de la capa oculta (detecta bordes de círculos)
    [1 if (i in [2, 3, 4, 5, 6, 7, 10, 11, 12, 16, 17, 18, 20, 21, 22, 
                27, 28, 29, 70, 79, 80, 89, 91, 92, 93, 94]) else -0.5 for i in range(100)],  
    
    # Neurona 4 de la capa oculta (detecta píxeles en las esquinas)
    [1 if i in [1, 2, 3, 10, 11, 12, 20, 21, 6, 7, 8, 17, 18, 19, 28, 29, 70, 
                71, 77,78, 80, 81, 87, 88, 91, 92, 93, 96,97,98] else -0.45 for i in range(100)], 
    
    # Neurona 5 de la capa oculta (detecta lineas diagonales)
    [1 if i in [0, 11, 22, 33, 44, 55, 66, 77, 88, 99] else -0.51 for i in range(100)],
    
    # Neurona 6 de la capa oculta (detecta lineas diagonales inversas)
    [1 if i in [9, 18, 27, 36, 45, 54, 63, 72, 81, 90] else -0.51 for i in range(100)],
    
    # Neurona 7 de la capa oculta (detecta centro de circulos vacios)
    [1 if i in [33, 34, 35, 43, 44, 45, 53, 54, 55, 63, 64, 65, 73, 74, 75] else -1 for i in range(100)],
    
    # Neurona 8 de la capa oculta (detecta esquinas de circulos vacios)
    [1 if i in [0, 9, 90, 99] else -0.01 for i in range(100)],
    
    # Neurona 9 de la capa oculta (detecta lineas en bordes de circulos)
    [-0.1 if i in [0, 9, 90, 99, 43, 44, 45, 46, 53, 54, 55, 56, 63, 64, 65, 66] else 0.8 for i in range(100)],
    
    # Neurona 10 (detectan otros patrones, pero con menor peso)
    [0.4 for _ in range(100)]
]

perceptron.weights_hidden_output = [
    # Neurona de salida 1 (clasifica como línea)
    [1, 0.8, -1, -1, 1, 1, -1, 0.2, -0.81, 0.1],  
    
    # Neurona de salida 2 (clasifica como círculo)
    [-1, -1, 1, 1, -1, -1, -0.5, -0.1, 1.1, 0.3]
]

perceptron.bias_hidden = -5.5  # Sesgo negativo para ayudar a que las neuronas de la capa oculta no se activen fácilmente
perceptron.bias_output = 0.1  # Sesgo positivo para la salida, ajustado para mejorar la discriminación

# Evaluación del perceptrón
correctos = 0
total = len(etiquetas)
#print(len(lineas), len(circulos), total)

buenos = 0
sin_clasificacion = 0
for i in range(total):
    isGood = "M"
    x = lineas[i] if i < 30 else circulos[i - 30]
    output = perceptron.forward(x)
    if output[0] > output[1]:
        prediccion = 1
    elif output[0] < output[1]:
        prediccion = 2
    else:
        print("No se pudo clasificar")
        prediccion = 0
        isGood = "0"
        sin_clasificacion += 1
    if prediccion == etiquetas[i]:
        correctos += 1
        isGood = "B"
        buenos += 1
    print(f"Ejemplo {i+1} ({isGood}): Esperado={etiquetas[i]}, Predicción={prediccion}\n")
malos = total - correctos - sin_clasificacion
print(f"Correctos: {buenos}, Incorrectos: {malos}, Sin clasificar: {sin_clasificacion}\n")

precision = (correctos / total) * 100
print(f"Precisión del modelo: {precision}%")

# Guardar lista de líneas y círculos en un archivo con el mismo formato que el original
# solo si la precisión es mayor o igual a 65%
# Si el archivo ya existe, se sobreescribe
if precision >= 77:
    with open("lineas_y_circulos.py", "w") as file:
        file.write(f"# Lista de líneas y círculos con {precision}% de presición \n")
        file.write("lineas = [\n")
        for i in range(30):
            file.write("[\n")
            for row in range(10):
                file.write(", ".join(map(str, lineas[i][row*10:(row+1)*10])) + ",\n")
            file.write("],\n")
        file.write("]\n")
        file.write("\ncirculos = [\n")
        for i in range(30):
            file.write("[\n")
            for row in range(10):
                file.write(", ".join(map(str, circulos[i][row*10:(row+1)*10])) + ",\n")
            file.write("],\n")
        file.write("\n]")
    print("Archivo guardado con éxito")
