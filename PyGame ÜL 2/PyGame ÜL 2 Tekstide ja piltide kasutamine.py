import pygame
pygame.init()

# lisab taustamuusika
pygame.mixer.music.load('village-theme.wav')
pygame.mixer.music.play(0)

# määrab ekraani suuruse ning paneb sellele nime
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("2")

# täidab ekraani pildiga, millest saab tagataust
bgshop = pygame.image.load("bgshop.jpg")
screen.blit(bgshop, [0, 0])

# lisab müüa pildi ja muudab sele suurust ja asukohta
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [253, 307])
screen.blit(seller, [105, 158])

# lisab jutumulli pildi ja muudab selle suurust ja asukohta
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [257, 203])
screen.blit(chat, [245, 66])

# määrab teksti fondi suuruse, värvi, olemuse ja asukoha
font = pygame.font.Font(pygame.font.match_font('comic sans'), 19)
text = font.render("Tere, olen Joel Riive", True, [255, 255, 255])
screen.blit(text, [280, 135])

# sulgemine hiirega
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
