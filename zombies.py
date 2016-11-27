import pygame
##from text import *
##from sprites import *
from questions import *


level = 0
questions = questions_set[level]
questions = list(questions.keys())

zombies = []

active_zombies = []

current_zombie = 0

def spawn_zombies():
    global zombies
    global active_zombies
    global zombies_spawned
    if len(zombies) > 0:
        active_zombies.append(zombies[len(zombies)-1])
        del zombies[len(zombies)-1]
