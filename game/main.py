from lib import game as g
import pygame
pygame.init()

audio = pygame.mixer.Sound('song.mp3')

audio.play()

g.play()
