<<<<<<< HEAD
def solution(hp, monsters, attack):
    monster_damage = {
        -1: 0,  # 회피
        0: monsters['골렘'],
        1: monsters['리본돼지'],
        2: monsters['슬라임']
    }
    
    for hit in attack:
        hp -= monster_damage[hit]
        if hp <= 0:
            return -1
    
    return hp

# 테스트 케이스
hp = 200
monsters = {'골렘': 40, '리본돼지': 20, '슬라임': 10}

attack = [-1, 0, 1, 1, 0, 2, -1, 1]
attack2 = [0, 0, 0, 0, 0, 2, -1, 1]
attack3 = [-1, -1, 1, 1, 0, 2, -1, 1]
attack4 = [-1, -1, -1, -1, -1, -1, -1, -1]

print(solution(hp, monsters, attack))   # 50
print(solution(hp, monsters, attack2))  # -1
print(solution(hp, monsters, attack3))  # 90
print(solution(hp, monsters, attack4))  # 200

=======
import pygame
import random
import sys
from datetime import datetime

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Game")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# FPS 설정
clock = pygame.time.Clock()

# 플레이어 설정
player_size = 20
player_x = (WIDTH - player_size) // 2
player_y = (HEIGHT - player_size) // 2
player_speed = 5

# 적 설정
enemy_size = 10
enemies = []
enemy_speed = 3

# 점수 및 시간 기록
start_time = datetime.now()
score = 0

# 게임 루프
running = True
while running:
    screen.fill(BLACK)

    # **이벤트 처리**
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # **키 입력 처리**
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # **적 생성**
    if random.randint(1, 50) == 2:  # 적이 가끔씩 생성되도록 조정
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemies.append([enemy_x, 0])

    # **적 이동**
    for enemy in enemies:
        enemy[1] += enemy_speed  # 아래로 이동

    # **충돌 감지**
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):  # 충돌 시 종료
            running = False

    # **점수 갱신**
    elapsed_time = (datetime.now() - start_time).seconds
    score = elapsed_time

    # **객체 그리기**
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))  # 플레이어
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, (enemy[0], enemy[1], enemy_size, enemy_size))  # 적

    # **점수 표시**
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # **화면 업데이트**
    pygame.display.flip()
    clock.tick(60)  # FPS 제한

# **게임 종료 후 메시지 표시**
print(f"Game Over! Your survival time: {score} seconds")
pygame.quit()
sys.exit()
>>>>>>> 80ab5859be5efd8854fea1296f389015985eac10
