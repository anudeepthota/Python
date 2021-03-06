# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "E-BOOK")

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if(booktype not in Book.BOOK_TYPES):
            raise ValueError(booktype+" is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types are : ", Book.BOOK_TYPES)

# TODO: Create some book instances
b1 = Book("Title 1", "E-BOOK")
b2 = Book("Title 2", "Notebook")

# TODO: Use the static method to access a singleton object
