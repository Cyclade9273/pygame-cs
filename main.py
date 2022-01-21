import pygame, sys, os
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 400

clock = pygame.time.Clock()
FPS = 60
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game window")

# Loading images and scaling
red_spaceship_img = pygame.image.load("spaceship_red.png")
red_spaceship = pygame.transform.scale(red_spaceship_img, (55, 40))
red_spaceship = pygame.transform.rotate(red_spaceship, 90)

yellow_spaceship_img = pygame.image.load("spaceship_yellow.png")
yellow_spaceship = pygame.transform.scale(yellow_spaceship_img, (55, 40))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship, -90)

def draw_window(red, yellow):
    WIN.fill((0, 255, 0))
    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(yellow_spaceship, (yellow.y, yellow.x))
    pygame.display.update()

def main():
    running = True

    red_rect = pygame.Rect(100, 300, 55, 40)
    yellow_rect = pygame.Rect(500, 300, 55, 40)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window(red_rect, yellow_rect)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_ESCAPE]: running = False # easier for testing, can be commented out

        if keys_pressed[pygame.K_a]:
            red_rect.x -= 2
        if keys_pressed[pygame.K_d]:
            red_rect.x += 2

        clock.tick(FPS)

main()