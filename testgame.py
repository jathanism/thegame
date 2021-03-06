# testgame.py - Simple PyGame game

import pygame
import sys

from pygame.locals import *



def set_background(screen, color=(0, 0, 0)):
    '''Takes a screen, returns a surface.'''
    background = pygame.Surface(screen.get_size())
    background.fill(color)
    background = background.convert()
    screen.blit(background, (0, 0))
    return background

# This will create a white square to be used as the main character
def create_test_shape(size=(32, 32), color=(255, 255, 255)):
    '''
    Create a surface object to use in place of real images.

    Returns a surface.
    '''
    surface = pygame.Surface(size)
    surface.fill(color)
    surface = surface.convert()
    return surface

MOVEMENTS = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
}

class MainCharacter(pygame.sprite.Sprite):
    """
    The main character of the game.

    Attributes:

    :pos:
        Position on the screen
    :image:
        Surface object representing player
    :rect:
        Rectangle of the main character
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [0, 0]
        self.image = create_test_shape()
        self.rect = self.image.get_rect()
        self.size = self.rect.size

    def update(self):
        self.rect.topleft = self.pos

    def move_char(self, keys_pressed, rect):
        """
        For each key that is currently pressed down, move the rectangle of the
        player in the right direction.
        """
        pixels = 2

        for key, vector in MOVEMENTS.iteritems():
            if keys_pressed[key]:
                print "GOT KEY", key
                x, y = vector
                self.pos[0] += x * pixels
                self.pos[1] += y * pixels
        self.rect.move(self.pos)
        self.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    background = set_background(screen)
    player = MainCharacter()
    allsprites = pygame.sprite.RenderPlain((player))

    pygame.key.set_repeat(250, 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

            print event
            if event.type == KEYDOWN:
                player.move_char(pygame.key.get_pressed(),
                                 background.get_rect())

            #if len(KEYSPRESSED):
            #    player.move_char(KEYSPRESSED, background.get_rect())
            allsprites.update()
            screen.blit(background, (0, 0))
            allsprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    main()
