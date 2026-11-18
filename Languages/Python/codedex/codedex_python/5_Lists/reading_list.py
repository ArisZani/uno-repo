#LESSON - Variables Exercise 25 (numbering following Codedex)
# -----------------------------------------------------

# TASK: To amend the items in a given list

books = ['Harry Potter',
         '1984',
         'The Fault in Our Stars',
         'The Mom Test',
         'Life in Code'
         ]

books.append('Pachinko')
books.insert(1, 'Fantastic Beasts')
books.remove("The Fault in Our Stars")
books.pop(2)
print(books)