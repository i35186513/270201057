the_num = (int(input("Enter a number: ")))

if the_num<10:
  print(the_num)
else:
  ones = the_num % 10
  tens = (the_num//10) % 10
  total = ones + tens
  print("The sum of the last two digits:",total)

