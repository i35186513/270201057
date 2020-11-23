n = int(input("how many students:"))

lst = []

for i in range(0,n):
  mex1 = int(input("Enter your midterm 1 :"))
  mex2 = int(input("Enter your midterm 2 :"))
  final = int(input("Enter your final : "))
  av = [mex1*3/10 + mex2*3/10 + final*4/10]
  lst.append([av])
print(lst.append)


