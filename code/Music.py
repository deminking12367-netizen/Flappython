from settings import *

# Music

Bg_Music = pygame.mixer.Sound(join('audio','friess.MP3'))
jump = pygame.mixer.Sound(join('audio','cartoon-jump-6462.mp3'))
point = pygame.mixer.Sound(join('audio','Point.mp3'))
Bg_Music.play(loops=-1)
death =  pygame.mixer.Sound(join('audio','DEATH.mp3'))
