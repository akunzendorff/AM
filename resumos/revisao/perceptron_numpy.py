import numpy as np

class PerceptronNumpy:
    def __init__(self, pesos, bias):
        self.weights = np.array(pesos)
        self.bias = bias

    def predict(self, matriz_cliente):
        # Processa todos os clientes com np.dot
        z = np.dot(matriz_cliente, self.weights) + self.bias

        return (z >= 0).astype(int)

