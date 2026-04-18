import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('None')

while True:
    """检查事件并打印"""
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(f"检测到按键: {pygame.key.name(event.key)}")

    pygame.display.flip()