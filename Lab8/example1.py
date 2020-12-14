
def summ(a_list):

  a_sum = 0
  for i in range(len(a_list)):
    a_sum += i
  return a_sum 

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
a_sum = summ(a_list)
print(a_sum*a_sum)

