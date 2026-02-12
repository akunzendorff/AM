# Keras é uma API de alto nível do TensorFlow que facilita a construção e treinamento de redes neurais
import tensorflow as tf
from tensorflow import keras

# Carregar dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Criar modelo simples
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compilar e treinar
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# Testar
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Acurácia: {accuracy * 100:.2f}%")