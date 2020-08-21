import pygame
import math
from PlanetaryObjectManager import PlanetaryObject

TIME_FACTOR = 1000000
FRAMES_PER_SECOND = 60

pygame.init()

#Pygame stuff, leave here for now
screen_width = 1200
screen_height = 1200
black = (0, 0, 0)
gray = (211, 211, 211)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
lblue = (0,0, 150)
blue = (0,0, 255)
red = (255,0,0)

#pygame stuff
sun_x = 0.5 * screen_width
sun_y = 0.5 * screen_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
screen.fill(black)

#calculated in class
mercury_angle = 0
venus_angle = 0
earth_angle = 0
mars_angle = 0
neptune_angle = 0

moon_angle = 0
phobos_angle = 0
deimos_angle = 0

#done in class, iterate through somehowe
mercury = PlanetaryObject(2)

mercury_angle = mercury.angle
mercury_period = mercury.period

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mercury_angle = mercury_angle + mercury.radians_per_frame

    mercury_x = (round((mercury.display_radius * math.cos(mercury_angle)) + sun_x, 2))
    mercury_y = (round((mercury.display_radius * math.sin(mercury_angle)) + sun_y, 2))

    screen.fill((black))

    pygame.draw.circle(screen, yellow, [sun_x, sun_y], 30)
    pygame.draw.circle(screen, white, [sun_x, sun_y], mercury.display_radius, width=1)
    pygame.draw.circle(screen, gray, [mercury_x, mercury_y], 5)

    pygame.display.flip()
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()
quit()