import json

sol = {}
sol['planets'] = []
sol['planets'].append({
    'id': 2,
    'parentid': 1,
    'type': 2,
    'name': 'Mercury',
    'angle': 20,
    'display_radius': 30,
    'radius': 30000000000.0,
})
sol['planets'].append({
    'id': 3,
    'parentid': 1,
    'type': 2,
    'name': 'Venus',
    'angle': 40,
    'display_radius': 70,
    'radius': 50000000000.0,
})
sol['planets'].append({
    'id': 4,
    'parentid': 1,
    'type': 2,
    'name': 'Earth',
    'angle': 60,
    'display_radius': 100,
    'radius': 60000000000.0,
})

sol['planets'].append({
    'id': 5,
    'parentid': 1,
    'type': 2,
    'name': 'Mars',
    'angle': 80,
    'display_radius': 150,
    'radius': 65000000000.0,
})
sol['planets'].append({
    'id': 6,
    'parentid': 1,
    'type': 2,
    'name': 'Jupiter',
    'angle': 95,
    'display_radius': 200,
    'radius': 160000000000.0,
})
sol['planets'].append({
    'id': 6,
    'parentid': 1,
    'type': 2,
    'name': 'Jupiter',
    'angle': 95,
    'display_radius': 200,
    'radius': 160000000000.0,
})
sol['planets'].append({
    'id': 7,
    'parentid': 1,
    'type': 2,
    'name': "Saturn",
    'angle': 15,
    'display_radius': 250,
    'radius': 260000000000.0,
})
sol['planets'].append({
    'id': 8,
    'parentid': 1,
    'type': 2,
    'name': "Uranus",
    'angle': 200,
    'display_radius': 300,
    'radius': 360000000000.0,
})
sol['planets'].append({
    'id': 9,
    'parentid': 1,
    'type': 2,
    'name': 'Neptune',
    'angle': 300,
    'display_radius': 350,
    'radius': 460000000000.0,
})
sol['planets'].append({
    'id': 10,
    'parentid': 1,
    'type': 2,
    'name': 'Pluto',
    'angle': 330,
    'display_radius': 380,
    'radius': 460000000000.0,
})

with open('planets.json', 'w') as outfile:
    json.dump(sol, outfile)