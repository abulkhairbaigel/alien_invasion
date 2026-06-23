class Settings:
    """Класс для хранения всех настроек игры "Инопланетное вторжение"."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля.
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Параметры снаряда.
        self.bullet_speed = 6.5
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настроки пришельца.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а и -1 - влево.
        self.fleet_direction = 1