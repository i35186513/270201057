def binary_to_decimal(n):
  binary = int("")
  decimal, i, n = 0, 0, 0
  while binary != 0:
    dec= binary % 10  
    decimal+= dec * pow(2,i)
    binary = binary//10
    i += 1
    print(binary_to_decimal(n))
    return(n)



binary_to_decimal(10010)