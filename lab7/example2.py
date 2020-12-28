books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
letters_set = set()

for i in books:
  letters_set.add(i)
  book_dict[i] = len(i),len(letters_set)
print(book_dict)

  

  

  

