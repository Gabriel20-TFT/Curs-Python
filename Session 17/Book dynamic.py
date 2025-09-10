class Book:
    def __init__(self, title, author, file_name):
        self.title = title
        self.author = author

        with open(file_name) as book_file:
            self.text = book_file.read()

    def pages(self):
        number_of_rows = 0

        text_rows = self.text.split("\n")
        for row in text_rows:
            number_of_rows += ((len(row) + 1) / 60).__ceil__()

        return ((number_of_rows + 1) / 30).__ceil__()

    def tip(self):
        if self.pages() > 150:
            return "roman"
        else:
            return "nuvela"


if __name__ == "__main__":
    book = Book("Lord of the rings", "Tolkien", "Lord of the rings.txt")

    print(book.pages())
    print(book.tip())
