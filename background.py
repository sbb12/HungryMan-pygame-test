import pygame
import os

from draw import win, WIDTH, HEIGHT

BG_IMG1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "parallax-forest-front-trees.png")), (WIDTH*2, HEIGHT))
BG_IMG2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "parallax-forest-middle-trees.png")), (WIDTH*2, HEIGHT))
BG_IMG3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "parallax-forest-lights.png")), (WIDTH*2, HEIGHT))
BG_IMG4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "parallax-forest-back-trees.png")), (WIDTH*2, HEIGHT))


def create_background(bg1=BG_IMG1, bg2=BG_IMG2, bg3=BG_IMG3, bg4=BG_IMG4):  # create background object from images.
    return Background(bg1, bg2, bg3, bg4)


class Background:
    """
    Background class containing different layers of the background
    """

    def __init__(self, bg1, bg2, bg3, bg4):
        """
        :param bg1: foremost img of background
        :param bg2: second layer image
        :param bg3: third layer image
        :param bg4: furthest layer image
        """
        self.bg1 = bg1
        self.bg2 = bg2
        self.bg3 = bg3
        self.bg4 = bg4

        self.pos1 = 0
        self.pos2 = 0
        self.pos3 = 0
        self.pos4 = 0

    def tick(self):  # move the background layers
        self.pos1 -= 1
        if self.pos1 <= -WIDTH:
            self.pos1 += WIDTH
        self.pos2 -= 2
        if self.pos2 <= -WIDTH:
            self.pos2 += WIDTH
        self.pos3 -= 3
        if self.pos3 <= -WIDTH:
            self.pos3 += WIDTH
        self.pos4 -= 4
        if self.pos4 <= -WIDTH:
            self.pos4 += WIDTH

    def draw(self):  # draw background layers
        win.blit(self.bg4, (self.pos1, 0))
        win.blit(self.bg3, (self.pos2, 0))
        win.blit(self.bg2, (self.pos3, 0))
        win.blit(self.bg1, (self.pos4, 0))
        self.tick()
