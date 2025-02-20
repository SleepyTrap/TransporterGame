import pygame  
from abc import ABC, abstractmethod
from gameObject import gameObject
class movableObject(gameObject):
    m_speed = 0

    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y)
        self.m_speed = speed

    @abstractmethod
    def move(self, dt):
        pass

    @abstractmethod
    def set_image(self, image):
        pass

    @abstractmethod
    def depositOre():
        pass

class truck(movableObject):
    m_capacity = 0
    m_ore = False
    m_fuel = 100 #100% fuel
    m_consumption = 0.1 #10% fuel consumption per second
    


    def __init__(self, pos_x, pos_y, speed, consumption, capacity):
        super().__init__(pos_x, pos_y, speed)
        self.m_consumption = consumption
        self.m_capacity = capacity
        self.set_image()
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.m_pos_y -= self.m_speed * dt
        if keys[pygame.K_s]:
            self.m_pos_y += self.m_speed * dt
        if keys[pygame.K_a]:
            self.m_pos_x -= self.m_speed * dt
        if keys[pygame.K_d]:
            self.m_pos_x += self.m_speed * dt
        self.m_rect.center = (self.m_pos_x, self.m_pos_y)

    def set_image(self):
        self.m_image = pygame.image.load("./imgs/truck.png")

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def depositOre():
        pass #TODO implement

    def refuel():
        pass #TODO implement

class helicopter(movableObject):
    
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, speed)
        self.set_image()
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))
    
    def move(self, dt, truck_pos_x, truck_pos_y):
        if self.m_pos_x < truck_pos_x:
            self.m_pos_x += self.m_speed * dt
        if self.m_pos_x > truck_pos_x:
            self.m_pos_x -= self.m_speed * dt
        if self.m_pos_y < truck_pos_y:
            self.m_pos_y += self.m_speed * dt
        if self.m_pos_y > truck_pos_y:
            self.m_pos_y -= self.m_speed * dt
        self.m_rect.center = (self.m_pos_x, self.m_pos_y)


    def set_image(self):
        self.m_image = pygame.image.load("./imgs/helicopter.png")

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)
    
    def depositOre():
        pass #TODO implement

    def stealOre():
        pass #TODO implement

    def disappear():
        pass #TODO implement