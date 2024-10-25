# Perceptrón para Clasificación de Líneas y Círculos

Este proyecto implementa un perceptrón para clasificar imágenes de 10x10 píxeles en dos categorías: líneas y círculos. El perceptrón utiliza una capa oculta y una capa de salida con una función de activación softmax.

## Estructura del Proyecto

- `perceptron.py`: Contiene la implementación del perceptrón y su lógica de clasificación.
- `lineas_y_circulos.py`: Contiene las listas de ejemplos de líneas y círculos generados.
- `lineas_circulos.py`: Genera ejemplos de imágenes de líneas y círculos.
- `README.md`: Este archivo, que explica el proyecto y cómo ejecutarlo.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio:

    ```sh
    git clone https://github.com/Diego-LC/Perceptron.git
    ```

2. Navega al directorio del proyecto:

    ```sh
    cd Perceptron
    ```

## Ejecución

Para ejecutar el perceptrón y clasificar las imágenes, simplemente ejecuta el archivo `perceptron.py`:

```sh
python perceptron.py
```

## Funcionamiento

1. **Generación de Imágenes**:

    - `lineas_circulos.py` genera ejemplos de imágenes de líneas y círculos en una matriz de 10x10 píxeles.
    - Las imágenes se aplanan en una lista de 100 elementos para ser utilizadas como entrada al perceptrón.

2. **Definición del Perceptrón**:
    - El perceptrón tiene una capa de entrada de 100 neuronas, una capa oculta de 10 neuronas y una capa de salida de 2 neuronas.
    - Se utilizan funciones de activación escalón y softmax.

3. **Clasificación**:
    - El perceptrón clasifica las imágenes en líneas o círculos basándose en los pesos y sesgos ajustados manualmente.
    - La precisión del modelo se imprime al final de la ejecución.

## Ejemplo de Salida

```sh
Ejemplo 1 (B): Esperado=1, Predicción=1
Ejemplo 2 (M): Esperado=1, Predicción=2

...

Correctos: 46, Incorrectos: 14, Sin clasificar: 0
Precisión del modelo: 76.66666666666667%
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
