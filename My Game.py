import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.flip()
pygame.display.set_caption("My Game")
screen.fill([89, 89, 89])
clock = pygame.time.Clock()
FPS = 30

move_right = False
move_left = False
move_up = False
move_down = False

speed = 10
X = 300
Y = 300

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True

    if move_right == True:
        X += speed
    if move_left == True:
        X -= speed
    if move_up == True:
        Y -= speed
    if move_down == True:
        Y += speed

    screen.fill([89, 89, 89])
    pygame.draw.circle(screen, [76, 185, 199], [X, Y,], 35)
    pygame.display.flip()
pygame.quit()
