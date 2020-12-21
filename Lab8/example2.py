

def is_prime(n):
  i=2
  while i*i <= n :
    if n%i ==0:
      return False
    i +=1
  return True

def print_primes_between(n,m):
  for i in range(n,m):
    if is_prime(i):
      print(i)

first_int = int(input("First integer : "))
second_int = int(input("Second integer : "))
print_primes_between(first_int,second_int)
