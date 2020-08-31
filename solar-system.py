import json
import math
import pygame
from sol_gen import PlanetaryObject

GRAVITATIONAL_CONSTANT = 6.7 * math.pow(10, -11)
MASS_OF_THE_SUN = 2.0 * math.pow(10, 30)
MASS_OF_THE_EARTH = 6.0 * math.pow(10, 24)
MASS_OF_THE_MARS = 6.0 * math.pow(10, 24)
yellow = (255, 255, 0)
black = (0, 0, 0)
gray = (211,211,211)
screen_width = 2560
screen_height = 1440
sun_x = 0.5 * screen_width
sun_y = 0.5 * screen_height
TIME_FACTOR = 100000
FRAMES_PER_SECOND = 60

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
screen.fill(black)


def calculate_simulation_period(radius, central_mass):
    period = (2 * math.pi * math.pow(radius, 3 / 2)) / math.pow(GRAVITATIONAL_CONSTANT * central_mass, 1 / 2)
    accelerated_period = period / TIME_FACTOR
    return round(accelerated_period, 2)

def angle_per_frame(period):
    total_frames = period * FRAMES_PER_SECOND
    # Multiply by minus one so we orbit counter-clockwise
    radians_per_frame = -1 * (2 * math.pi) / total_frames
    return radians_per_frame


SOLARSYSTEM = []
with open('planets.json') as json_file:
    data = json.load(json_file)
    for p in data['planets']:
        if p['type'] == 2 or 3:
            SOLARSYSTEM.append(PlanetaryObject(p['id']))
        

for StarObject in SOLARSYSTEM:
    period = calculate_simulation_period(StarObject.radius, MASS_OF_THE_SUN)
    StarObject.update_period(period)
    angle_tick = angle_per_frame(period)
    StarObject.update_angle_per_frame(angle_tick)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((black))
    pygame.draw.circle(screen, yellow, [sun_x, sun_y], 25)

    for StarObject in SOLARSYSTEM:
        StarObject.update_tick()
        star_x = (round((float(StarObject.display_radius) * math.cos(float(StarObject.angle))) + sun_x, 2))
        star_y = (round((float(StarObject.display_radius) * math.sin(float(StarObject.angle))) + sun_y, 2))
        StarObject.update_x(star_x)
        StarObject.update_y(star_y)

        if StarObject.type != 3:
            pygame.draw.circle(screen, gray, [sun_x, sun_y], StarObject.display_radius, width=1)
            pygame.draw.circle(screen, StarObject.color, [StarObject.x, StarObject.y], StarObject.size)
        else: pygame.draw.circle(screen, StarObject.color, [StarObject.x, StarObject.y], StarObject.size)


    pygame.display.flip()
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()
quit()