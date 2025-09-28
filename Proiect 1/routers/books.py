import csv

from fastapi import APIRouter, HTTPException

from models import BookModel, BookPlainModel

router = APIRouter(prefix="/books", tags=["books"])


@router.get('')
def get_books():
    with open('db/books.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        return [BookPlainModel(**book).to_author_name() for book in csv_dict_reader]


@router.get('/{title}')
def get_books_by_title(title: str):
    with open('db/books.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        books = [BookPlainModel(**book).to_author_name() for book in csv_dict_reader if
                 title.lower() in book['title'].lower()]
        if len(books) == 0:
            raise HTTPException(status_code=404, detail="Books not found")
        return books


@router.post('/create')
def create_book(new_book: BookModel):
    new_book = new_book.to_author_id()
    if new_book is None:
        raise HTTPException(status_code=404, detail="Author name not found")
    with open('db/books.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())

        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["book_id", "title", "genre", "author_id"])
        csv_dict_writer.writerow(
            {"book_id": lines, "title": new_book.title, "genre": new_book.genre, "author_id": new_book.author_id})
        return "Added author successfully"
