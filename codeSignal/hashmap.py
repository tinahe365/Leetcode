# Python program based on the scenario of counting books in a library
books = ['mystery', 'sci-fi', 'mystery', 'fantasy', 'sci-fi', 'romance']
books_count = {}

for book in books:
    # if book in books_count:
    #     books_count[book] += 1
    # else:
    #     books_count[book] = 1
    books_count[book] = books_count.get(book, 0) + 1

print(books_count)