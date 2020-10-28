a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
delta =(b**2 - 4*a*c)
x1= (-b - delta**1/2)/ (2*a)
x2= (-b + delta**1/2)/ (2*a)
#U will find the exact value of x1 and x2,whatever it is complex or not.
#So when you enter a,b,c for any equation which doesnt have any reel root,x1 and x2 will give u the complex numbers...
#whose i's part representing by j in computer. for example 5+3i is same thing as 5.0+3.0j.
#Therefore, you dont need to write any special 'elif'statement for delta<0.
#Here is the code, u can easily understand.
if delta>0:
 print('There are two reel roots:',x1,x2)
elif delta==0:
 print('There is only one reel root:',x1)
#This 'else'statement will be executed when only delta<0.:
else:
 print('No reel roots,two complex roots:',x1,x2) 
