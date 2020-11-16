a = int(input("Enter number 1:"))
b= int(input("Enter number 2:"))

match = 0

while a>0 and b>0:
  if a%10 == b%10:
    match += 1
  
  a//= 10
  b//= 10
print(match)