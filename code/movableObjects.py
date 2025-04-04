import pygame
from abc import ABC, abstractmethod
from gameObject import GameObject

class MovableObject(GameObject):
    """
    Abstract base class for all movable objects.
    """
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y)
        self.m_speed = speed

    @abstractmethod
    def move(self, dt):
        """
        Abstract method to move the object.
        """
        pass

    @abstractmethod
    def set_image(self):
        """
        Abstract method to set the image of the object.
        """
        pass

    @abstractmethod
    def withdraw_ore(self):
        """
        Abstract method to withdraw ore.
        """
        pass

    @abstractmethod
    def deposit_ore(self):
        """
        Abstract method to deposit ore.
        """
        pass

class Truck(MovableObject):
    """
    Class representing the truck.
    """
    def __init__(self, pos_x, pos_y, speed, consumption, capacity):
        super().__init__(pos_x, pos_y, speed)
        self.m_consumption = consumption
        self.m_capacity = capacity
        self.m_fuel = 100
        self.m_ore = False
        self.set_image()

    def move(self, dt):
        if self.m_fuel > 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.m_pos_y -= self.m_speed * dt
                self.consume_fuel(dt)
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.m_pos_y += self.m_speed * dt
                self.consume_fuel(dt)
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.m_pos_x -= self.m_speed * dt
                self.consume_fuel(dt)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.m_pos_x += self.m_speed * dt
                self.consume_fuel(dt)
            self.m_rect.center = (self.m_pos_x, self.m_pos_y)
        else:
            return True

    def set_image(self):
        self.m_image = pygame.image.load(".\\imgs\\truck.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def consume_fuel(self, dt):
        self.m_fuel -= self.m_consumption * dt

    def withdraw_ore(self):
        self.m_ore = True

    def deposit_ore(self):
        self.m_ore = False

    def refuel(self):
        self.m_fuel = 100

class Helicopter(MovableObject):
    """
    Class representing the helicopter.
    """
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, speed)
        self.m_ore_stolen = 0
        self.m_ore = False
        self.m_wait_timer = 0
        self.set_image()

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
        self.m_image = pygame.image.load(".\\imgs\\/helicopter.png")
        self.m_rect = self.m_image.get_rect(center=(self.m_pos_x, self.m_pos_y))

    def steal_ore(self, amount):
        self.m_ore = True
        self.m_ore_stolen += amount

    def deposit_ore(self):
        pass

    def withdraw_ore(self):
        pass