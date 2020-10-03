# calculate the amount of paint needed to paint a wall

width = float(input('Width: '))
height = float(input('Height: '))

print('\n1 liter of paint paints 2m²\n')

area = width * height
print('Area: {}'.format(area))
print('Required amount of ink: {} liters'.format(area / 2))