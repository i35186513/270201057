F = int(input("How many numbers:"))
n1=0
n2=1

for sum in range(0,F):
  n3 = n1 + n2
  n1=n2
  n2 = n3
  print(n1)
   