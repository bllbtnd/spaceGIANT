import pygame
import os
import random

pygame.font.init()
ATTACKER_SIZE = 20
WIDTH, HEIGHT = 800, 500
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
DEATH_FONT = pygame.font.SysFont('comicsans', 80)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space GIANT")
pygame.display.set_icon(pygame.image.load(os.path.join('meteor.png')))
PLAYERRAW = pygame.image.load(os.path.join('ufo.png'))
PLAYER = pygame.transform.scale(PLAYERRAW, (150, 75))
ITEMRAW = pygame.image.load(os.path.join('meteor.png'))
ITEM = pygame.transform.scale(ITEMRAW, (ATTACKER_SIZE, ATTACKER_SIZE))
posx, posy = 100, 100
SPEED = 5
def draw_window(posx, posy, poix, poiy, poisize, point, dtext):
    WIN.fill((20, 20, 20))
    WIN.blit(PLAYER, (posx, posy))
    scroetext = SCORE_FONT.render('Score: ' + str(point), 1, (255, 255, 255))
    WIN.blit(scroetext, (WIDTH - scroetext.get_width() - 10, 10))
    item = pygame.transform.scale(ITEM, (poisize, poisize))
    WIN.blit(item, (poix, poiy))
    deathtext = DEATH_FONT.render(dtext, 1, (255, 255, 255))
    WIN.blit(deathtext, (WIDTH/2 - scroetext.get_width() - 70, HEIGHT/2 - scroetext.get_height()))
    pygame.display.update()

def main():
    point = 0
    pispeed = 10
    poisize = ATTACKER_SIZE
    go = True
    pl = pygame.Rect(100, 300, 150, 20)
    pi = pygame.Rect(random.randint(10, 790), 10, 20, 20)
    run = True
    run_count = 0
    dtext = ''
    while run:
        run_count += 1
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and pl.y > 0 and go == True:
            pl.y -= SPEED
        if keys_pressed[pygame.K_s] and pl.y < 490 and go == True:
            pl.y += SPEED
        if keys_pressed[pygame.K_a] and pl.x > 0 and go == True:
            pl.x -= SPEED
        if keys_pressed[pygame.K_d] and pl.x < 700 and go == True:
            pl.x += SPEED
        if keys_pressed[pygame.K_SPACE] and go == False:
            run_count = 1
            go = True
            dtext = ""
            pi.y = 10
            point = 0
            poisize = ATTACKER_SIZE
            pi.x = random.randint(10, 790)
        if keys_pressed[pygame.K_ESCAPE]:
            quit()
        if run_count % 600 == 0 and go == True:
            poisize += 5
            point += 1
            print(poisize)
        if go == True:
            pi.y += pispeed
        if pi.y == 500:
            pi.y = 10
            pi.x = random.randint(10, 790)
        if pi.colliderect(pl):
            dtext = 'You are dead!'
            go = False
        draw_window(pl.x, pl.y, pi.x, pi.y, poisize, point, dtext)
    pygame.QUIT

if __name__ == "__main__":
    main()
