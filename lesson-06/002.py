# read some value and show its primitive type

value = input('Some value: ')

print('The primitive type of {} is {}\n'.format(value, type(value)))
print('Informations:\n')
print('is numeric: {}'.format(value.isnumeric()))
print('is alpha: {}'.format(value.isalpha()))
print('is alnum: {}'.format(value.isalnum()))

