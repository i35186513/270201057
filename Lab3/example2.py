x = float(input("x:"))
y = float(input("y:"))
z = float(input("z:"))

if x<y and x<z:
  print(x)
elif y<x and y<z:
  print(y)
else:
  print(z)