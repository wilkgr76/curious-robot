import random, pygame

background_colour = (255,255,255)
(width, height) = (256, 256)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Curious Robot')
screen.fill(background_colour)

# Load Textures
ground = pygame.image.load('stuff/textures/ground.png') 
grass = pygame.image.load('stuff/textures/grass.png')

#screen.blit(ground,(50,100))
#screen.blit(grass,(50,100))
pygame.display.flip()

i=0
#while i < 256:
#  height = random.randint(0,240)
#  addgrass = random.randint(0,100)
#  screen.blit(ground,(i,height))
#  if addgrass > 50: 
#    screen.blit(grass,(i,height))
#  i = i+16
#i=0

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False