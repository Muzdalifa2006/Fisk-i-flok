import pygame
from vector import * 


fish_img = pygame.image.load('fish.png')
fish_img = pygame.transform.scale(fish_img, (50,50))
position = Vector(400, 300)
velocity = Vector(1,1)

class Fish: 

    def __init__(self, position, velocity, screen):
       self.position = position
       self.velocity = velocity
       self.screen = screen

    def update(self):
        self.position = self.position + self.velocity
        if self.position.x <= 0 or self.position.x >= self.screen.get_width():
            self.velocity.x = -self.velocity.x
        if self.position.y <= 0 or self.position.y >= self.screen.get_height():
            print(self.position.y)
            self.velocity.y = -self.velocity.y
            print(self.velocity.y)

    def draw(self, screen):
        screen.blit(fish_img, (self.position.x, self.position.y))



    
