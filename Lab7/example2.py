books= ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD","ENDER'S GAME"]
book_dict ={}
unique_numbers=[]

for i in books:
  print(i)
  length_str= len(i)
  un_str= len(list(set(i)))
  
  cur_tuple = (length_str, un_str)
  book_dict[i]=cur_tuple

  print(cur_tuple)

