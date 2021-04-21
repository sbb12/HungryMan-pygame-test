import pygame
import random

import draw
from player import create_player
from food import FOODS, create_food
from background import create_background
from draw import clock, draw_window


def check_collision():  # update game objects

    for food in foods:
        if food.x < -30:
            foods.remove(food)
        if food.rect.colliderect(players[0].rect):
            food.sound_eat()
            draw.score += 1
            foods.remove(food)


foods = []
foods.append(create_food())
players = [create_player()]
bg = create_background()

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 17)


def main():  # main game loop

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    players[0].jump()

            if random.random() > 0.95:
                foods.append(create_food())

        clock.tick(60)
        check_collision()

        draw_window(players, foods, bg)


if __name__ == "__main__":
    main()

pygame.quit()
