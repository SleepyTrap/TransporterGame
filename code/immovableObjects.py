import pygame
from abc import ABC, abstractmethod
from gameObject import GameObject

class ImmovableObject(GameObject):
    """
    Abstract base class for all immovable objects.
    """
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    @abstractmethod
    def set_image(self):
        """
        Abstract method to set the image of the object.
        """
        pass

    @abstractmethod
    def draw(self, screen):
        """
        Abstract method to draw the object on the screen.
        """
        pass



class Home(ImmovableObject):
    """
    Class representing the home.
    """
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.m_ore_stored = 100
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load(".\\imgs\\home.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def store_ore(self, amount):
        self.m_ore_stored -= amount

class GasStation(ImmovableObject):
    """
    Class representing the gas station.
    """
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load(".\\imgs\\gas_station.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

class Storage(ImmovableObject):
    """
    Class representing the storage.
    """
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.m_ore_stored = 0
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load(".\\imgs\\storage.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def store_ore(self, amount):
        self.m_ore_stored += amount

