class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует статические настройки игры."""
        self.screen_width = 1920  # 1920, 1000 (800, 600)
        self.screen_height = 1000
        self.bg_color = (0, 0, 255)  # 230, 230, 230  0, 0, 255
        self.ship_speed = 3  # Настройки корабля
        self.ship_limit = 3
        self.bullet_speed = 8  # Параметры снаряда
        self.bullet_width = 5  # 5 300 (3000!)
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 1.5  # Настройки пришельцев (50)
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1  # Темп ускорения игры
        self.score_scale = 1.5  # Темп роста стоимости пришельцев
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1  # fleet_direction = 1  # обозначает движение вправо; а -1 - влево
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)







