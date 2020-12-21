lst = [1, 2, 3, 4]
reversed_list = []
#print(lst.index(2))
'''
def get_reversed(n):
  if len(n)==0:
    return []
  
  return reversed_list.append(n.index(len(n)-1))

get_reversed([1, 2, 3, 4])
'''

def get_reversed(n):
  if len(n)==0:
    return []
  return [n.pop()] + get_reversed(n)

print(get_reversed(lst))