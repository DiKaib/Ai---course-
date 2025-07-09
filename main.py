import pygame
import random
import sys

# --- Настройки ---
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# --- Цвета ---
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# --- Инициализация ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая змейка")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)

# --- Функции ---
def draw_block(color, pos):
    pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

def random_position():
    return [random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)]

# --- Переменные игры ---
snake = [[100, 100]]
direction = "RIGHT"
food = random_position()
score = 0
speed = 10

# --- Игровой цикл ---
running = True
while running:
    screen.fill(WHITE)

    # --- События ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Управление ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    elif keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    elif keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    elif keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    # --- Движение змейки ---
    head = list(snake[0])
    if direction == "UP":
        head[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        head[1] += BLOCK_SIZE
    elif direction == "LEFT":
        head[0] -= BLOCK_SIZE
    elif direction == "RIGHT":
        head[0] += BLOCK_SIZE
    snake.insert(0, head)

    # --- Проверка еды ---
    if head == food:
        score += 1
        food = random_position()
    else:
        snake.pop()

    # --- Проверка столкновений ---
    if head in snake[1:] or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # --- Отрисовка ---
    for block in snake:
        draw_block(GREEN, block)
    draw_block(RED, food)

    score_text = font.render(f"Счёт: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()