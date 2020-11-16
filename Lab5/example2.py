N = int(input("How many numbers ? "))
print(N)
evens = 0
for i in range(N):
  number = int(input("Enter an integer:"))
  if number %2==0:
     evens += 1
print( evens/N * 100, "%")