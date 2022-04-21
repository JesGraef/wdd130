import math

items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

answer = math.ceil(items/items_per_box)
# answer = math.ceil(answer)

print(f'For {items} items, packing {items_per_box} items in each box, you will need {answer} boxes.')