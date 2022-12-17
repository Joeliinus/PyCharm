"""
Lae alla pall ja alus
Loo uus mäng 640x480 suurusega.Vali heledam taustavärv

Lisa ja animeeri pall
palli suurus 20x20
pall liigub sinu valitud kiirusega
pall põrkub seintest tagasi

Lisa ja animeeri alus
aluse suurus 120x20
aluse y - koordinaat on keskkohast allpool.Näiteks screenY / 1.5
alus liigub vasakule / paremale(vahetab suunda, kui puudub seinu)

Kokkupõrke tuvastamine
kui pall puutub alust siis muudab suunda.
kui pall käitub kokkupuutel alusega imelikult, siis lisa tingimusse kontroll,
et palli y - suund oleks suurem kui null(ballSpeedY > 0)

Boonus
kui pall puudub alumist äärt, siis saab mängija negatiivse punkti
kui pall puutub alust, siis saab positiivse punkti
kuva tulemus mängu ülemises nurgas
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

pall = pygame.image.load("ball.png")
pall = pygame.transform.scale(pall, [20, 20])
alus = pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, [120, 20])
posX = 0
posY = screenY / 1.5
speedX = 0.1
posZ, posQ = 69, 289
speedZ, speedQ = 0.15, 0.15

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

    alus_kast = ekraan.blit(alus, (posX, posY))
    pall_kast = ekraan.blit(pall, (posZ, posQ))

    if pall_kast.colliderect(alus_kast) and speedZ > 0:
        speedQ = -speedQ

    pygame.display.flip()
    ekraan.fill(lBlue)
