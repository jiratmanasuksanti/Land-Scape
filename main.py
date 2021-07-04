import pygame
pygame.init()
#############
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height),pygame.FULLSCREEN)
title = pygame.display.set_caption("LandScape")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
