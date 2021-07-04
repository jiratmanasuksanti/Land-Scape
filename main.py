import pygame
pygame.init()
#############
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height),pygame.FULLSCREEN)
title = pygame.display.set_caption("LandScape")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
gameloop = True
#Import Module#
from menu_data import *

while gameloop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameloop = False
