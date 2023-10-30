import pygame
import random
import csv

'''
1 = card back
2...14 = clubs
15...27 = diamonds

'''

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

class MySprite(pygame.sprite.Sprite):
    def __init__(self, csv_path, scale_factor=1.0):
        super().__init__()
        self.image_paths = self.load_image_paths_from_csv(csv_path)
        self.images = [pygame.image.load(path) for path in self.image_paths]
        self.current_image = 0
        self.scale_factor = scale_factor
        self.update_image()

    def load_image_paths_from_csv(self, csv_path):
        image_paths = []
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Check if the row is not empty
                    image_paths.append(row[0])
        return image_paths

    def change_image(self, index):
        self.current_image = index
        self.update_image()

    def update_image(self):
        self.image = pygame.transform.scale(self.images[self.current_image],
                                           (int(self.images[self.current_image].get_width() * self.scale_factor),
                                            int(self.images[self.current_image].get_height() * self.scale_factor)))
        self.rect = self.image.get_rect()


scale_factor = 4.0
csv_path = "Sprites\_cards.csv"
card_sprite = MySprite(csv_path, scale_factor)
card_sprite_x = 40
card_sprite_y = 120
card_sprite_clicked = False

card_sprite2 = MySprite(csv_path, scale_factor)
card_sprite2_x = 120
card_sprite2_y = 120
card_sprite2_clicked = False

card_sprite3 = MySprite(csv_path, scale_factor)
card_sprite3_x = 200
card_sprite3_y = 120
card_sprite3_clicked = False

card_sprite4 = MySprite(csv_path, scale_factor)
card_sprite4_x = 280
card_sprite4_y = 120
card_sprite4_clicked = False

card_sprite5 = MySprite(csv_path, scale_factor)
card_sprite5_x = 360
card_sprite5_y = 120
card_sprite5_clicked = False

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(card_sprite, card_sprite2, card_sprite3, card_sprite4, card_sprite5)

'''
Card Index Map:
0 = Card Back
1 - 13 = Hearts
14 - 26 = Diamonds
27 - 39 = Clubs
40 - 52 = Spades
53 = Black Joker
54 = Red Joker
'''

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        card_sprite.change_image(41)

    # Check if the mouse button is clicked
    if pygame.mouse.get_pressed()[0]:  # 0 represents the left mouse button
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if the mouse position intersects with the sprite's bounding box
        if card_sprite.rect.collidepoint(mouse_x, mouse_y) and not card_sprite_clicked:
            card_sprite.change_image(random.randint(1, 54))
            card_sprite_clicked = True
        elif card_sprite2.rect.collidepoint(mouse_x, mouse_y) and not card_sprite2_clicked:
            card_sprite2.change_image(random.randint(1, 54))
            card_sprite2_clicked = True
        elif card_sprite3.rect.collidepoint(mouse_x, mouse_y) and not card_sprite3_clicked:
            card_sprite3.change_image(random.randint(1, 54))
            card_sprite3_clicked = True
        elif card_sprite4.rect.collidepoint(mouse_x, mouse_y) and not card_sprite4_clicked:
            card_sprite4.change_image(random.randint(1, 54))
            card_sprite4_clicked = True
        elif card_sprite5.rect.collidepoint(mouse_x, mouse_y) and not card_sprite5_clicked:
            card_sprite5.change_image(random.randint(1, 54))
            card_sprite5_clicked = True


    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the card sprite
    card_sprite.rect.topleft = (card_sprite_x, card_sprite_y)
    card_sprite2.rect.topleft = (card_sprite2_x, card_sprite2_y)
    card_sprite3.rect.topleft = (card_sprite3_x, card_sprite3_y)
    card_sprite4.rect.topleft = (card_sprite4_x, card_sprite4_y)
    card_sprite5.rect.topleft = (card_sprite5_x, card_sprite5_y)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()