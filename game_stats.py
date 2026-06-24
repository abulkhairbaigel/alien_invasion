class GameStats:
    """Отслеживает статистику для игры "Инопланетное вторжение"."""
        
    def __init__(self, ai_game):
        """Иниициализирует статистику."""
        self.settings = ai_game.settings
        # На все время работы игры будет создаваться один экзмепляр GameStats.
        # Но часть статистики должна сбрасываться в начале каждой новой игры.
        # Для этого большая часть статистики инициализируется в методе reset_stats() вместо __init__():
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0