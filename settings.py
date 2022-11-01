class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 800  # 1920, 750 (800, 600)
        self.screen_height = 600
        self.bg_color = (0, 0, 255)  # 230, 230, 230
        self.ship_speed = 1.5

