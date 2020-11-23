password= "963tuv"

while True:
  user_entry = input("Enter password: ")
  if user_entry == password:
    print("Welcome")
    break
  elif user_entry == "help" :
    print(password[0])
  else:
    print("Wrong")


user_entry = input("Enter password: ")




