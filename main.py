import pygame

# Constants
WIDTH, HEIGHT = 800, 600

PLAYER_SPEED = 5
PLAYER_SIZE = 64

BACKGROUND_COLOR = (127, 64, 0)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player position
player_x, player_y = WIDTH // 2, HEIGHT // 2

# Load sprites
player_sprite = pygame.image.load("player.png")
player_sprite = pygame.transform.scale(player_sprite, (PLAYER_SIZE, PLAYER_SIZE))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]: player_x += PLAYER_SPEED
    if keys[pygame.K_UP]: player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]: player_y += PLAYER_SPEED

    window.fill(BACKGROUND_COLOR)
    window.blit(player_sprite, (player_x - PLAYER_SIZE // 2, player_y - PLAYER_SIZE // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()