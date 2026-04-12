from src.models.perceptron import Perceptron

def run():
    print("Executando Perceptron Manual - Tema Titanic")
    
    X_train = [[3, 1], [1, 0], [3, 1], [1, 0]]
    y_train = [0, 1, 0, 1]

    clf = Perceptron(learning_rate=0.1, n_iters=100)
    clf.fit(X_train, y_train)
    
    teste = [[1, 0]]
    pred = clf.predict(teste)
    
    resultado = 'Sobreviveu' if pred[0] == 1 else 'Morreu'
    print(f"Predição para passageiro {teste[0]}: {resultado}")

if __name__ == "__main__":
    run()