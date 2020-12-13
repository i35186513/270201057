books= ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD","ENDER'S GAME"]
book_dict ={}
unique_numbers=[]

for i in books:
  print(i)
  length_str= len(i)
  un_str= len(list(set(i)))
  av = ((length_str)+ (un_str))/2
  cur_tuple = (length_str,av, un_str)
  book_dict[i]=cur_tuple

  print(cur_tuple)