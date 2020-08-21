import math

class PlanetaryObjectManager(id):
    pass
    def __init__(self):
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
    
    def read_object(id):
        pass

    def calculate_mass(mass):
        self.mass = mass * math.pow(10, 24)
    
    def calculate_simulation_period(radius, central_mass):
        period = (2 * math.pi * math.pow(radius, 3 / 2)) / math.pow(GRAVITATIONAL_CONSTANT * central_mass, 1 / 2)
        accelerated_period = period / TIME_FACTOR
        self.period = round(accelerated_period, 2)

    def angle_per_frame(period):
        total_frames = period * FRAMES_PER_SECOND
        # Multiply by minus one so we orbit counter-clockwise
        self.radians_per_frame = -1 * (2 * math.pi) / total_frames