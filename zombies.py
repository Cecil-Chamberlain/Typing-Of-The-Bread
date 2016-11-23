import pygame
from text import *
from sprites import *
from questions import *


level = 0
questions = questions_set[level]
questions = list(questions.keys())

zombies = []

active_zombies = []

zombies_spawned = 1

current_zombie = 0

def spawn_zombies():
    global zombies
    global active_zombies
    global zombies_spawned
    if len(zombies) != zombies_spawned:
        active_zombies.append(zombies[zombies_spawned])
        zombies_spawned += 1
