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
kell = pygame.time.Clock()

pall = pygame.image.load("ball.png")
pall = pygame.transform.scale(pall, [20, 20])
alus = pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, [120, 20])
posX = 2
posY = screenY / 1.5
speedX = 0.2
posZ, posQ = 69, 289
speedZ, speedQ = 7, 7
directionX, directionY = 0, 0

pygame.mixer.music.load('happy.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.5)
hit_sound = pygame.mixer.Sound('jump.ogg')
log_hit = pygame.mixer.Sound('rock-hitting-log.wav')
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
        pygame.mixer.Sound.play(log_hit)

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
            posX -= 12
    if directionX == "move_right":
        if posX + 120 < screenX:
            posX += 12

    pygame.display.flip()
    ekraan.fill(lBlue)
