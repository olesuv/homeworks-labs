#include <Arduino.h>

const int PWM_FREQ = 800;          // Частота ШІМ
const int PWM_RESOLUTION = 8;      // Роздільна здатність 8 біт
const int MAX_DUTY_CYCLE = 255;    // Максимальний робочий цикл для 8 біт (0-255)
const int LED1_PIN = 18;           // Вивід GPIO для LED1
const int LED2_PIN = 19;           // Вивід GPIO для LED2
const int LED3_PIN = 21;           // Вивід GPIO для LED3
const int DELAY_MS = 12;           // Затримка для плавного ефекту

void setup() {
    // Налаштовуємо ШІМ для кожного LED
    ledcAttachPin(LED1_PIN, 0);
    ledcSetup(0, PWM_FREQ, PWM_RESOLUTION);
    
    ledcAttachPin(LED2_PIN, 1);
    ledcSetup(1, PWM_FREQ, PWM_RESOLUTION);
    
    ledcAttachPin(LED3_PIN, 2);
    ledcSetup(2, PWM_FREQ, PWM_RESOLUTION);
}

void fadeLed(int channel, int duration) {
    int steps = duration / (2 * DELAY_MS);  // Розрахунок кроків для загасання/засвічування
    for (int dutyCycle = 0; dutyCycle <= MAX_DUTY_CYCLE; dutyCycle += MAX_DUTY_CYCLE / steps) {
        ledcWrite(channel, dutyCycle);
        delay(DELAY_MS);
    }
    for (int dutyCycle = MAX_DUTY_CYCLE; dutyCycle >= 0; dutyCycle -= MAX_DUTY_CYCLE / steps) {
        ledcWrite(channel, dutyCycle);
        delay(DELAY_MS);
    }
}

void loop() {
    fadeLed(0, 3000);  // Засвічення та загасання LED1 протягом 3 секунд
    fadeLed(1, 3000);  // Засвічення та загасання LED2 протягом 3 секунд
    fadeLed(2, 3000);  // Засвічення та загасання LED3 протягом 3 секунд
}

