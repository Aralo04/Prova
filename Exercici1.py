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

# Clase Red Neuronal
class RedNeuronal:
    def __init__(self, num_neuronas, num_entradas):
        # Crear un conjunto de neuronas
        self.neuronas = [Neurona(num_entradas) for _ in range(num_neuronas)]

    def calcular_salida(self, entradas):
        # Calcular la salida de cada neurona en la capa
        salidas_capa = [neurona.calcular_salida(entradas) for neurona in self.neuronas]
        return salidas_capa

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una red neuronal con 5 neuronas en una capa y 3 entradas
    red_neuronal = RedNeuronal(5, 2)

    # Entradas de ejemplo
    entradas = np.array([0.5, 0.2])

    # Calcular la salida de la red neuronal
    salida_capa = red_neuronal.calcular_salida(entradas)

    print("Salida de la capa de neuronas:", salida_capa)