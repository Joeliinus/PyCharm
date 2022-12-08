import pygame
pygame.init()

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("2")
screen.fill([204, 255, 204])

bgshop = pygame.image.load("bgshop.jpg")
screen.blit(bgshop, [0, 0])

seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [253, 307])
screen.blit(seller, [105, 158])

chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [257, 203])
screen.blit(chat, [245, 66])

font = pygame.font.Font(pygame.font.match_font('comic sans'), 19)
text = font.render("Tere, olen Joel Riive", True, [255, 255, 255])
screen.blit(text, [280, 135])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
