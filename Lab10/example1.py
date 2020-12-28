def mult3(n):
  if n ==0:
    return 0
  else:
    return mult3(n-1)+3

print(mult3(6))
