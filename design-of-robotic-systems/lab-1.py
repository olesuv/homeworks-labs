import numpy as np

class Robot:
    def __init__(self, world, P, S, possible_moves=None):
        """
        Ініціалізація робота
        world: numpy array - карта світу (R і G)
        P: float - ймовірність правильного визначення кольору
        S: float - ймовірність руху на 1 клітинку
        possible_moves: dict - словник можливих рухів
        """
        self.world = np.array(world)
        self.height, self.width = self.world.shape
        self.P = P
        self.S = S
        
        # Ініціалізація рівномірного розподілу ймовірностей
        self.probability = np.ones((self.height, self.width)) / (self.height * self.width)
        
        # Визначення можливих рухів
        if possible_moves is None:
            self.possible_moves = {
                'L': (0, -1),
                'R': (0, 1),
                'U': (-1, 0),
                'D': (1, 0)
            }
        else:
            self.possible_moves = possible_moves

    def normalize(self):
        """Нормалізація розподілу ймовірностей"""
        self.probability = self.probability / np.sum(self.probability)

    def scan(self, observed_color):
        """
        Оновлення ймовірностей на основі спостереження
        observed_color: str - колір, який спостерігається ('R' або 'G')
        """
        for i in range(self.height):
            for j in range(self.width):
                # Якщо спостереження співпадає з реальним кольором
                if self.world[i, j] == observed_color:
                    self.probability[i, j] *= self.P
                else:
                    self.probability[i, j] *= (1 - self.P)
        
        self.normalize()

    def move(self, direction):
        """
        Моделювання руху робота
        direction: str - напрямок руху ('L', 'R', 'U', 'D')
        """
        new_prob = np.zeros_like(self.probability)
        
        for i in range(self.height):
            for j in range(self.width):
                if self.probability[i, j] > 0:
                    # Ймовірність залишитися на місці
                    new_prob[i, j] += self.probability[i, j] * (1 - self.S)
                    
                    # Рух на 1 клітинку
                    di, dj = self.possible_moves[direction]
                    new_i = (i + di) % self.height  # Тороїдальна топологія
                    new_j = (j + dj) % self.width
                    new_prob[new_i, new_j] += self.probability[i, j] * self.S
        
        self.probability = new_prob
        self.normalize()

    def process_path(self, path, observations):
        """
        Обробка повного шляху та спостережень
        path: str - послідовність рухів
        observations: str - послідовність спостережень
        """
        # Початкове сканування
        self.scan(observations[0])
        
        # Обробка кожного кроку
        for move, obs in zip(path[1:], observations[1:]):
            self.move(move)
            self.scan(obs)
        
        return self.probability

def main():
    # Визначення світу
    world = [
        ['R', 'G', 'R', 'G', 'G', 'R', 'G'],
        ['R', 'G', 'G', 'G', 'R', 'R', 'G'],
        ['G', 'R', 'G', 'R', 'R', 'G', 'R'],
        ['R', 'G', 'R', 'G', 'R', 'R', 'R']
    ]
    
    # Параметри завдання
    P = 0.65  # Точність сканування
    S = 0.7   # Ймовірність руху
    path = "DDLURRLU"
    observations = "GGRGRGGGG"
    
    # Створення та запуск робота
    robot = Robot(world, P, S)
    final_probabilities = robot.process_path(path, observations)
    
    # Виведення результату
    print("\nФінальний розподіл ймовірностей:")
    print(np.round(final_probabilities, 4))

if __name__ == "__main__":
    main()

