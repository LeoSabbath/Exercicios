# Faz reproduzir um arquivo de áudio .mp3

import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load('blackvelho.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()


