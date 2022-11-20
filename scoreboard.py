import pygame.font


class Scoreboard:
    """Класс для вывода игровой информации."""
    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчета очкой."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)  # Настройка шрифта для вывода счета
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()  # Подготовка исходного изображения
        self.prep_high_score()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()  # Вывод счета в правой верхней части экрана
        self.score_rect.right = self.score_rect.right
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = ":,".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect_centerx = self.score_rect.centerx
        self.high_score_rect_top = self.score_rect.top





