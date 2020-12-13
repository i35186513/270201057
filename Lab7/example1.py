#name = str(input("Enter name:"))
#age = int(input("Enter age:"))
a = dict((("Jon",15), ("Ned", 45), ("Arya",9), ("Catelyn",44),("Bran",10)))

for cur_key in a.keys():
  if (a[cur_key]>18):
   print(a)

dict_exmple = dict((("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)))

for cur_key in dict_exmple.keys():
  if(dict_exmple[cur_key] > 18):
    print(cur_key)
