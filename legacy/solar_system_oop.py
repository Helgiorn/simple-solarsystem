import math
import pygame
from PlanetaryObjectManager import PlanetaryObject

TIME_FACTOR = 10000
FRAMES_PER_SECOND = 60

pygame.init()

#Pygame stuff, leave here for now
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LBLUE = (0, 0, 150)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#pygame stuff
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SUN_X = 0.5 * SCREEN_WIDTH
SUN_Y = 0.5 * SCREEN_HEIGHT
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solar System")
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)

#calculated in class
# mercury_angle = 0
# venus_angle = 0
# earth_angle = 0
# mars_angle = 0
# neptune_angle = 0
# moon_angle = 0
# phobos_angle = 0
# deimos_angle = 0

SOLARSYSTEM = []

with open('planets.txt', encoding="utf8") as f:
    for line in f:
        parts = line.split(",")
        if parts[1] != "0":
            SOLARSYSTEM.append(PlanetaryObject(parts[0]))

RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    SCREEN.fill((BLACK))

    pygame.draw.circle(SCREEN, YELLOW, [SUN_X, SUN_Y], 1)

    NEW_ANGLE = 0
    for StarObject in SOLARSYSTEM:
        #if object.type == "0":
        #TODO: Draw sun first
        if StarObject.type != "0":
            NEW_ANGLE = StarObject.angle
            StarObject.angle = NEW_ANGLE + StarObject.radians_per_frame
            StarObject.x = (round((StarObject.orbital_radius * math.cos(StarObject.angle)) + SUN_X, 2))
            StarObject.y = (round((StarObject.orbital_radius * math.sin(StarObject.angle)) + SUN_Y, 2))
            pygame.draw.circle(SCREEN, StarObject.color, [SUN_X, SUN_Y], StarObject.display_radius, width=1)
            print(StarObject.color)
            pygame.draw.circle(SCREEN, StarObject.color, [StarObject.x, StarObject.y], 2)

        #TODO: moon implementation is not ready yet
        # elif object.type == "2":
        #     new_angle = object.angle + object.angle_per_frame
        #     new_x = (round((earth_display_radius * math.cos(earth_angle)) + sun_x, 2))
        #     new_y = (round((earth_display_radius * math.sin(earth_angle)) + sun_y, 2))
        #     earth_moon_orbit_x = object.parent_x
        #     earth_moon_orbit_y = object.parent_y
        #     pygame.draw.circle(screen, white, [earth_moon_x, earth_moon_y], 1)
        #     pygame.draw.circle(screen, white, [earth_moon_orbit_x, earth_moon_orbit_y], moon_display_radius, width=1)

    pygame.display.flip()
    CLOCK.tick(FRAMES_PER_SECOND)

pygame.quit()
quit()
