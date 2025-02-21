import pygame
from abc import ABC, abstractmethod

class GameObject(ABC):
    """
    Abstract base class for all game objects.
    """
    def __init__(self, pos_x, pos_y):
        """
        Initialize the game object with a position.
        """
        self.m_pos_x = pos_x
        self.m_pos_y = pos_y
        self.m_image = pygame.image.load('./imgs/placeholder.png')
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    @abstractmethod
    def set_image(self):
        """
        Abstract method to set the image of the game object.
        """
        pass

    def draw(self, screen):
        """
        Draw the game object on the screen.
        """
        screen.blit(self.m_image, self.m_rect.topleft)