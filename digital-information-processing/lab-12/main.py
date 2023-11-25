import cv2

jpg_image = cv2.imread('background.jpg')
png_image = cv2.imread('marker.png', cv2.IMREAD_UNCHANGED)

# Отримуємо розміри основного та наложеного зображень
height, width, _ = jpg_image.shape
overlay_height, overlay_width, _ = png_image.shape

# Обчислюємо позицію для наложення
x_position = int((width - overlay_width) / 2)
y_position = int((height - overlay_height) / 2)

# Налаштовуємо розмір та позицію наложеного зображення
roi = jpg_image[y_position:y_position + overlay_height, x_position:x_position + overlay_width]

# Створюємо маску для альфа-каналу
alpha_channel = png_image[:, :, 3] / 255.0

# Налаштовуємо наложення
for c in range(0, 3):
    jpg_image[y_position:y_position + overlay_height, x_position:x_position + overlay_width, c] = \
        (1 - alpha_channel) * jpg_image[y_position:y_position + overlay_height, x_position:x_position + overlay_width, c] + \
        alpha_channel * png_image[:, :, c]

# Зберігаємо результат
cv2.imwrite('output_image.jpg', jpg_image)