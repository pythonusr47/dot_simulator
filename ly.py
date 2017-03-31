import pygame, random, sys

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

def gen_yums():
    yumDict = dict()
    for i in range(20):
        location = randgen_location(700,800)
        count = random.randint(50,120)
        if location in yumDict:
            yumDict[location] += count
        else:
            yumDict[location] = count
    return yumDict

def calc_distance(location, destination):
    x,y = location
    x2,y2 = destination
    x -= x2
    y -= y2
    if x < 0: x*=-1
    if y < 0: y*=-1
    if x > y: return x
    else: return y

def move_to_destination(location, destination, speed):
    x, y = location
    x2, y2 = destination
    if x < x2:
        x += speed
        if x > x2:
            x = x2
    if x > x2:
        x -= speed
        if x < x2:
            x = x2
    if y < y2:
        y += speed
        if y > y2:
            y = y2
    if y > y2:
        y -= speed
        if y < y2:
            y = y2
    newLocation = (x, y)
    return newLocation


def randgen_location(width, length):
    x, y = (random.randint(0, width), random.randint(0, length))
    return (x,y)
def randgen_color():
    r,g,b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return (r,g,b)