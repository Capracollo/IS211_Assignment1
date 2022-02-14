#created a class called 'book' and then a function that takes in 2 attributes (title and author).

#created a function that takes in an author and a title, and sets them to the object variables.
class Book:
    author = ""
    title = ""
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
        print(self.title+" written by "+self.author)

#instantiated two objects from this class and then print them by using if __name__ == "__main__"
if __name__ == "__main__":
    book1 = Book("John Steinbeck","Of Mice and Men")
    book2 = Book("Harper Lee","To Kill a Mockingbird")
    book1.display()
    book2.display()