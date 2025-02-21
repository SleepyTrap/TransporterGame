import pygame
from abc import ABC, abstractmethod
from gameObject import GameObject
from immovableObjects import ImmovableObject, Home, GasStation, Storage
from movableObjects import MovableObject, Truck, Helicopter

class GameMGMT:
    def __init__(self, params=None):
        """
        Initialize the game management class.
        """
        self.m_params = params
        pygame.init()
        self.m_screen = pygame.display.set_mode((1280, 720))
        self.m_clock = pygame.time.Clock()
        self.m_running = True
        self.m_lost = False
        self.m_won = False
        self.m_dt = 0
        self.m_win_condition = 80
        self.m_player = Truck(self.m_screen.get_width() / 2, self.m_screen.get_height() / 2, 500, 1, 20)
        self.m_heli = Helicopter(self.m_screen.get_width() - 100, 0, 210)
        self.m_home = Home(100, self.m_screen.get_height() / 2)
        self.m_gas_station = GasStation(self.m_screen.get_width() / 2, self.m_screen.get_height() - 150)
        self.m_storage = Storage(self.m_screen.get_width() - 100, self.m_screen.get_height() - 100)
        pygame.font.init()
        self.m_font = pygame.font.SysFont('Comic Sans MS', 20)
        self.m_big_font = pygame.font.SysFont('Comic Sans MS', 100)
        self.update_text()

    def update_text(self):
        """
        Update the on-screen text.
        """
        self.m_text = self.m_font.render(
            f'Fuel: {round(self.m_player.m_fuel)}, Player has Ore: {self.m_player.m_ore}, '
            f'Heli has Ore: {self.m_heli.m_ore}, Ore stored in Storage: {self.m_storage.m_ore_stored}, '
            f'Ore stored in Home: {self.m_home.m_ore_stored}, Ore stolen by Heli: {self.m_heli.m_ore_stolen}', False, (0, 0, 0)
        )

    def start_game(self):
        """
        Start the game.
        """
        self.run_game()

    def end_game(self):
        """
        End the game.
        """
        self.m_running = False

    def handle_collisions(self):
        """
        Handle collisions between the player and other objects.
        """
        if self.m_player.m_rect.colliderect(self.m_gas_station.m_rect):
            self.m_player.refuel()

        if self.m_player.m_rect.colliderect(self.m_home.m_rect) and not self.m_player.m_ore:
            self.m_player.withdraw_ore()
            self.m_home.store_ore(self.m_player.m_capacity)

        if self.m_player.m_ore:
            if self.m_player.m_rect.colliderect(self.m_storage.m_rect):
                self.m_storage.store_ore(self.m_player.m_capacity)
                self.m_player.deposit_ore()

            if self.m_player.m_rect.colliderect(self.m_heli.m_rect) and not self.m_heli.m_ore:
                self.m_heli.steal_ore(self.m_player.m_capacity)
                self.m_player.deposit_ore()

    def check_win_loss_conditions(self):
        """
        Check if the player has won or lost the game.
        """
        if self.m_storage.m_ore_stored >= self.m_win_condition:
            self.m_won = True
            self.end_game()

        if self.m_heli.m_ore_stolen > 100 - self.m_win_condition:
            self.m_lost = True
            self.end_game()

    def run_game(self):
        """
        Main game loop.
        """
        while self.m_running and not self.m_lost:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()

            self.m_screen.fill("white")

            if self.m_player.move(self.m_dt):
                self.end_game()
                self.m_lost = True

            self.m_heli.move(self.m_dt, self.m_player.m_pos_x, self.m_player.m_pos_y)

            self.m_player.draw(self.m_screen)
            self.m_heli.draw(self.m_screen)
            self.m_home.draw(self.m_screen)
            self.m_gas_station.draw(self.m_screen)
            self.m_storage.draw(self.m_screen)

            self.handle_collisions()
            self.check_win_loss_conditions()
            self.update_text()

            self.m_screen.blit(self.m_text, (0, 0))

            self.m_dt = self.m_clock.tick(60) / 1000

            pygame.display.flip()

        self.display_end_message()

    def display_end_message(self):
        """
        Display the end game message.
        """
        while self.m_lost or self.m_won:
            self.m_screen.fill("white")
            message = 'You lost!' if self.m_lost else 'You won!'
            self.m_big_text = self.m_big_font.render(message, False, (0, 0, 0))
            self.m_screen.blit(self.m_big_text, (self.m_screen.get_width() / 2, self.m_screen.get_height() / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.m_lost = False
                    self.m_won = False
                    self.end_game()