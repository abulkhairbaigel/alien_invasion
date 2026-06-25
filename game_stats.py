from pathlib import Path
import json

class GameStats:
    """Отслеживает статистику для игры "Инопланетное вторжение"."""
        
    def __init__(self, ai_game):
        """Иниициализирует статистику."""
        self.settings = ai_game.settings
        # На все время работы игры будет создаваться один экзмепляр GameStats.
        # Но часть статистики должна сбрасываться в начале каждой новой игры.
        # Для этого большая часть статистики инициализируется в методе reset_stats() вместо __init__():
        self.reset_stats()

        # Рекорд не должен сбрасываться.
        self.high_score = self.get_stored_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def get_stored_high_score(self):
        """Получает хранимое значение рекорда."""
        path = Path(r'C:\Users\admin\Desktop\alien_invasion\text_files\new_high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0