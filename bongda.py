import pygame
from modules.player import Player
from modules.ball import Ball
from modules.goalkeeper import Goalkeeper
from modules.ui import draw_ui

# Khởi tạo game
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⚽ Đá Banh Pro")

# Tạo đối tượng
player = Player(WIDTH // 2, HEIGHT - 100)
ball = Ball(WIDTH // 2, HEIGHT // 2)
goalkeeper = Goalkeeper(WIDTH // 2, 50)

clock = pygame.time.Clock()
score = 0

running = True
while running:
    clock.tick(60)
    screen.fill((34, 139, 34))  # Sân bóng màu xanh
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_keys()
    ball.move()
    goalkeeper.move()

    # Va chạm bóng & khung thành
    if ball.check_goal(goalkeeper.rect):
        score += 1
        ball.reset()

    # Vẽ các đối tượng
    player.draw(screen)
    ball.draw(screen)
    goalkeeper.draw(screen)
    draw_ui(screen, score)

    pygame.display.flip()

pygame.quit()
