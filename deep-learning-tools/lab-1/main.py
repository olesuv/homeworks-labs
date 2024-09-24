import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Завантаження даних
fashion_mnist = keras.datasets.fashion_mnist
(x_train_full, y_train_full), (x_test, y_test) = fashion_mnist.load_data()

VAL_SIZE = 4000
x_valid, x_train = x_train_full[:VAL_SIZE] / \
    255.0, x_train_full[VAL_SIZE:] / 255.0
y_valid, y_train = y_train_full[:VAL_SIZE], y_train_full[VAL_SIZE:]

# Перетворення 2D зображень у 1D вектори
x_train = x_train.reshape(-1, 28 * 28)
x_valid = x_valid.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

# Перетворення міток класів у one-hot encoding
y_train_one_hot = keras.utils.to_categorical(y_train, 10)
y_valid_one_hot = keras.utils.to_categorical(y_valid, 10)
y_test_one_hot = keras.utils.to_categorical(y_test, 10)

class_names = [
    'T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]


def create_model_relu():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(28*28,)),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def create_model_tanh():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(256, activation='tanh', input_shape=(28*28,)),
        tf.keras.layers.Dense(128, activation='tanh'),
        tf.keras.layers.Dense(64, activation='tanh'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def create_model_selu():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(384, activation='selu', input_shape=(28*28,)),
        tf.keras.layers.Dense(192, activation='selu'),
        tf.keras.layers.Dense(96, activation='selu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def train_and_plot(model, x_train, y_train, x_valid, y_valid, epochs=10):
    history = model.fit(x_train, y_train, epochs=epochs,
                        validation_data=(x_valid, y_valid),
                        batch_size=32, verbose=0)

    fig, ax = plt.subplots(figsize=(8, 5))
    pd.DataFrame(history.history).plot(ax=ax)
    ax.grid(True)
    ax.set_ylim(0, 1)

    val_loss, val_acc = model.evaluate(x_valid, y_valid, verbose=0)
    return fig, val_acc


st.title('Fashion MNIST Класифікатор')

model_choice = st.selectbox('Виберіть модель:',
                            ['ReLU', 'Tanh', 'New ReLU'])

if model_choice == 'ReLU':
    model = create_model_relu()
elif model_choice == 'Tanh':
    model = create_model_tanh()
else:
    model = create_model_selu()

epochs = st.slider('Виберіть кількість епох:', 1, 20, 10)

if st.button('Навчити модель'):
    with st.spinner('Навчання моделі...'):
        fig, val_acc = train_and_plot(model, x_train, y_train_one_hot,
                                      x_valid, y_valid_one_hot, epochs)
    st.pyplot(fig)
    st.write(f"Точність на валідаційних даних: {val_acc:.4f}")

st.subheader('Класифікація окремого зображення')
index = st.number_input('Введіть індекс зображення для класифікації (0-9999):',
                        min_value=0, max_value=9999, value=0, step=1)

if st.button('Класифікувати'):
    if 'model' in locals():
        image = x_test[index].reshape(1, -1)
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)

        st.image(x_test[index].reshape(28, 28),
                 caption='Вибране зображення', width=200)
        st.write(f'Прогноз: {class_names[predicted_class]}')
        st.write(f'Справжній клас: {class_names[y_test[index]]}')

        st.bar_chart(prediction[0])
    else:
        st.write('Спочатку навчіть модель!')
