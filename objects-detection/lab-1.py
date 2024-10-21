import cv2
import numpy as np
import matplotlib.pyplot as plt

# Завантажуємо зображення
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Функція для показу зображення
def show_image(title, img):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.show()

# Фільтр розмиття (Gaussian Blur)
def apply_gaussian_blur(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

# Фільтр покращення чіткості зображення (Sharpen)
def apply_sharpen(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

# Медіанний фільтр
def apply_median_filter(image):
    median_image = cv2.medianBlur(image, 3)
    return median_image

# Фільтр Ґабора
def apply_gabor_filter(image):
    kernel = cv2.getGaborKernel((21, 21), 8.0, np.pi / 4, 10.0, 0.5, 0, ktype=cv2.CV_32F)
    gabor_image = cv2.filter2D(image, -1, kernel)
    return gabor_image

# Застосовуємо фільтри
blurred_image = apply_gaussian_blur(image)
sharpened_image = apply_sharpen(image)
median_image = apply_median_filter(image)
gabor_image = apply_gabor_filter(image)

# Виводимо результати
show_image('Original Image', image)
show_image('Gaussian Blur', blurred_image)
show_image('Sharpened Image', sharpened_image)
show_image('Median Filter', median_image)
show_image('Gabor Filter', gabor_image)

