import pygame
import random

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/тир.jpeg")
pygame.display.set_icon(icon)

# Параметры цели
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Генерация начальной позиции цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменная для подсчёта очков
score = 0
font = pygame.font.SysFont(None, 36)

# Основной цикл игры
running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получаем координаты клика мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверяем, попал ли игрок по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Увеличиваем счёт
                score += 1

                # Перемещаем цель на новое место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Рисуем цель
    screen.blit(target_img, (target_x, target_y))

    # Выводим количество очков на экран
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновляем экран
    pygame.display.update()

pygame.quit()


