class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = 0.0

    def activation_func(self, x):
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = self.bias
                for i in range(n_features):
                    linear_output += x_i[i] * self.weights[i]
                
                y_predicted = self.activation_func(linear_output)
                
                update = self.lr * (y[idx] - y_predicted)
                
                for i in range(n_features):
                    self.weights[i] += update * x_i[i]
                self.bias += update

    def predict(self, X):
        predictions = []
        for x_i in X:
            linear_output = self.bias
            for i in range(len(x_i)):
                linear_output += x_i[i] * self.weights[i]
            predictions.append(self.activation_func(linear_output))
        return predictions