import pygame

FLOOR = 350
ROTATION_VEL = 20
WIDTH = 900
HEIGHT = 500

score = 0

# initialise pygame window
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
fps_font = pygame.font.SysFont("Arial", 18)
pygame.display.set_caption("The Game")


def blitRotateCenter(surf, image, topleft, angle):
    """
    :param surf: Surface to draw on
    :param image: image to draw
    :param topleft: (x, y) draw from top left corner
    :param angle: rotation angle of image
    :return: none
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)


def draw_window(players, foods, backgrounds):  # update game and draw objects
    """
    :param players: the player to draw
    :param foods: list of food items to draw
    :param backgrounds: the background to draw
    :return: None
    """

    backgrounds.draw()

    for player in players:  # draw and move player objects
        player.move()
        player.draw()

    for food in foods:  # draw and move food objects
        food.move()
        food.rotate()
        food.draw()

    update_fps()
    update_score()
    pygame.display.update()


def update_fps():  # draw fps counter on the window
    fps = str(int(clock.get_fps()))
    fps_text = fps_font.render(fps, 1, pygame.Color("coral"))
    win.blit(fps_text, (WIDTH - 30, 0))


def update_score():  # draw score on the window, increasing size with the score
    score_font = pygame.font.SysFont("Comicsans", score+10)
    score_text = score_font.render(f"{score}", 1, pygame.Color("white"))
    win.blit(score_text, (WIDTH // 2, 0))
