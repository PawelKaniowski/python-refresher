from vehicle import Vehicle
boat = Vehicle.water_vehicle("Minnow", (30, 40, 10))
print(boat.name)

print(boat.num_wheels)

print(boat.volume())

car = Vehicle.road_vehicle("Kitt", (4, 3, 1.5), 4)
print(car.name)

print(car.num_wheels)

print(car.volume())

print(Vehicle.all_float(boat))

print(Vehicle.all_float(boat, boat))

print(Vehicle.all_float(boat, boat, car))

