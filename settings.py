class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 800  # 1920, 750 (800, 600)
        self.screen_height = 600
        self.bg_color = (0, 0, 255)  # 230, 230, 230
        self.ship_speed = 1.5
        self.bullet_speed = 3  # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

