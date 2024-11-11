const int buttonPin = 5;      // Номер виводу для кнопки
const int ledPins[] = {14, 15, 16, 17};  // Виводи для LED1, LED2, LED3, LED4
int buttonState = 0;          // Змінна для зчитування стану кнопки
int pressCount = 0;           // Лічильник натискань кнопки
float frequency = 0.75;       // Початкова частота засвічування в Гц

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT);
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    pressCount++;
    delay(300);  // Антидребезг кнопки

    if (pressCount == 1) {
      frequency *= 2;
    } else if (pressCount == 2) {
      frequency *= 2;
    } else if (pressCount >= 3) {
      frequency = 0.75;
      pressCount = 0;
    }
  }

  // Розрахунок затримки між засвічуванням для заданої частоти
  int delayTime = (int)(1000 / (frequency * 4));  // 4 світлодіоди

  // Біжучі вогні від LED1 до LED4
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], HIGH);
    delay(delayTime);
    digitalWrite(ledPins[i], LOW);
  }
}

