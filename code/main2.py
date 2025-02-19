import pygame
from abc import ABC, abstractmethod

class gameObject(ABC):
    m_pos_x = 0
    m_pos_y = 0
    m_image = pygame.image.load('placeholder.png')

    def __init__(self, pos_x, pos_y):
        self.m_pos_x = pos_x
        self.m_pos_y = pos_y
    
    @abstractmethod
    def set_image(self):
        pass

    def draw(screen, self):
        screen.blit(self.m_image,(self.m_pos_x, self.m_pos_y))

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

class immovableObject(gameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    @abstractmethod
    def set_image(self, image):
        pass

    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def onContact():
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
        self.set_image

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

    def set_image(self):
        self.m_image = pygame.image.load("truck.png")

    def draw(screen, self):
        screen.blit(self.m_image, (self.m_pos_x, self.m_pos_y))

    def depositOre():
        pass #TODO implement

    def refuel():
        pass #TODO implement

class helicopter(movableObject):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, speed)
        self.set_image()
    
    def move(self, dt, truck_pos_x, truck_pos_y):
        if self.m_pos_x < truck_pos_x:
            self._pos_x += self.m_speed * dt
        if self._pos_x > truck_pos_x:
            self._pos_x -= self.m_speed * dt
        if self._pos_y < truck_pos_y:
            self._pos_y += self.m_speed * dt
        if self._pos_y > truck_pos_y:
            self._pos_y -= self.m_speed * dt

    def set_image(self):
        self.m_image = pygame.image.load("helicopter.png")

    def draw(screen, self):
        screen.blit(self.m_image, (self.m_pos_x, self.m_pos_y))
    
    def depositOre():
        pass #TODO implement

    def stealOre():
        pass #TODO implement

    def disappear():
        pass #TODO implement

class home(immovableObject):
    m_capacity = 100
    
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load("home.png")

    def draw(screen, self):
        screen.blit(self.m_image, (self.m_pos_x, self.m_pos_y))

    def onContact():
        pass #TODO implement

class gasStation(immovableObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image

    def set_image(self):
        self.m_image = pygame.image.load("gas_station.png")

    def draw(screen, self):
        screen.blit(self.m_image, (self.m_pos_x, self.m_pos_y))

    def onContact():
        pass #TODO implement

class storage(immovableObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.set_image()

    def set_image(self):
        self.m_image = pygame.image.load("storage.png")

    def draw(screen, self):
        screen.blit(self.m_image, (self.m_pos_x, self.m_pos_y))

    def onContact():
        pass #TODO implement

class gameMGMT():
    m_params = None #array of parameters
    m_screen = pygame.display.set_mode((1280, 720))
    m_clock = pygame.time.Clock()
    m_running = True
    m_dt = 0
    m_player = truck(m_screen.get_width()/2,m_screen.get_height()/2,200,1,100)
    m_heli = helicopter(m_screen.get_width()-100,0,210)
    m_home = home(0,m_screen.get_height()/2)
    m_gas_station = gasStation(m_screen.get_width()/2,m_screen.get_height-150)
    m_storage = storage(m_screen.get_width()-100,m_screen.get_height()-100)

    def __init__(self, params):
        self.m_params = params
        pygame.init()

    def startGame():
        pass #TODO implement

    def endGame():
        pass #TODO implement

    def runGame():
        pass #TODO implement