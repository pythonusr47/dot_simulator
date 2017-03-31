import ly
from unit import Unit
import pygame, sys, random
from pygame.locals import *
fps=60
clock = pygame.time.Clock()

display = pygame.display.set_mode((700,800))

units = [Unit(ly.randgen_location(700,800), ly.randgen_color(), 2) for i in range(100)]

yums = ly.gen_yums()

while True:
    display.fill((0, 0, 0))
    for unit in units:
        unit.move()
        loc = unit.location
        if loc in yums:
            if yums[loc] > 0:
                yums[loc] -= 1
                unit.yums += 1
            if yums[loc] < 1:
                del yums[loc]
        pygame.draw.circle(display, unit.color, unit.location, 3)
    yumcount = 0
    for yum in yums:
        yumcount += yums[yum]
        pygame.draw.circle(display, (0,255,0), yum, 2)
    if yumcount < 500:
        yums = ly.gen_yums()
    pygame.display.update()
    ly.event_handler()
    clock.tick(fps)
