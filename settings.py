class Settings:
    """Класс для хранения всех настроек игры "Инопланетное вторжение"."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля.
        self.ship_speed = 3.5

        # Параметры снаряда.
        self.bullet_speed = 7.0
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (214, 94, 0)
        self.bullets_allowed = 4