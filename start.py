import random, pygame

background_colour = (208,240,255)
(width, height) = (256, 256)

tw = 16 # Texture Width

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Curious Robot')
screen.fill(background_colour)

# Load Textures
ground = pygame.image.load('stuff/textures/ground.png') 
grass = pygame.image.load('stuff/textures/grass.png')
y_grass = pygame.image.load('stuff/textures/y_grass.png')


#screen.blit(ground,(50,100))
#screen.blit(grass,(50,100))
pygame.display.flip()

#while i < 256:
#  height = random.randint(0,240)
#  addgrass = random.randint(0,100)
#  screen.blit(ground,(i,height))
#  if addgrass > 50: 
#    screen.blit(grass,(i,height))
#  i = i+16
#i=0

n = 1

while n < 6: # No. of blocks to be rendered atm
  n = n+1     # Increase n by 1, don't want an endless loop
  i = 0
  w = random.randint(3,5) # w is width of platform
  y = random.randint(0,15) # y is height of platform
  x = random.randint(0,15)
  c = random.randint(0,1) 
  while i < w:
    screen.blit(ground,(tw*x+tw*i,tw*y))
    if c == 1:
      screen.blit(grass,(tw*x+tw*i,tw*y))
    else:
      screen.blit(y_grass,(tw*x+tw*i,tw*y))  
    i = i+1
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False