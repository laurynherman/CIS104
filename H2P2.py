book_title = input('Please enter your books title:')
book_author = input('Please enter your books author:')
yr_of_pub = int(input('Please enter the year this book was published:'))
num_of_pgs = int(input('Please enter the number of pages in this book:'))
book_age = int(2019 - yr_of_pub)
print('The age of this book is:', book_age)

if book_age < 10:
    print('This book is younger than ten years old.')
if book_age > 10:
      print('This book is at least ten years old.')

if num_of_pgs < 100:
    print('This book is a short book.')
if num_of_pgs < 300:
    print('This book is an average book.')
if num_of_pgs > 300:
    print('This book is a long book.')
