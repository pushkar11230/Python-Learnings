import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors - Dark theme
DARK_BG = (20, 20, 30)
LIGHT_GREEN = (100, 255, 100)
BRIGHT_RED = (255, 80, 80)
WHITE = (255, 255, 255)

# Font for score display
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 10

# Snake properties
snake_pos = [300, 200]
snake_body = [[300, 200], [290, 200], [280, 200]]
direction = 'RIGHT'
change_to = direction

# Food - random position
food_pos = [random.randint(0, (WIDTH-10)//10)*10, random.randint(0, (HEIGHT-10)//10)*10]

# Score tracking
current_score = 0
high_score = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    # Update direction
    direction = change_to
    
    # Move snake
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10
    
    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    
    # Check if snake eats food
    if snake_pos == food_pos:
        # Food eaten - reposition food and grow snake
        current_score += 10
        if current_score > high_score:
            high_score = current_score
        food_pos = [random.randint(0, (WIDTH-10)//10)*10, random.randint(0, (HEIGHT-10)//10)*10]
    else:
        # Food not eaten - remove last segment (no growth)
        snake_body.pop()
    
    # Clear screen with dark background
    screen.fill(DARK_BG)
    
    # Draw food as circle
    pygame.draw.circle(screen, BRIGHT_RED, (food_pos[0] + 5, food_pos[1] + 5), 5)
    
    # Draw snake
    for segment in snake_body:
        pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(segment[0], segment[1], 10, 10))
    
    # Draw score text
    score_text = font.render(f"Score: {current_score}", True, WHITE)
    high_score_text = small_font.render(f"High Score: {high_score}", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
