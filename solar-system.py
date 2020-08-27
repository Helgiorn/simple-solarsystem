import math
import pygame
from sol_gen import PlanetaryObject

#move to file then comment out
GRAVITATIONAL_CONSTANT = 6.7 * math.pow(10, -11)
# MERCURY_RADIUS = 0.3 * math.pow(10, 11)
# VENUS_RADIUS = 0.5 * math.pow(10, 11)
# EARTH_RADIUS = 0.6 * math.pow(10, 11)
# MARS_RADIUS = 0.65 * math.pow(10, 11)
# NEPTUNE_RADIUS = 4.5 * math.pow(10, 12)
# MOON_RADIUS = 3.8 * math.pow(10, 8)
# PHOBOS_RADIUS = 3.8 * math.pow(10, 8)
# DEIMOS_RADIUS = 3.8 * math.pow(10, 8)
MASS_OF_THE_SUN = 2.0 * math.pow(10, 30)
MASS_OF_THE_EARTH = 6.0 * math.pow(10, 24)
MASS_OF_THE_MARS = 6.0 * math.pow(10, 24)
screen_width = 1600
screen_height = 1200
sun_x = 0.5 * screen_width
sun_y = 0.5 * screen_height

TIME_FACTOR = 10000000
FRAMES_PER_SECOND = 60

pygame.init()

#Pygame stuff, leave here for now
black = (0, 0, 0)
gray = (211, 211, 211)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
lblue = (0,0, 150)
blue = (0,0, 255)
red = (255,0,0)

#pygame stuff

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
screen.fill(black)

#use class function
def calculate_simulation_period(radius, central_mass):
    period = (2 * math.pi * math.pow(radius, 3 / 2)) / math.pow(GRAVITATIONAL_CONSTANT * central_mass, 1 / 2)
    accelerated_period = period / TIME_FACTOR
    # return round(accelerated_period, 2)
    return accelerated_period

def angle_per_frame(period):
    total_frames = period * FRAMES_PER_SECOND
    # Multiply by minus one so we orbit counter-clockwise
    radians_per_frame = -1 * (2 * math.pi) / total_frames
    return radians_per_frame
###
SOLARSYSTEM = []

with open('planets.txt', encoding="utf8") as f:
    for line in f:
        parts = line.split(",")
        if parts[1] != "0":
            SOLARSYSTEM.append(PlanetaryObject(parts[0]))

for STAR_OBJECT in SOLARSYSTEM:
    if STAR_OBJECT.name == "Earth":
        period = calculate_simulation_period(STAR_OBJECT.radius, MASS_OF_THE_SUN)
        print (period)
        STAR_OBJECT.update_period(period)
        print (STAR_OBJECT.period)
        STAR_OBJECT.angle_per_frame = angle_per_frame(STAR_OBJECT.period)
        print (STAR_OBJECT.angle_per_frame)
        print (float(STAR_OBJECT.angle_per_frame) + float(STAR_OBJECT.angle))

###
running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((black))
#     pygame.draw.circle(screen, yellow, [sun_x, sun_y], 30)

#     for STAR_OBJECT in SOLARSYSTEM:
#         STAR_OBJECT.update_angle_tick()

#         if STAR_OBJECT.name == "Earth":
#             print (STAR_OBJECT.angle)

#         x = (round((STAR_OBJECT.display_radius * math.cos(STAR_OBJECT.angle)) + sun_x, 2))
#         y = (round((STAR_OBJECT.display_radius * math.sin(STAR_OBJECT.angle)) + sun_y, 2))
#         STAR_OBJECT.update_x(x)
#         STAR_OBJECT.update_y(y)

#         pygame.draw.circle(screen, white, [sun_x, sun_y], STAR_OBJECT.display_radius, width=1)
#         pygame.draw.circle(screen, white, [STAR_OBJECT.x, STAR_OBJECT.y], 2)


#     pygame.display.flip()
#     clock.tick(FRAMES_PER_SECOND)

# pygame.quit()
# quit()