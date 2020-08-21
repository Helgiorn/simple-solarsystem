import pygame
import math
from PlanetaryObjectManager import PlanetaryObject

TIME_FACTOR = 1000000
FRAMES_PER_SECOND = 60

# pygame.init()

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

solarsystem = []

with open('planets.txt', encoding="utf8") as f:
    for line in f:
        parts = line.split(",")
        solarsystem.append(PlanetaryObject(parts[0]))

for object in solarsystem:
    print (object.name)


# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


#     earth_angle = earth_angle + earth.angle_per_frame
#     moon_angle = moon_angle + moon.angle_per_frame

#     earth_x = (round((earth_display_radius * math.cos(earth_angle)) + sun_x, 2))
#     earth_y = (round((earth_display_radius * math.sin(earth_angle)) + sun_y, 2))
 
#     earth_moon_x = (round((moon_display_radius * math.cos(moon_angle)) + earth_x, 2))
#     earth_moon_y = (round((moon_display_radius * math.sin(moon_angle)) + earth_y, 2))
#     earth_moon_orbit_x = earth_x
#     earth_moon_orbit_y = earth_y

#     screen.fill((black))

#     pygame.draw.circle(screen, yellow, [sun_x, sun_y], 30)
   
#     pygame.draw.circle(screen, white, [sun_x, sun_y], earth_display_radius, width=1)
#     pygame.draw.circle(screen, blue, [earth_x, earth_y], 5)

#     pygame.draw.circle(screen, white, [earth_moon_x, earth_moon_y], 1)
#     pygame.draw.circle(screen, white, [earth_moon_orbit_x, earth_moon_orbit_y], moon_display_radius, width=1)

#     pygame.display.flip()
#     clock.tick(FRAMES_PER_SECOND)

# pygame.quit()
# quit()