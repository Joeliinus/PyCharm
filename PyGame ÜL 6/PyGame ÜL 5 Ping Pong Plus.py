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
Lisa mängule taustamuusika
Lisa heliefektid
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

alus = pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, [120, 20])
pall = pygame.image.load("ball.png")
pall = pygame.transform.scale(pall, [20, 20])
posX = 2
posY = screenY / 1.5
speedX = 0.3
posZ, posQ = 69, 289
speedZ, speedQ = 0.5, 0.5

pygame.mixer.music.load('happy.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.5)
hit_sound = pygame.mixer.Sound('jump.ogg')
log_hit = pygame.mixer.Sound('rock-hitting-log.wav')
end_sound = pygame.mixer.Sound('game-over.wav')

while True:
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        sys.exit()

    posX += speedX
    posZ += speedZ
    posQ += speedQ

    if posX > screenX-alus.get_rect().width or posX < 0:
        speedX = -speedX
        pygame.mixer.Sound.play(log_hit)

    if posZ > screenX-pall.get_rect().width or posZ < 0:
        speedZ = -speedZ
        pygame.mixer.Sound.play(hit_sound)

    if posQ < 0:
        speedQ = -speedQ
        pygame.mixer.Sound.play(hit_sound)

    if posQ > screenY-pall.get_rect().width:
        speedQ = -speedQ
        pygame.mixer.Sound.play(end_sound)

    aluse_kast = ekraan.blit(alus, (posX, posY))
    pall_kast = ekraan.blit(pall, (posZ, posQ))

    font = pygame.font.Font(pygame.font.match_font('comic sans'), 16)
    skoortekst = font.render("Punktid: " + str(skoor), True, [255, 255, 255])
    ekraan.blit(skoortekst, [535, 20])

    if pall_kast.colliderect(aluse_kast) and posQ > 0:
        speedQ = -speedQ
        skoor += 4
        pygame.mixer.Sound.play(log_hit)

    if pall_kast.colliderect(aluse_kast) and speedQ > 0.2:
        speedQ = -speedQ
        skoor -= 4

    if posQ > 460:
        skoor -= 1

    pygame.display.flip()
    ekraan.fill(lBlue)
