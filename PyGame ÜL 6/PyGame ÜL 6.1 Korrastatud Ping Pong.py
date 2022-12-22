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
screenX = 640   # laius on 640
screenY = 480   # Kõrgus on 480
ekraan = pygame.display.set_mode([screenX, screenY])   # ekraan avab aknale määratud laiuse ja kõrgusega
pygame.display.set_caption("Ping Pong")   # paneb ekraanile pealkirja
lRed = [255, 204, 204]   # annab lRed-ile väärtuseks värvikoodi
taust = pygame.image.load("tilt.png")
taust = pygame.transform.scale(taust, [640, 480])
ekraan.blit(taust, [0, 0])
skoor = 0   # määrab skoori, algväärtusega 0
kell = pygame.time.Clock()   # loob kella objekti

# PILDID JA OMADUSED
alus = pygame.image.load("pad.png")   # määrab alusele palgi pildi
alus = pygame.transform.scale(alus, [120, 20])   # muudab aluse suurust
pall = pygame.image.load("CATDOG.png")   # määrab pallile palli pildi
pall = pygame.transform.scale(pall, [20, 20])   # muudab palli suurust
posX = 200   # määrab posX-i väärtuseks 200
posY = screenY / 1.5   # määrab posY väärtuseks ekraani lauise jagatud 1.5-ga
speedX = 0.2   # määrab speedX-i väärtuseks 0.2
posZ, posQ = 99, 189   # määrab posZ-i väärtuseks 99 ja määrab posQ väärtuseks 189
speedZ, speedQ = 5, 5   # määrab speedZ-i väärtuseks 5 ja speedQ väärtuseks 5
directionX, directionY = 0, 0   # määrab directionX-i väärtuseks 0 ja directionY-i väärtuseks 0

# HELI SEADED
pygame.mixer.music.load('happy.mp3')   # laeb sisse muusika
pygame.mixer.music.play(0)   # mängib sisse laetud muusikat
pygame.mixer.music.set_volume(0.5)   # muudab heli tugevust
porke_heli = pygame.mixer.Sound('jump.ogg')   # tekitad heliobjekti hit_sound
lopu_heli = pygame.mixer.Sound('game-over.wav')   # tekitad heliobjekti end_sound
log_hit = pygame.mixer.Sound('rock-hitting-log.wav')   # tekitad heliobjekti log_hit

# AKENT LAHTI HOIDEV PÕHITSÜKKEL
while True:
    fps = kell.tick(60)   # lisab kaadrisageduse

    # Sulgeb ekraani ristile vajutades
    sisend = pygame.event.poll()
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            sys.exit()

    posZ += speedZ   # posZ suureneb speedZ võrra
    posQ += speedQ   # posQ suureneb speedQ võrra

    aluse_kast = ekraan.blit(alus, (posX, posY))   # määrab alusele tema mõõtme suuruse kasti ja algpositsioonid
    pall_kast = ekraan.blit(pall, (posZ, posQ))   # määrab pallile tema mõõtme suuruse kasti ja algpositsioonid

# PALLI KOKKUPUUDE ASJADEGA
    # Kui posZ on suurem kui ekraani ja palli kasti laiuse vahe või kui posZ on väiksem kui null
    if posZ > screenX-pall.get_rect().width or posZ < 0:
        speedZ = -speedZ   # siis speedZ muutub vastupidiseks
        pygame.mixer.Sound.play(porke_heli)   # ja kostub põrke heli

    # Kui posQ on väiksem kui null
    if posQ < 0:
        speedQ = -speedQ   # siis speedQ muutub vastupidiseks
        pygame.mixer.Sound.play(porke_heli)   # ja kostub põrke heli

    # Kui posQ on suurem kui ekraani ja palli kasti laiuse vahe, mis on saja võrra vähendatud
    if posQ > screenY-pall.get_rect().width-100:
        pygame.mixer.Sound.play(lopu_heli)   # siis kostub lõpu heli

    # Kui posQ on suurem kui ekraani ja palli kasti laiuse vahe
    if posQ > screenY-pall.get_rect().width:
        sys.exit()   # siis ekraan sulgub

# TEKSTI OMADUSED
    font = pygame.font.Font(pygame.font.match_font('Impact'), 20)   # määrab fondi ja suuruse
    skoortekst = font.render("Punktid: " + str(skoor), True, [102, 0, 51])   # määrab teksti ja värvi
    ekraan.blit(skoortekst, [530, 20])   # määrab asukoha

# PALLI KOKKUPUUDE ALUSEGA
    # Kui palli kast puutub kokku aluse kastiga ja posQ on suurem kui 0
    if pall_kast.colliderect(aluse_kast) and posQ > 0:
        speedQ = -speedQ   # siis speedQ muutub vastupidiseks
        skoor += 1   # skoor suureneb ühe võrra
        pygame.mixer.Sound.play(log_hit)   # ja kostub puute heli

    # Kui palli kast puutub kokku aluse kastiga ja speedQ on suurem kui 0.5
    if pall_kast.colliderect(aluse_kast) and speedQ > 0.5:
        speedQ = -speedQ   # siis speedQ muutub vastupidiseks
        skoor -= 1   # ja skoor alaneb ühe võrra

# KLAVIVAJUTUS
    if sisend.type == pygame.KEYDOWN:   # kui vajutad klavhi alla
        if sisend.key == pygame.K_RIGHT:   # ja kui vajutatud klahv on parema noole klav
            directionX = "move_right"   # siis annab juhiseks paremale liikuda
        if sisend.key == pygame.K_LEFT:   # kui vajutatud klahv on vasaku noole klav
            directionX = "move_left"   # siis annab juhiseks vasakule liikuda

# KLAHVIVAJUTUSE VABASTAMINE
    if sisend.type == pygame.KEYUP:   # kui lased klahvi lahti
        if sisend.key == pygame.K_RIGHT or sisend.key == pygame.K_LEFT:   # ja kui lahti lastud klav on parem või vasak
            directionX = 0   # siis ei liigu kuhugi

# MÄNGU PIIRJOONTE TUVASTAMINE
    if directionX == "move_left":   # kui juhiseks on vasakule liikuda
        if posX > 5:   # ja kui posX on väiksem kui 5
            posX -= 15   # siis posX väheneb 15 võrra
    if directionX == "move_right":   # kui juhiseks on paremale liikuda
        if posX + 130 < screenX:   # ja kui posX-i ja 130 summa on väiksem kui screenX
            posX += 15   # siis posX suureneb 15 võrra

# EKRAANI VÄRSKENDAMINE
    pygame.display.flip()
    taust = pygame.image.load("tilt.png")
    taust = pygame.transform.scale(taust, [640, 480])
    ekraan.blit(taust, [0, 0])
