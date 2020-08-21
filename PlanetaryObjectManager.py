import math

def class PlanetaryObjectManager(self, id):
    def __init__(self)
        self.id = id
        self.parentid = ""
        self.name = ""
        self.color = ""
        self.radius = ""
        self.display_radius = ""
        self.angle = ""
        self.mass = ""
        self.period = ""
        self.radians_per_frame = ""
        
        #these need inheritance, static in class for now
        self.FRAMES_PER_SECOND = 60
        self.TIME_FACTOR = 1000000
        self.GRAVITATIONAL_CONSTANT = 6.7 * math.pow(10, -11)
    
    def read_object(id)
        pass

    def calculate_mass(mass)
        self.mass = mass * math.pow(10, 24)
    
    def calculate_simulation_period(radius, central_mass):
        period = (2 * math.pi * math.pow(radius, 3 / 2)) / math.pow(GRAVITATIONAL_CONSTANT * central_mass, 1 / 2)
        accelerated_period = period / TIME_FACTOR
        self.period = round(accelerated_period, 2)

    def angle_per_frame(period):
        total_frames = period * FRAMES_PER_SECOND
        # Multiply by minus one so we orbit counter-clockwise
        self.radians_per_frame = -1 * (2 * math.pi) / total_frames










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