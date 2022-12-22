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

# EKRAANI SEADED
screenX = 640
screenY = 480
ekraan = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping Pong")
taust = pygame.image.load("tilt.png")
taust = pygame.transform.scale(taust, [640, 480])
ekraan.blit(taust, [0, 0])
skoor = 0
kell = pygame.time.Clock()

# PILDID JA OMADUSED
alus = pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, [120, 20])
pall = pygame.image.load("CATDOG.png")
pall = pygame.transform.scale(pall, [30, 30])
posX = 200
posY = screenY / 1.5
speedX = 0.2
posZ, posQ = 99, 189
speedZ, speedQ = 5, 5
directionX, directionY = 0, 0

# HELI SEADED
pygame.mixer.music.load('happy.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.5)
porke_heli = pygame.mixer.Sound('jump.ogg')
lopu_heli = pygame.mixer.Sound('game-over.wav')
log_hit = pygame.mixer.Sound('rock-hitting-log.wav')

# AKENT LAHTI HOIDEV PÕHITSÜKKEL
while True:
    fps = kell.tick(60)   # lisab kaadrisageduse

    # Sulgeb ekraani ristile vajutades
    sisend = pygame.event.poll()
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            sys.exit()

    # Palli asukoht muutub vastavalt palli kiirusele
    posZ += speedZ
    posQ += speedQ

    # Lisab palgile ja pallile kokkupuutekastid
    aluse_kast = ekraan.blit(alus, (posX, posY))
    pall_kast = ekraan.blit(pall, (posZ, posQ))

# PALLI KOKKUPUUDE ASJADEGA
    if posZ > screenX-pall.get_rect().width or posZ < 0:
        speedZ = -speedZ
        pygame.mixer.Sound.play(porke_heli)

    if posQ < 0:
        speedQ = -speedQ
        pygame.mixer.Sound.play(porke_heli)

    if posQ > screenY-pall.get_rect().width-100:
        pygame.mixer.Sound.play(lopu_heli)

    if posQ > screenY-pall.get_rect().width:
        sys.exit()

# TEKSTI OMADUSED
    font = pygame.font.Font(pygame.font.match_font('Impact'), 20)
    skoortekst = font.render("Punktid: " + str(skoor), True, [251, 141, 11])
    ekraan.blit(skoortekst, [530, 20])

# PALLI KOKKUPUUDE ALUSEGA
    if pall_kast.colliderect(aluse_kast) and posQ > 0:
        speedQ = -speedQ
        skoor += 1
        pygame.mixer.Sound.play(log_hit)

    if pall_kast.colliderect(aluse_kast) and speedQ > 0.5:
        speedQ = -speedQ
        skoor -= 1

# KLAVIVAJUTUS
    if sisend.type == pygame.KEYDOWN:
        if sisend.key == pygame.K_RIGHT:
            directionX = "move_right"
        if sisend.key == pygame.K_LEFT:
            directionX = "move_left"

# KLAHVIVAJUTUSE VABASTAMINE
    if sisend.type == pygame.KEYUP:
        if sisend.key == pygame.K_RIGHT or sisend.key == pygame.K_LEFT:
            directionX = 0

# MÄNGU PIIRJOONTE TUVASTAMINE
    if directionX == "move_left":
        if posX > 5:
            posX -= 15
    if directionX == "move_right":
        if posX + 130 < screenX:
            posX += 15

# EKRAANI VÄRSKENDAMINE
    pygame.display.flip()
    taust = pygame.image.load("tilt.png")
    taust = pygame.transform.scale(taust, [640, 480])
    ekraan.blit(taust, [0, 0])
