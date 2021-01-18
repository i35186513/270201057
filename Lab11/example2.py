def binarysearch(a, lst):
  low = 0
  high = len(lst)-1
  while low <= high:
    mid = (low+high)//2
    item = lst[mid]
    if a == item:
      return mid
    elif a < mid:
      high = mid - 1
    else:
      low = mid + 1 
  return -1

print(binarysearch(5, [ 2, 3, 4, 10, 40 ]))