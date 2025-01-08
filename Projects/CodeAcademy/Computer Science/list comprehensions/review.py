single_digits = range(0,10)

squares = []

for i in single_digits:
  squares.append(i*i)
  print(i)

print(squares)

cubes = [i ** 3 for i in single_digits]

print(cubes)

