#define Button_GPIO  4   // Номер виводу ESP32, до якого підключена кнопка
#define LED1_GPIO    18  // Номер виводу ESP32, до якого підключений LED1
#define LED2_GPIO    19  // Номер виводу ESP32, до якого підключений LED2
#define LED3_GPIO    21  // Номер виводу ESP32, до якого підключений LED3

uint8_t buttonState = 0; // Змінна для відстежування стану натискань кнопки
bool pressed = false; // Змінна для відстежування натискання кнопки

// Змінні для відстежування часу між останніми перериваннями
unsigned long button_time = 0;  
unsigned long last_button_time = 0;  

void IRAM_ATTR Ext_INT1_ISR() 
{ 
    button_time = millis(); 
    if (button_time - last_button_time > 250) 
    { 
        buttonState++; 
        pressed = true; 
        last_button_time = button_time; 
    } 
} 

void setup()  
{ 
    Serial.begin(9600); 
    pinMode(Button_GPIO, INPUT); 
    pinMode(LED1_GPIO, OUTPUT); 
    pinMode(LED2_GPIO, OUTPUT); 
    pinMode(LED3_GPIO, OUTPUT); 
    attachInterrupt(Button_GPIO, Ext_INT1_ISR, RISING); 
} 

void loop()  
{ 
    if (pressed)  
    { 
        Serial.printf("Кількість натискань кнопки Button_GPIO: %u \n", buttonState); 
        // Реалізація логіки вмикання/вимикання LED
        switch (buttonState % 4) 
        { 
            case 1: // Перше натискання
                digitalWrite(LED1_GPIO, HIGH);
                digitalWrite(LED2_GPIO, LOW);
                digitalWrite(LED3_GPIO, LOW);
                break;
            case 2: // Друге натискання
                digitalWrite(LED1_GPIO, HIGH);
                digitalWrite(LED2_GPIO, HIGH);
                digitalWrite(LED3_GPIO, LOW);
                break;
            case 3: // Третє натискання
                digitalWrite(LED1_GPIO, HIGH);
                digitalWrite(LED2_GPIO, HIGH);
                digitalWrite(LED3_GPIO, HIGH);
                break;
            case 0: // Четверте натискання
                digitalWrite(LED1_GPIO, LOW);
                digitalWrite(LED2_GPIO, LOW);
                digitalWrite(LED3_GPIO, LOW);
                break;
        }
        pressed = false; 
    } 
}

