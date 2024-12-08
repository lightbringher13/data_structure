list1 = [1, 0, -1]
# len function is predefined for type list
print(len(list1))
print(list1)
print(type(list1))


class Author:
    def __init__(self, name, book_name, pages):
        self.book_name = book_name
        self.pages = pages
        self.name = name

    # manually define the len function for user defined class
    def __str__(self):
        return f"{self.book_name} by {self.name} with {self.pages}"

    def __len__(self):
        return self.pages

    def __call__(self, *args, **kwds):
        print("hi object is called")

    def __del__(self):
        print("Author has been deleted")


d = Author("riss", "my life", 300)
print(len(d))
print(d)
d()
del d
print(d)
