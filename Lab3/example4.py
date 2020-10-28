ticket_price = 3
age= int(input("What is your age?"))

if age<6 and age>60:
  print("It is FREE!")
elif 6<=age and age<= 18:
  print("Your ticket price is", ticket_price - ticket_price/1/2,"TL." )
else:
  print("Your ticket price is", ticket_price,"TL.")

