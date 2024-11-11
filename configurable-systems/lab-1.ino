// Визначаємо пін для вбудованого синього світлодіода
const int LED_PIN = 2;  // Синій світлодіод підключений до GPIO2

void setup() {
  // Налаштовуємо пін світлодіода як вихід
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Вмикаємо світлодіод
  digitalWrite(LED_PIN, HIGH);
  // Затримка 1 секунда
  delay(1000);
  
  // Вимикаємо світлодіод
  digitalWrite(LED_PIN, LOW);
  // Затримка 1 секунда
  delay(1000);
}

