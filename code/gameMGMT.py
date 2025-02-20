import pygame
from abc import ABC, abstractmethod
from gameObject import gameObject
from immovableObjects import immovableObject
from immovableObjects import home
from immovableObjects import gasStation
from immovableObjects import storage
from movableObjects import movableObject
from movableObjects import truck
from movableObjects import helicopter
class gameMGMT():
    m_params = None #array of parameters
    m_screen = pygame.display.set_mode((1280, 720))
    m_clock = pygame.time.Clock()
    m_running = True
    m_dt = 0
    m_player = truck(m_screen.get_width()/2,m_screen.get_height()/2,200,1,100)
    m_heli = helicopter(m_screen.get_width()-100,0,210)
    m_home = home(100,m_screen.get_height()/2)
    m_gas_station = gasStation(m_screen.get_width()/2,m_screen.get_height()-150)
    m_storage = storage(m_screen.get_width()-100,m_screen.get_height()-100)

   # def __init__(self, params):
    #    self.m_params = params
     #   pygame.init()
    
    def __init__(self):
        pygame.init()

    def startGame():
        pass #TODO implement

    def endGame():
        pass #TODO implement

    def runGame(self):
        while self.m_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.m_running = False

            self.m_screen.fill("white")

            self.m_player.move(self.m_dt)
            self.m_heli.move(self.m_dt, self.m_player.m_pos_x, self.m_player.m_pos_y)


            self.m_player.draw(self.m_screen)
            self.m_heli.draw(self.m_screen)
            self.m_home.draw(self.m_screen)
            self.m_gas_station.draw(self.m_screen)
            self.m_storage.draw(self.m_screen)

            self.m_dt = self.m_clock.tick(60) / 1000


            
            pygame.display.flip()
            pygame.display.update()
