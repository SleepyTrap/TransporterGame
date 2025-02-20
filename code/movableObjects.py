import pygame  
from abc import ABC, abstractmethod
from gameObject import gameObject

class movableObject(gameObject):
    m_speed = 0
    m_ore = False
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
    def withdrawOre(self):
        pass

    @abstractmethod
    def depositOre(self):
        pass

class truck(movableObject):
    m_capacity = 5 # 5 units of ore
    m_fuel = 100 # 100% fuel
    m_consumption = 100 # 100% consumption /second 

    def __init__(self, pos_x, pos_y, speed, consumption, capacity):
        super().__init__(pos_x, pos_y, speed)
        self.m_consumption = consumption
        self.m_capacity = capacity
        self.set_image()
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def move(self, dt):
        if self.m_fuel > 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.m_pos_y -= self.m_speed * dt
                self.consumeFuel(dt)
            if keys[pygame.K_s]:
                self.m_pos_y += self.m_speed * dt
                self.consumeFuel(dt)
            if keys[pygame.K_a]:
                self.m_pos_x -= self.m_speed * dt
                self.consumeFuel(dt)
            if keys[pygame.K_d]:
                self.m_pos_x += self.m_speed * dt
                self.consumeFuel(dt)
            self.m_rect.center = (self.m_pos_x, self.m_pos_y)
        else:
            return True

    def set_image(self):
        self.m_image = pygame.image.load("./imgs/truck.png")

    def draw(self, screen):
        screen.blit(self.m_image, self.m_rect.topleft)

    def consumeFuel(self,dt):     
        self.m_fuel -= self.m_consumption * dt

    def withdrawOre(self):
        self.m_ore = True

    def depositOre(self):
        self.m_ore = False

    def refuel(self):
        self.m_fuel = 100

class helicopter(movableObject):
    
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, speed)
        self.set_image()
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))
        self.m_wait_timer = 0  # Timer for waiting
        self.m_oreStolen = 0 # Ore stolen from the truck

    def move(self, dt, truck_pos_x, truck_pos_y):
        if self.m_ore:
            if self.m_pos_y > -self.m_rect.height:
                self.m_pos_y -= self.m_speed * dt
            else:
                self.m_wait_timer += dt
                if self.m_wait_timer >= 30:  # Wait for 30 seconds
                    self.m_ore = False
                    self.m_wait_timer = 0
                    self.m_pos_y = 0  # Reset position to re-enter the screen
        else:
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

    def stealOre(self, amount):
        self.m_ore = True
        self.m_oreStolen += amount

    def depositOre(self):
        pass

    def withdrawOre(self):
        pass