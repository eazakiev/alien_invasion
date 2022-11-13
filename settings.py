class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 800  # 1920, 750 (800, 600)
        self.screen_height = 600
        self.bg_color = (0, 0, 255)  # 230, 230, 230
        self.ship_speed = 3  # Настройки корабля
        self.ship_limit = 3
        self.bullet_speed = 8  # Параметры снаряда
        self.bullet_width = 5  # 5 300 (3000!)
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 1.5  # Настройки пришельцев (50)
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet_direction = 1 обозначает движение вправо; а -1 - влево



