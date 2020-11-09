a = int(input("Enter the base:"))
b = int(input("Enter the exponent: "))
power = 1

if b> 0 :
   for i in range(b):
     power*= a
else:
  for i in range(0, b, -1):
    power /= a

print(power)



