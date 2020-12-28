def sum_list(x):
  if not isinstance(x,list):
    return x 
  else:
    sum =0
    for a in x :
      sum += sum_list(a)
    return sum

print(sum_list([3, 12, 76, [4, 56, 43], [2,8], 81, 75]))
