def selectionsort(lst):
  if len(lst)== 0:
    lst = []
  else:
    for i in range(len(lst)-1):
      minimum = i
      for j in range(1,len(lst)):
        if lst[i] > lst[j]:
          minimum = j
     
      if minimum !=i:
        temp = lst[i]
        lst[i] = lst[minimum]
        lst[minimum] = temp
      
    return lst

array = [13, 4, 9, 5, 3, 16, 12]
print(selectionsort(array))