import sys
from time import sleep
import pygame

from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion (game for Ilya and David)')
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши."""
        for event in pygame.event.get():  # отслеживание событий клавиатуры и мыши
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Тип события нажать на клавишу
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # Тип события отпустить клавишу
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:  # Перемещение корабля вправо
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # Перемещение корабля влево
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()  # Обновление позиции снарядов
        for bullet in self.bullets.copy():  # Удаление снарядов, вышедших за край экрана
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:  # Уничтожение существующих снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()
        # print(len(self.bullets))

    def _update_aliens(self):
        """
        Проверяет, достиг ли флот края экрана,
        с последующим обновлением позиции всех пришельцев во флоте.
        """
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()  # Проверка, добрались ли пришельцы до нижнего края экрана

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()  # Очистка списков пришельцев и снарядов
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()  # Создание нового флота и размещение корабля в центре
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)  # При каждом проходе цикла перерисовывается экран (заполняется)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """Создание флота вторжения."""
        alien = Alien(self)  # Создание пришельца и вычисление кол-ва пришельцев в ряду
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)  # Интервал между соседними пришельцами
        number_aliens_x = available_space_x // (2 * alien_width)  # равен ширине пришельца
        ship_height = self.ship.rect.height  # Определяет кол-во рядов, помещающихся на экране
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)  # 2
        for row_number in range(number_rows):  # Создание флота вторжения
            for alien_number in range(number_aliens_x):  # Создание первого ряда пришельцев
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)  # Создание пришельца и размещение его в ряду
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':  # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
