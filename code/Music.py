from settings import *

# Music

Bg_Music = pygame.mixer.Sound(join('code','audio','friess.MP3'))
jump = pygame.mixer.Sound(join('code','audio','cartoon-jump-6462.mp3'))
point = pygame.mixer.Sound(join('code','audio','Point.mp3'))
Bg_Music.play(loops=-1)
death =  pygame.mixer.Sound(join('code','audio','DEATH.mp3'))
