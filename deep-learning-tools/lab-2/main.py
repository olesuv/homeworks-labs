import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras.utils import plot_model
import io

# Завантаження даних та підготовка
housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Завантаження збереженої моделі
@st.cache_resource
def load_saved_model():
    return keras.models.load_model('complex_model_auxiliary.keras')

model = load_saved_model()

# Функція для створення графіку втрат
def plot_loss(history):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(history['main_output_loss'], label='Train Loss (Main)')
    ax.plot(history['val_main_output_loss'], label='Validation Loss (Main)')
    ax.plot(history['auxiliary_output_loss'], label='Train Loss (Auxiliary)')
    ax.plot(history['val_auxiliary_output_loss'], label='Validation Loss (Auxiliary)')
    ax.set_title("Складна модель з допоміжним виходом - Графік втрат")
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.legend()
    return fig

# Streamlit app
st.title('Інтерактивна сторінка моделі прогнозування цін на житло в Каліфорнії')

# Виведення схеми моделі
st.header('Схема моделі')
buffer = io.StringIO()
model.summary(print_fn=lambda x: buffer.write(x + '\n'))
model_summary = buffer.getvalue()
st.text(model_summary)

# Виведення точності навчання моделі
st.header('Точність навчання моделі')
mse = model.evaluate(X_test_scaled, [y_test, y_test], verbose=0)
st.write(f"Середньоквадратична похибка на тестовому наборі (головний вихід): {mse[1]:.4f}")
st.write(f"Середньоквадратична похибка на тестовому наборі (допоміжний вихід): {mse[2]:.4f}")

# Графік зміни функції втрат
st.header('Графік зміни функції втрат')
history = np.load('model_history.npy', allow_pickle=True).item()
st.pyplot(plot_loss(history))

# Вибір елемента з тестового набору
st.header('Передбачення для обраного елемента')
index = st.number_input('Введіть індекс елемента з тестового набору (0-2919):', min_value=0, max_value=2919, value=0, step=1)

if st.button('Зробити передбачення'):
    sample = X_test_scaled[index].reshape(1, -1)
    prediction = model.predict(sample)
    st.write(f"Передбачене значення (головний вихід): {prediction[0][0][0]:.4f}")
    st.write(f"Передбачене значення (допоміжний вихід): {prediction[1][0][0]:.4f}")
    st.write(f"Фактичне значення: {y_test[index]:.4f}")

    # Виведення вхідних даних
    st.subheader('Вхідні дані для обраного елемента:')
    feature_names = housing.feature_names
    input_data = pd.DataFrame(X_test[index].reshape(1, -1), columns=feature_names)
    st.dataframe(input_data)

