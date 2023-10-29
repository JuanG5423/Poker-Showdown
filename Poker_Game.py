import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

#cursor_sprite = MySprite("Sprites/Cursor.png")
cursorx = 40
cursory = 120
#cursor_sprite.rect.topleft = (cursorx, cursory)

# Sprite groups
all_sprites = pygame.sprite.Group()


# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()


    # Clear the screen
    all_sprites.draw(screen)
    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()