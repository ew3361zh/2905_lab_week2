"""Part 1: Author class

Create a new class called Author

An Author has a name, and a list of books published

When you create a new Author, they don't have any books. So create an empty books list attribute in __init__

Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list

Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles

Write a main function to test your class, create some example authors, and publish some example books"""

class Author:
#An author has a name and alist of books published but start with empty books list attribute in _init_
    def __init__(self, name): #don't need to include empty list in def init arguments
        self.name = name
        self.books = []

#author class should have a publish method which takes the title of a book as an argument and add title to this object's books list
    def publish(self, title):
        self.books.append(title)

#add _str_ method that returns a String with the author's name, and the names of all their book's titles
    def __str__(self):
        #check if the author has done any books:
        if self.books:
            book_list = ', '.join(self.books) #use join method to put the list in a more readable format for printing
        else:
            book_list = 'No books published...yet'
        # could also do:
        # titles = ', '.join(self.books) or 'No published books'
        # return {titles} instead of {book_list}
        return f'Author name: {self.name}, Published Works: {book_list}'

def main():
    get_name = input('What is the name of an author? ')
    author_name = Author(get_name)
    book_num = int(input('How many books would you like to add to their profile? '))
    for book in range(book_num):
        book_title = input(f'What is the name of book #{book + 1}: ')
        # use specific object name created above to then use the Class function publish and specifically add the books to that object
        author_name.publish(book_title)
    print(author_name)

main()