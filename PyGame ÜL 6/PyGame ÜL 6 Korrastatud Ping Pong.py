"""
Eesmärk: korrastada mäng PingPong

Ava Harjutus 5 “PingPong” ja salvesta uue nimega
Lisa mängule taustamuusika
Kontrolli alust klaviatuuri abil x-suunal
alus ei välja mängu piiridest
Kui pall puudub alumist äärt, siis mäng lõpetatakse
"""

import pygame
import sys
pygame.init()

screenX = 640
screenY = 480
ekraan = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping Pong")
lRed = [255, 204, 204]
ekraan.fill(lRed)
skoor = 0
kell = pygame.time.Clock()

alus = pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, [120, 20])
pall = pygame.image.load("ball.png")
pall = pygame.transform.scale(pall, [20, 20])
posX = 2
posY = screenY / 1.5
speedX = 0.2
posZ, posQ = 99, 289
speedZ, speedQ = 10, 10
directionX, directionY = 0, 0

pygame.mixer.music.load('happy.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.5)
hit_sound = pygame.mixer.Sound('jump.ogg')
end_sound = pygame.mixer.Sound('game-over.wav')

while True:
    dt = kell.tick(30)

    sisend = pygame.event.poll()
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            sys.exit()

    posZ += speedZ
    posQ += speedQ

    if posX > screenX-alus.get_rect().width or posX < 0:
        speedX = -speedX

    if posZ > screenX-pall.get_rect().width or posZ < 0:
        speedZ = -speedZ
        pygame.mixer.Sound.play(hit_sound)

    if posQ < 0:
        speedQ = -speedQ
        pygame.mixer.Sound.play(hit_sound)

    if posQ > screenY-pall.get_rect().width-100:
        pygame.mixer.Sound.play(end_sound)

    if posQ > screenY-pall.get_rect().width:
        sys.exit()

    aluse_kast = ekraan.blit(alus, (posX, posY))
    pall_kast = ekraan.blit(pall, (posZ, posQ))

    font = pygame.font.Font(pygame.font.match_font('Impact'), 20)
    skoortekst = font.render("Punktid: " + str(skoor), True, [102, 0, 51])
    ekraan.blit(skoortekst, [530, 20])

    if pall_kast.colliderect(aluse_kast) and posQ > 0:
        speedQ = -speedQ
        skoor += 4
        pygame.mixer.Sound.play(hit_sound)

    if pall_kast.colliderect(aluse_kast) and speedQ > 0.2:
        speedQ = -speedQ
        skoor -= 4

    if posQ > 460:
        skoor -= 1

    # klahvivajutus
    if sisend.type == pygame.KEYDOWN:
        if sisend.key == pygame.K_RIGHT:
            directionX = "move_right"
        if sisend.key == pygame.K_LEFT:
            directionX = "move_left"

    # klahvivajutuse vabastamine
    if sisend.type == pygame.KEYUP:
        if sisend.key == pygame.K_RIGHT or sisend.key == pygame.K_LEFT:
            directionX = 0

    # mängu piirjoonte tuvastamine
    if directionX == "move_left":
        if posX > 5:
            posX -= 15
    if directionX == "move_right":
        if posX + 130 < screenX:
            posX += 15

    pygame.display.flip()
    ekraan.fill(lRed)
