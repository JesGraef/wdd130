import math
from datetime import datetime

w = int(input('Enter the width of the tire in mm (ex 205): '))
a= int(input('Enter the aspect ratio of the tire (ex 60): '))
d= int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi * w ** 2 * a) * (w * a + 2540 * d) / 10000000000

print(f'The approximate volume is {volume:.2f} liters.')

current_date_and_time = datetime.now()

# print(f"{current_date_and_time:%Y-%m-%d}")

with open('volumes.txt', 'at') as volumes_file:
    print(f"{current_date_and_time}, {w}, {a}, {d}, {volume}", file=volumes_file)