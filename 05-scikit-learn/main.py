import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    """
    Regressão Linear: encontra a melhor linha reta que descreve a relação entre X e y.
    Neste exemplo: y = 2 * X (ou seja, valores dobram).
    Esperamos que o modelo aprenda isso e preveja corretamente.
    """
    # Dados de entrada (X) e saída (y)
    X = np.array([[1], [2], [3], [4]])  # Features
    y = np.array([2, 4, 6, 8])  # Target (valores esperados)

    # Criar e treinar o modelo de regressão linear
    model = LinearRegression().fit(X, y)

    # Exibir o coeficiente (inclinação da reta)
    # Coeficiente: o número que multiplica X (neste caso, deveria ser ~2)
    print("Coeficiente:", model.coef_[0])

    # Fazer uma previsão para o valor 5
    print("Previsão para 7:", model.predict([[7]])[0])


if __name__ == "__main__":
    main()