import pygame
import sys
import time

# Ініціалізація Pygame
pygame.init()

# Розмір вікна
width, height = 400, 200

# Створення вікна
screen = pygame.display.set_mode((width, height))

# Кольори від райдуги
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 165, 0)
yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 128, 0)
blue = pygame.Color(0, 0, 255)
indigo = pygame.Color(75, 0, 130)
violet = pygame.Color(238, 130, 238)

# Частота оновлення кадрів
fps = 60
clock = pygame.time.Clock()

# Час анімації (в секундах)
animation_time = 10.0

# Головний цикл
start_time = time.time()
while True:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обчислення пройденого часу
    elapsed_time = time.time() - start_time

    # Відсоток завершення анімації
    progress = elapsed_time / animation_time

    # Інтерполяція кольору від райдуги
    r = int(max(0, min((1 - progress) * red.r + progress * violet.r, 255)))
    g = int(max(0, min((1 - progress) * red.g + progress * violet.g, 255)))
    b = int(max(0, min((1 - progress) * red.b + progress * violet.b, 255)))

    # Заповнення екрану поточним кольором
    screen.fill((r, g, b))

    # Оновлення екрану
    pygame.display.flip()
    clock.tick(fps)
