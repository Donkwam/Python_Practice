import pygame
import random   # 랜덤함수 가져오기
import sys
from datetime import datetime   # 경과 시간 구하기

pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("창 피하기")


pygame.quit()
sys.exit()