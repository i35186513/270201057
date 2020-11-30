N = int(input("how many numbers do you have?"))
user_input = (input("Enter the numbers:"))
lst=[]

unique_list=[]
for i in range(0,N-1):
  print(int(input("Enter the numbers:")))
lst.append(user_input)
print(lst)

for i in lst :
  repeat = lst.count(i)
  if repeat==0:
    unique_list.append(i)
  else:
    break

print(unique_list)




