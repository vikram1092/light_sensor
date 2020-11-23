from gpiozero import LightSensor
from light_switch import toggle_light

class People:
    count = 0
    def __init__(self, new_count):
        count = new_count

people = People(0)

def light_break_detected():
    if people.count > 0:
        toggle_light(True)
    else:
        toggle_light(False)

def set_first_switch(value):
    switch_one = value
    switch_two = sensor_two.light_detected
    print('Switch one: ' + str(sensor_one.value))

    # Decrease count to a minimum of zero if sensor two has been triggered already and toggle light
    if (not switch_one and not switch_two):
        new_count = max(0, people.count - 1)
        people.count = new_count
        print('Switch one: ' + str(people.count))
        light_break_detected()

def set_second_switch(value):
    switch_two = value
    switch_one = sensor_one.light_detected
    print('Switch two: ' + str(sensor_two.value))

    # Increase count if sensor one has been triggered already and toggle light
    if (not switch_one and not switch_two):
        people.count += 1
        print('Switch two: ' + str(people.count))
        light_break_detected()

sensor_one = LightSensor(4, 5, 0.01, 0.01)
sensor_one.when_dark = lambda: set_first_switch(False)
sensor_one.when_light = lambda: set_first_switch(True)

sensor_two = LightSensor(9, 5, 0.01, 0.01)
sensor_two.when_dark = lambda: set_second_switch(False)
sensor_two.when_light = lambda: set_second_switch(True)

while True:
    if sensor_one.light_detected != True and sensor_two.light_detected != True:
        continue
        print('Light break with people:' + str(people.count))