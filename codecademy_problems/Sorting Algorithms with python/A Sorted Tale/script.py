import utils
import sorts

# Comparison function here

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

# Comparison functions end


bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

sort_2 = sorts.bubble_sort(bookshelf, by_author_ascending)

'''
for book in sort_1:
  print(book['title'])

for book in sort_2:
  print(book['author'])

'''
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in bookshelf_v2:
  print(book['author'])
