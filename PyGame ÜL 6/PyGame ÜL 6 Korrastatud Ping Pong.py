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
lBlue = [153, 204, 255]
ekraan.fill(lBlue)
skoor = 0

pall = pygame.image.load("ball.png")
pall = pygame.transform.scale(pall, [20, 20])
alus = pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, [120, 20])
posX = 2
posY = screenY / 1.5
speedX = 0.3
posZ, posQ = 69, 289
speedZ, speedQ = 0.5, 0.5

pygame.mixer.music.load('happy.mp3')
pygame.mixer.music.play(0)

while True:
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        sys.exit()

    posX += speedX
    posZ += speedZ
    posQ += speedQ

    if posX > screenX-alus.get_rect().width or posX < 0:
        speedX = -speedX

    if posZ > screenX-pall.get_rect().width or posZ < 0:
        speedZ = -speedZ

    if posQ > screenY-pall.get_rect().width or posQ < 0:
        speedQ = -speedQ

    aluse_kast = ekraan.blit(alus, (posX, posY))
    pall_kast = ekraan.blit(pall, (posZ, posQ))

    font = pygame.font.Font(pygame.font.match_font('comic sans'), 16)
    skoortekst = font.render("Punktid: " + str(skoor), True, [255, 255, 255])
    ekraan.blit(skoortekst, [535, 20])

    if pall_kast.colliderect(aluse_kast) and posQ > 0:
        speedQ = -speedQ
        skoor += 4

    if pall_kast.colliderect(aluse_kast) and speedQ > 0.2:
        speedQ = -speedQ
        skoor -= 4

    if posQ > 460:
        skoor -= 1

    pygame.display.flip()
    ekraan.fill(lBlue)
