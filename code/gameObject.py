import pygame
from abc import ABC, abstractmethod

class gameObject(ABC):
    m_pos_x = 0
    m_pos_y = 0
    m_image = pygame.image.load('./imgs/placeholder.png')

    def __init__(self, pos_x, pos_y):
        self.m_pos_x = pos_x
        self.m_pos_y = pos_y
    
    @abstractmethod
    def set_image(self):
        pass

    def draw(screen, self):
        screen.blit(self.m_image,(self.m_pos_x, self.m_pos_y))