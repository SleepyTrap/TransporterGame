import pygame
from abc import ABC, abstractmethod
from gameObject import gameObject

class immovableObject(gameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    @abstractmethod
    def set_image(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

class home(immovableObject):
    m_ore_stored = 100

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load("./imgs/home.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def storeOre(self, amount):
        self.m_ore_stored -= amount

class gasStation(immovableObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load("./imgs/gas_station.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def onContact(self, truck_pos_x, truck_pos_y):
        pass #TODO implement

class storage(immovableObject):
    m_ore_stored = 0

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load("./imgs/storage.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def storeOre(self, amount):
        self.m_ore_stored += amount

    