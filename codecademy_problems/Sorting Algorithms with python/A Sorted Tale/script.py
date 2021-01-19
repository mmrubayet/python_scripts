import utils
import sorts

# Comparison function here

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

# Comparison functions end

'''
bookshelf = utils.load_books('books_small.csv')
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort_1:
  print(book['title'])
'''

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf, by_author_ascending)

for book in sort_2:
  print(book['title'])
