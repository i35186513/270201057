n = int(input("how many students:"))
aa_lst=[]
grade_lst = []
av_lst=[]
for i in range(0,n):
  print("student",str(i+1))
  mex1 = int(input("Enter your midterm 1 :"))
  mex2 = int(input("Enter your midterm 2 :"))
  final = int(input("Enter your final : "))
  av = mex1*3/10 + mex2*3/10 + final*4/10
  #av_lst.append([mex1*3/10 + mex2*3/10 + final*4/10]) 
  if av>=90:
    aa_lst.append([av])
print(aa_lst)
