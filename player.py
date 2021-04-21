import os
import pygame

from math import floor as round_down
from draw import blitRotateCenter, win, FLOOR


running_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("Assets/runningman", "Run " + str(x) + ".png")))
                  for x in range(1, 11)]


def create_player():  # create new player object
    player = Player(x=0, y=0, imgs=running_images)
    return player


class Player:
    """
    Player class representing the player
    """

    def __init__(self, x, y, imgs):
        """
        :param x: starting x position
        :param y: starting y position
        :param imgs: sprites used for the animations
        """
        self.x = x
        self.y = y
        self.imgs = imgs
        self.tick = 0.0
        self.velocity = 0
        self.acceleration = 1
        self.jumpCount = 2
        self.rect = pygame.Rect(x, y, 100, 100)

    def draw(self):  # draw player, increase tick to cycle through running images
        if self.tick > 10:
            self.tick = 0

        rounded = int(round_down(self.tick))
        blitRotateCenter(win, self.imgs[rounded], (self.x, self.y), 0)

        self.tick += 0.2

    def move(self):  # move player
        if (self.y + self.velocity) > FLOOR:  # landing after a jump
            self.y = FLOOR
            self.velocity = 0
            self.jumpCount = 2

        else:
            self.y += self.velocity
            self.velocity += 2

        self.rect.update(self.x, self.y, 100, 100)

    def jump(self):  # set player moving upwards with
        if self.jumpCount > 0:
            self.velocity = -20
            self.jumpCount -= 1
