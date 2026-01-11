
import pygame, random, numpy as np, copy

sc = pygame.display.set_mode((1600, 900))

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit()
