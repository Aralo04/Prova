import numpy as np


# Función de activación (por ejemplo, función sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Clase Neurona
class Neurona:
    def __init__(self, num_entradas):
        # Inicializar pesos y sesgo de manera aleatoria
        self.pesos = np.random.rand(num_entradas)
        self.sesgo = np.random.rand()

    def calcular_salida(self, entradas):
        # Calcular la suma ponderada de las entradas y aplicar la función de activación
        suma_ponderada = np.dot(entradas, self.pesos) + self.sesgo
        salida = sigmoid(suma_ponderada)
        return salida


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una neurona con 3 entradas
    neurona = Neurona(3)

    # Entradas de ejemplo
    entradas = np.array([0.5, 0.2, 0.1])

    # Calcular la salida de la neurona
    salida = neurona.calcular_salida(entradas)

    print("Salida de la neurona:", salida)