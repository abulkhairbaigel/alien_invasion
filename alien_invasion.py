# Импортирование модуля sys (завершает игру по команде игрока).
import sys

# Импортирование модуля pygame (содержит функциональность, необходимую для создания игры.)
import pygame

from settings import Settings

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        # Функция pygame.init() инициализирует настройки, необходимые Pygame для нормальной работы.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Задание цвета фона.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Запускает основной цикл игры."""
        # Цикл while содержит цикл событий и код, управляющий обновлениями экрана.
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходе цикла перерисовывется экран.
            self.screen.fill(self.settings.bg_color)
            
            # Отражение последнего прорисованного экрана.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()