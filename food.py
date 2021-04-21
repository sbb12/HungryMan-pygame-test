import pygame
import os
import random

from draw import blitRotateCenter, win, WIDTH

FOOD_WIDTH = 30
FOOD_HEIGHT = 30

VEL = 5

APPLE_IMG = pygame.image.load(os.path.join("Assets", "Apple.png"))
BANANA_IMG = pygame.image.load(os.path.join("Assets", "Banana.png"))
BURGER_IMG = pygame.image.load(os.path.join("Assets", "Burger.png"))
FRIES_IMG = pygame.image.load(os.path.join("Assets", "Fries.png"))
ICECREAM_IMG = pygame.image.load(os.path.join("Assets", "Icecream.png"))
DONUT_IMG = pygame.image.load(os.path.join("Assets", "Donut.png"))

food_imgs = [APPLE_IMG, BANANA_IMG, BURGER_IMG, FRIES_IMG, ICECREAM_IMG, DONUT_IMG]

EAT_SOUND = pygame.mixer.Sound("Assets/chew.mp3")

FOODS = []


def create_food():  # generates food objects
    food = Food(WIDTH + 30, random.randrange(200, 400, 1), random.choice(food_imgs))
    return food


class Food:
    """
    food class representing food items
    """

    def __init__(self, x, y, img):
        """
        :param x: starting x position
        :param y: starting y position
        :param img: image of the food item
        """

        self.x = x
        self.y = y
        self.img = img
        self.tilt = 0
        self.rotationspeed = random.randrange(1, 4)
        self.tick = 0
        self.rect = pygame.Rect(x, y, 30, 30)

    def draw(self):  # draw food object
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def move(self):  # move food object and its rect
        self.x -= VEL
        self.tick += 1
        self.rect.update(self.x, self.y, 30, 30)

    def rotate(self):  # rotate food object
        self.tilt += self.rotationspeed

    def sound_eat(self):  # play sound
        EAT_SOUND.play()
