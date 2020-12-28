'''
def hailstone(x):
  if x==2:
    return 1
  else:
    if x%2==0:
      x = x/2
    else:
      x = 3*x+1

    return x + hailstone(x)

print(hailstone(5))
#this gives the sum of all integers except starting parameter
'''
def hailstone(x):
  s =str(x)
  if x==1:
    return s
  if x%2==0:
    return s+","+hailstone(x//2)
  else:
    return s+","+hailstone((3*x)+1)

print(hailstone(5))