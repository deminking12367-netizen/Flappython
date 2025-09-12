from settings import *

# Objects
      
# Menu screen

menu = pygame.image.load(join('graphics', 'Menu_screen.png'))
menu = pygame.transform.scale(menu,(1500,800))


# Sky
   
sky = pygame.image.load(join('graphics', 'Sky.png'))
sky1 = pygame.image.load(join('graphics', 'Sky.png'))

# Ground

# Frame 1

ground = pygame.image.load(join('graphics','Ground.png'))
ground = pygame.transform.scale(ground,(1000,700))

# Frame 2

ground1 = pygame.image.load(join('graphics','Ground.png'))
ground1 = pygame.transform.scale(ground1,(1000,700))

# Obstacle

# Frame 1

obstacle = pygame.image.load(join('graphics', 'pipe', 'pipeup.png'))
obstacle = pygame.transform.scale(obstacle,(300,900))

# Frame 2

obstacle1 = pygame.image.load(join('graphics', 'pipe', 'pipedown.png'))
obstacle1 = pygame.transform.scale(obstacle1,(300,900))

# Frame 3

obstacl1e = pygame.image.load(join('graphics', 'pipe', 'pipeup.png'))
obstacl1e = pygame.transform.scale(obstacl1e,(300,900))

# Frame 4

obstacl1e1 = pygame.image.load(join('graphics', 'pipe', 'pipedown.png'))
obstacl1e1 = pygame.transform.scale(obstacl1e1,(300,900))

# Player

player = pygame.image.load(join('graphics', 'durpthon', 'durpthon.png'))
player = pygame.transform.scale(player,(100,200))

# Font

test = pygame.font.Font(join('graphics', 'Pixeltype.ttf'), 60)
