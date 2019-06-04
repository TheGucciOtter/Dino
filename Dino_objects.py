import pygame
from pygame.math import Vector2

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position

        self.image = pygame.image.load('big chungus.png')
        self.image = pygame.transform.scale(self.image, (90,174))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

        self.jumping = False
        self.velocity = Vector2(0,0)
        self.gravity = Vector2(0, 9 / 16)

    def update(self):
        if self.jumping:
            self.velocity += self.gravity
        else:
            self.velocity = Vector2(0,0)
        self.position += self.velocity
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def kill(self):
        pygame.sprite.Sprite.kill(self)
        self.position = Vector2(-10000,-1000)
        self.speed = Vector2(0,0)

class Ground(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(10,0)

        self.image = pygame.image.load('ground.jpg')
        self.image = pygame.transform.scale(self.image, (1200,260))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self):
        self.position -= self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def kill(self):
        pygame.sprite.Sprite.kill(self)
        self.position = Vector2(-300,-1000)
        self.speed = Vector2(0,0)

    def setposition(self, pos):
        self.position = pos
        self.rect.x = self.position.x
        self.rect.y = self.position.y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position, obstacle_image, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(10,0)

        self.image = pygame.image.load(obstacle_image)
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()

    def update(self):
        self.position -= self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y


    def kill(self):
        pygame.sprite.Sprite.kill(self)
        self.position = Vector2(-10000,-1000)
        self.speed = Vector2(0,0)
