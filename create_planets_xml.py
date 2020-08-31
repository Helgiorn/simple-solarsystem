import json
from random import seed
from random import *

sol = {}
sol['planets'] = []
sol['planets'].append({
    'id': 2,
    'parentid': 1,
    'type': 2,
    'name': 'Mercury',
    'angle': 20,
    'display_radius': 10,
    'radius': 30000000000.0,
    'size' : 2,
    'color' : [211, 211, 211],
})
sol['planets'].append({
    'id': 3,
    'parentid': 1,
    'type': 2,
    'name': 'Venus',
    'angle': 40,
    'display_radius': 16,
    'radius': 50000000000.0,
    'size' : 4,
    'color' : [0, 0, 150],
})
sol['planets'].append({
    'id': 4,
    'parentid': 1,
    'type': 2,
    'name': 'Earth',
    'angle': 60,
    'display_radius': 22,
    'radius': 60000000000.0,
    'size' : 4,
    'color' : [0, 255, 0],
})

sol['planets'].append({
    'id': 5,
    'parentid': 1,
    'type': 2,
    'name': 'Mars',
    'angle': 80,
    'display_radius': 32,
    'radius': 65000000000.0,
    'size' : 3,
    'color' : [255, 0, 0],
})
sol['planets'].append({
    'id': 6,
    'parentid': 1,
    'type': 2,
    'name': 'Jupiter',
    'angle': 95,
    'display_radius': 180,
    'radius': 160000000000.0,
    'size' : 12,
    'color' : [160, 82, 45],
})
sol['planets'].append({
    'id': 7,
    'parentid': 1,
    'type': 2,
    'name': "Saturn",
    'angle': 15,
    'display_radius': 280,
    'radius': 260000000000.0,
    'size' : 12,
    'color' : [255, 255, 0],
})
sol['planets'].append({
    'id': 8,
    'parentid': 1,
    'type': 2,
    'name': "Uranus",
    'angle': 200,
    'display_radius': 380,
    'radius': 360000000000.0,
    'size' : 8,
    'color' : [211, 211, 211],
})
sol['planets'].append({
    'id': 9,
    'parentid': 1,
    'type': 2,
    'name': 'Neptune',
    'angle': 300,
    'display_radius': 450,
    'radius': 460000000000.0,
    'size' : 8,
    'color' : [0, 0, 150],
})
sol['planets'].append({
    'id': 10,
    'parentid': 1,
    'type': 2,
    'name': 'Pluto',
    'angle': 380,
    'display_radius': 480,
    'radius': 460000000000.0,
    'size' : 4,
    'color' : [212, 158, 120],
})

seed(1)
amount = 400
i = 0
while i <= amount:
    name = "asteroid" + str(i)
    sol['planets'].append({
        'id': i + 11,
        'parentid': 1,
        'type': 3,
        'name': name,
        'angle': randint(0, 300),
        'display_radius': randint(60, 75),
        'radius': 30000000000.0,
        'size' : 1,
        'color' : [211, 211, 211],
    })
    i += 1

with open('planets.json', 'w') as outfile:
    json.dump(sol, outfile)