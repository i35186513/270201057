email = "ceng113@example.com"
user_mail = (input("Enter your mail:"))
user_mail = user_mail.lower()


if "@" in email:
  part_1 = email.split("@")[0]
  part_1 = part_1.replace(".", "")
  part_2 = email.split("@")[1]
  email=part_1 +"@"+ part_2

if email == user_mail:
  print("equal")
else:
  print("not equal")