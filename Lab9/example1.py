num = int(input("Enter a number:"))
'''
def harmonic(n):
  summ= 0 
  if n == 1:
    summ = 1
  elif n >= 2:
    summ = summ + 1/n
    return harmonic(n-1)
  return summ

print(harmonic(num))
'''

def harmonic(n): 
  if n == 1:
    return 1
  return 1/n + harmonic(n-1)

print(harmonic(num))