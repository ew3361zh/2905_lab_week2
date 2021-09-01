"""Part 2: Author class - no duplicate books

Start with the program from part 1.

In this version, an author can't publish two books with the same name.

When the publish function is called, print an error message if the book 
given has the same name as a book currently in the books list. (in 
other words, make sure the Author object's book list doesn't already 
contain that name)"""


class Author:
#An author has a name and alist of books published but start with empty books list attribute in _init_
    def __init__(self, name): #don't need to include empty list in def init arguments
        self.name = name
        self.books = []

#author class should have a publish method which takes the title of a book as an argument and add title to this object's books list
    def publish(self, title):
        #case sensitive book title check
        if len(self.books) > 0: # make sure there is at least one book in the list
            book_list_check = [b.lower() for b in self.books] # or this will crash
            if title.lower() in book_list_check:
                print('Sorry, that book is already added, cannot add it again')
            else:
                self.books.append(title)
        else:
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

# main function with inputs to test a variety of data for creating author objects
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