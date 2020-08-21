import pygame
import math
#from PlanetaryObjectManager import PlanetaryObjectManager

#move to file then comment out
GRAVITATIONAL_CONSTANT = 6.7 * math.pow(10, -11)
MERCURY_RADIUS = 0.3 * math.pow(10, 11)
VENUS_RADIUS = 0.5 * math.pow(10, 11)
EARTH_RADIUS = 0.6 * math.pow(10, 11)
MARS_RADIUS = 0.65 * math.pow(10, 11)
NEPTUNE_RADIUS = 4.5 * math.pow(10, 12)
MOON_RADIUS = 3.8 * math.pow(10, 8)
PHOBOS_RADIUS = 3.8 * math.pow(10, 8)
DEIMOS_RADIUS = 3.8 * math.pow(10, 8)
MASS_OF_THE_SUN = 2.0 * math.pow(10, 30)
MASS_OF_THE_EARTH = 6.0 * math.pow(10, 24)
MASS_OF_THE_MARS = 6.0 * math.pow(10, 24)


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

#move to text, then comment out
mercury_display_radius = 40
venus_display_radius = 70
earth_display_radius = 100
mars_display_radius = 150
neptune_display_radius = 300
moon_display_radius = 10
phobos_display_radius = 5
deimos_display_radius = 10

#pygame stuff
sun_x = 0.5 * screen_width
sun_y = 0.5 * screen_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
screen.fill(black)

#use class function
def calculate_simulation_period(radius, central_mass):
    period = (2 * math.pi * math.pow(radius, 3 / 2)) / math.pow(GRAVITATIONAL_CONSTANT * central_mass, 1 / 2)
    accelerated_period = period / TIME_FACTOR
    return round(accelerated_period, 2)

def angle_per_frame(period):
    total_frames = period * FRAMES_PER_SECOND
    # Multiply by minus one so we orbit counter-clockwise
    radians_per_frame = -1 * (2 * math.pi) / total_frames
    return radians_per_frame

#calculated in class
mercury_angle = 55
venus_angle = 150
earth_angle = 200
mars_angle = 0
neptune_angle = 10

moon_angle = 0
phobos_angle = 50
deimos_angle = 0

#done in class, iterate through somehowe
venus_period = calculate_simulation_period(VENUS_RADIUS, MASS_OF_THE_SUN)
venus_angle_per_frame = angle_per_frame(venus_period)

mercury_period = calculate_simulation_period(MERCURY_RADIUS, MASS_OF_THE_SUN)
mercury_angle_per_frame = angle_per_frame(mercury_period)

earth_period = calculate_simulation_period(EARTH_RADIUS, MASS_OF_THE_SUN)
earth_angle_per_frame = angle_per_frame(earth_period)

mars_period = calculate_simulation_period(MARS_RADIUS, MASS_OF_THE_SUN)
mars_angle_per_frame = angle_per_frame(mars_period)

neptune_period = calculate_simulation_period(NEPTUNE_RADIUS, MASS_OF_THE_SUN)
neptune_angle_per_frame = angle_per_frame(neptune_period)

moon_period = calculate_simulation_period(MOON_RADIUS, MASS_OF_THE_EARTH)
moon_angle_per_frame = angle_per_frame(moon_period)

phobos_period = calculate_simulation_period(PHOBOS_RADIUS, MASS_OF_THE_MARS)
phobos_angle_per_frame = angle_per_frame(phobos_period)
deimos_period = calculate_simulation_period(DEIMOS_RADIUS, MASS_OF_THE_MARS)
deimos_angle_per_frame = angle_per_frame(deimos_period)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mercury_angle = mercury_angle + mercury_angle_per_frame
    venus_angle = venus_angle + venus_angle_per_frame
    earth_angle = earth_angle + earth_angle_per_frame
    mars_angle = mars_angle + mars_angle_per_frame
    neptune_angle = neptune_angle + neptune_angle_per_frame

    moon_angle = moon_angle + moon_angle_per_frame
    phobos_angle = phobos_angle + phobos_angle_per_frame
    deimos_angle = deimos_angle + deimos_angle_per_frame

    venus_x = (round((venus_display_radius * math.cos(venus_angle)) + sun_x, 2))
    venus_y = (round((venus_display_radius * math.sin(venus_angle)) + sun_y, 2))

    mercury_x = (round((mercury_display_radius * math.cos(mercury_angle)) + sun_x, 2))
    mercury_y = (round((mercury_display_radius * math.sin(mercury_angle)) + sun_y, 2))

    earth_x = (round((earth_display_radius * math.cos(earth_angle)) + sun_x, 2))
    earth_y = (round((earth_display_radius * math.sin(earth_angle)) + sun_y, 2))

    mars_x = (round((mars_display_radius * math.cos(mars_angle)) + sun_x, 2))
    mars_y = (round((mars_display_radius * math.sin(mars_angle)) + sun_y, 2))

    neptune_x = (round((neptune_display_radius * math.cos(neptune_angle)) + sun_y, 2))
    neptune_y = (round((neptune_display_radius * math.sin(neptune_angle)) + sun_y, 2))

    earth_moon_x = (round((moon_display_radius * math.cos(moon_angle)) + earth_x, 2))
    earth_moon_y = (round((moon_display_radius * math.sin(moon_angle)) + earth_y, 2))
    earth_moon_orbit_x = earth_x
    earth_moon_orbit_y = earth_y

    mars_phobos_x = (round((phobos_display_radius * math.cos(phobos_angle)) + mars_x, 2))
    mars_phobos_y = (round((phobos_display_radius * math.sin(phobos_angle)) + mars_y, 2))
    mars_phobos_orbit_x = mars_x
    mars_phobos_orbit_y = mars_y

    mars_deimos_x = (round((deimos_display_radius * math.cos(deimos_angle)) + mars_x, 2))
    mars_deimos_y = (round((deimos_display_radius * math.sin(deimos_angle)) + mars_y, 2))
    mars_deimos_orbit_x = mars_x
    mars_deimos_orbit_y = mars_y

    screen.fill((black))

    pygame.draw.circle(screen, yellow, [sun_x, sun_y], 30)
    pygame.draw.circle(screen, white, [sun_x, sun_y], venus_display_radius, width=1)
    pygame.draw.circle(screen, lblue, [venus_x, venus_y], 5)
    pygame.draw.circle(screen, white, [sun_x, sun_y], mercury_display_radius, width=1)
    pygame.draw.circle(screen, gray, [mercury_x, mercury_y], 5)
    pygame.draw.circle(screen, white, [sun_x, sun_y], earth_display_radius, width=1)
    pygame.draw.circle(screen, blue, [earth_x, earth_y], 5)
    pygame.draw.circle(screen, white, [sun_x, sun_y], mars_display_radius, width=1)
    pygame.draw.circle(screen, red, [mars_x, mars_y], 5)

    pygame.draw.circle(screen, white, [earth_moon_x, earth_moon_y], 1)
    pygame.draw.circle(screen, white, [earth_moon_orbit_x, earth_moon_orbit_y], moon_display_radius, width=1)

    pygame.draw.circle(screen, white, [mars_phobos_x, mars_phobos_y], 1)
    pygame.draw.circle(screen, white, [mars_phobos_orbit_x, mars_phobos_orbit_y], phobos_display_radius, width=1)

    pygame.draw.circle(screen, white, [mars_deimos_x, mars_phobos_y], 1)
    pygame.draw.circle(screen, white, [mars_deimos_orbit_x, mars_deimos_orbit_y], deimos_display_radius, width=1)

    pygame.draw.circle(screen, white, [sun_x, sun_y], neptune_display_radius, width=1)
    pygame.draw.circle(screen, blue, [neptune_x, neptune_y], 10)

    pygame.display.flip()
    clock.tick(FRAMES_PER_SECOND)

pygame.quit()
quit()