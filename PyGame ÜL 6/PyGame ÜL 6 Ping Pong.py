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
kui pall käitub kokkupuutel alusega imelikult, siis lisa tingimusse kontroll, et palli y - suund oleks suurem kui null(ballSpeedY > 0)

Boonus
kui pall puudub alumist äärt, siis saab mängija negatiivse punkti
kui pall puutub alust, siis saab positiivse punkti
kuva tulemus mängu ülemises nurgas
"""

import pygame
import sys
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping Pong")
lBlue = [153, 204, 255]
screen.fill(lBlue)

alus = pygame.image.load("pad.png")

# sulgemine hiirega
pygame.display.flip()

while True:
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        sys.exit()
    pygame.display.flip()
