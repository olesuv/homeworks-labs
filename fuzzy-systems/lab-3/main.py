import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the membership functions for "low person" and "high person"
height_range = np.arange(150, 201)
low_person = np.maximum(0, 1 - abs((height_range - 150) / 25))  # Corrected for "low person"
high_person = np.maximum(0, 1 - abs((height_range - 200) / 25))  # Corrected for "high person"

# Define the complement function
def complement(fuzzy_set):
    return 1 - fuzzy_set

# Set Seaborn style
sns.set(style="darkgrid")

# Create a Pandas DataFrame to work with Seaborn
data = {
    'Зріст (см)': height_range,
    'Низька людина': low_person,
    'Висока людина': high_person
}
df = pd.DataFrame(data)
print(df)

# Plot the membership functions
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Зріст (см)', y='Низька людина', label="Низька людина")
sns.lineplot(data=df, x='Зріст (см)', y='Висока людина', label="Висока людина")
plt.xlabel("Зріст (см)")
plt.ylabel("Функція приналежності")
plt.title("Функція приналежності для 'Низька людина' та 'Висока людина' ")
plt.legend(loc='upper right')
plt.grid(True)

# Operations on fuzzy sets
intersection = np.minimum(low_person, high_person)  # "Low and High Person"
union = np.maximum(low_person, high_person)  # "Low or High Person"
complement_high = complement(high_person)  # "Not High Person"
concentration_low = low_person ** 0.5  # "Slightly Low Person"
stretch_high = high_person ** 2  # "Very High Person"

# Plot the resulting membership functions
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Зріст (см)', y=intersection, label="Низька та Висока людина")
sns.lineplot(data=df, x='Зріст (см)', y=union, label="Низька або Висока людина")
sns.lineplot(data=df, x='Зріст (см)', y=complement_high, label="Не Висока людина")
sns.lineplot(data=df, x='Зріст (см)', y=concentration_low, label="Злегка Низька людина")
sns.lineplot(data=df, x='Зріст (см)', y=stretch_high, label="Дуже висока людина")
plt.xlabel("Зріст (см)")
plt.ylabel("Функція приналежності")
plt.title("Функції приналежності для визначених операторів")
plt.legend(loc='upper right')
plt.grid(True)

# Show the plots
plt.show()

# Verification of basic properties of operations
print("Перевірка основних властивостей операцій")
# Commutativity
print("Комутативність (A та B = B та A):", np.array_equal(intersection, np.minimum(high_person, low_person)))
# Associativity
A = low_person
B = high_person
C = union
D = np.maximum(np.maximum(low_person, high_person), union)
print("Асоціативність (A і (B та C) = (A і B) і C):", np.array_equal(np.minimum(A, np.minimum(B, C)), np.minimum(np.minimum(A, B), C)))
# Distributivity
print("Дистрибутивність (A і (B або C) = (A і B) або (A і C)):", np.array_equal(np.minimum(A, np.maximum(B, C)), np.maximum(np.minimum(A, B), np.minimum(A, C))))
# Involution
print("Інволюція:", np.array_equal(complement(complement(A)), A))
# De Morgan's Laws
print("Закони де Моргана:", np.array_equal(complement(union), np.minimum(complement(A), complement(B))))
