gpa = float(input("enter your gpa:"))
lecture  = int(input("enter your number of lecture:"))
if lecture < 47 and gpa < 2.0:
  print("Not enough number of lectures and gpa.")
elif lecture < 47 and gpa>= 2.0:
  print("not enough number of lectures.")
elif lecture > 47 and gpa <2.0:
  print("not enough gpa.")
else: 
  print("GRADUATED")