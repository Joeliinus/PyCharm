"""
Loo vastutulevate autode animatsioon ning loe skoori: punane_auto, sinine_auto, taust

Loo mäng 640×480 suurusega
Lisa tautapilt
Lisa ekraani alla keskele punane auto
Lisa siniste autode animatsioon ülevalt alla
autod jäävad tee vahemikku
alustavad erinevatelt kõrgustelt
kui auto alla jõuab, hakkab ta uuesti ülevalt alla liikuma
Kuva skoor
kui sinine auto jõuab alla, lisatakse skoorile punkte juurde
arv, mida soovid lisada tekstikasti, tuleb teisendada tekstiks str(number)
"""


import pygame
import sys
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ralli")

# graafika laadimine
pauto = pygame.image.load("f1_red.png")
sauto = pygame.image.load("f1_blue.png")
sauto = pygame.transform.rotate(sauto, 180)
sauto2 = pygame.image.load("f1_blue.png")
sauto2 = pygame.transform.rotate(sauto2, 180)
taust = pygame.image.load("bg_rally.jpg")
screen.blit(taust, [0, 0])
scoreboard = pygame.image.load("skoorkast.png")
scoreboard = pygame.transform.scale(scoreboard, [100, 100])
screen.blit(scoreboard, [245, 66])
skoor = 0
skoor2 = 0

# heliefektide lisamine
auto_heli = pygame.mixer.Sound('niuh.wav')
start_heli = pygame.mixer.Sound('robot-go.wav')
pygame.mixer.Sound.play(start_heli)
pygame.mixer.Sound.play(auto_heli)

# kiirus ja asukoht
posX, posY = 175, 80
posZ, posQ = 300, 375
posN, posM = 425, 100
speedY, speedM = 7, 5

# sulgemine hiirega
while True:
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        sys.exit()

    # skoori lisamine ekraanile
    font = pygame.font.Font(pygame.font.match_font('comic sans'), 16)
    skoortekst = font.render("Vasak: " + str(skoor), True, [255, 255, 255])
    screen.blit(skoortekst, [535, 20])
    skoortekst2 = font.render("Parem: " + str(skoor2), True, [255, 255, 255])
    screen.blit(skoortekst2, [535, 45])

    # pildi lisamine ekraanile
    screen.blit(pauto, (posZ, posQ))
    screen.blit(sauto, (posX, posY))
    screen.blit(sauto2, (posN, posM))

    # auto positsioon suureneb kiiruse võrra
    posY += speedY
    posM += speedM

    # kui auto jõuab alla, siis läheb tagasi üles ja suurendab ühe võrra skoori
    if posY > screenY:
        posX, posY = 175, -85
    if posY < -84:
        skoor += 1
        pygame.mixer.Sound.play(auto_heli)

    if posM > screenY:
        posN, posM = 425, -85
    if posM < -84:
        skoor2 += 1
        pygame.mixer.Sound.play(auto_heli)

    # graafika kuvamine ekraanil
    pygame.display.flip()
    taust = pygame.image.load("bg_rally.jpg")
    screen.blit(taust, [0, 0])
    scoreboard = pygame.image.load("skoorkast.png")
    scoreboard = pygame.transform.scale(scoreboard, [125, 75])
    screen.blit(scoreboard, [515, 0])
