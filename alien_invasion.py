# Импортирование модуля sys (завершает игру по команде игрока).
import sys

# Импортирование модуля pygame (содержит функциональность, необходимую для создания игры.)
import pygame

from settings import Settings
from ship import Ship

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

        self.ship = Ship(self)

    def run_game(self):
        """Запускает основной цикл игры."""
        # Цикл while содержит цикл событий и код, управляющий обновлениями экрана.
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        # При каждом проходе цикла перерисовывется экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        # Отражение последнего прорисованного экрана.
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()