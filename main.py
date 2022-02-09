import pygame 

pygame.init()

bullet_speed = 5
player_speed = 2

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

width, height = 700, 400
border = pygame.Rect(width/2 - 5, 0, 10, height)

screen = pygame.display.set_mode((width, height))
yellow_spaceship_img = pygame.image.load('spaceship_yellow.png')
yellow_spaceship = pygame.transform.scale(yellow_spaceship_img, (55, 40))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)

red_spaceship_img = pygame.image.load('spaceship_red.png')
red_spaceship = pygame.transform.scale(red_spaceship_img, (55, 40))
red_spaceship = pygame.transform.rotate(red_spaceship, 270)

def draw_window(red, yellow, red_bullets, yellow_bullets):
    screen.fill((0,0,0)) #R, G, B
    pygame.draw.rect(screen, (255,255,255), border)

    screen.blit(yellow_spaceship, (yellow.x, yellow.y))
    screen.blit(red_spaceship, (red.x, red.y))

    for bullet in red_bullets:
      pygame.draw.rect(screen, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
      pygame.draw.rect(screen, (255, 255, 0), bullet)
    pygame.display.update()


def yellow_spaceship_move(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: # Left
        yellow.x -= player_speed
    if keys_pressed[pygame.K_d]: # Right
        yellow.x += player_speed
    if keys_pressed[pygame.K_w]:
        yellow.y -= player_speed
    if keys_pressed[pygame.K_s]:
        yellow.y += player_speed


def red_spaceship_move(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: # Left
        red.x -= player_speed
    if keys_pressed[pygame.K_RIGHT]: # Right
        red.x += player_speed
    if keys_pressed[pygame.K_UP]:
        red.y -= player_speed
    if keys_pressed[pygame.K_DOWN]:
        red.y += player_speed


def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x -= bullet_speed
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x += bullet_speed
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)

        elif bullet.x > width:
            yellow_bullets.remove(bullet)


def main():
    yellow = pygame.Rect(100, 300, 55, 40)
    red = pygame.Rect(500, 300, 55, 40)

    red_bullets = []
    yellow_bullets = []

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                yellow_bullets.append(bullet)

            if event.key == pygame.K_RALT:
                bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()

        yellow_spaceship_move(keys_pressed, yellow)
        red_spaceship_move(keys_pressed, red)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)
        
        draw_window(red, yellow, red_bullets, yellow_bullets)

main()
