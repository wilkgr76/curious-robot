import pygame

background_colour = (255,255,255)
(width, height) = (256, 256)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()

# Load Textures
ground = pygame.image.load('stuff/textures/ground.png') 
grass = pygame.image.load('stuff/textures/grass.png')

#screen.blit(ground,(50,100))
#screen.blit(grass,(50,100))
pygame.display.flip()

i=0
while i < 256:
  screen.blit(ground,(i,240))
  i = i+16
i=0
while i < 240:
  screen.blit(grass,(i,240))
  i = i+16
screen.blit(ground,(240,224))
screen.blit(grass,(240,224))
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False