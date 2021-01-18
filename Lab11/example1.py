def selectionsort(lst):
 
  for bottom in range(len(lst)-1):
    mp = bottom 
    for i in range(bottom+1,len(lst)):
      if lst[i] < lst[mp]:
        mp = i      
    lst[bottom], lst[mp] = lst[mp], lst[bottom]

lst = [13, 4, 9, 5, 3, 16, 12]
print(selectionsort(lst))

#lab örneğiyle aynı yazmış olduğumu düşünüyorum ama neden none çıktısını verior anlayamıyorum. 