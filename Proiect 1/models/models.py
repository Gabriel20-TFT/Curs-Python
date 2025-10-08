import csv

from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str


class AuthorModel(BaseModel):
    full_name: str
    birth_year: int


class BookPlainModel(BaseModel):
    title: str
    genre: str
    author_id: str

    def to_author_name(self):
        with open('db/authors.csv', "r", newline="", encoding="utf-8") as csvfile:
            csv_dict_reader = csv.DictReader(csvfile)
            for author in csv_dict_reader:
                if author["author_id"] == self.author_id:
                    return BookModel(title=self.title, genre=self.genre, author_name=author["full_name"])
            return None


class BookModel(BaseModel):
    title: str
    genre: str
    author_name: str

    def to_author_id(self):
        with open('db/authors.csv', "r", newline="", encoding="utf-8") as csvfile:
            csv_dict_reader = csv.DictReader(csvfile)
            for author in csv_dict_reader:
                if author["full_name"] == self.author_name:
                    return BookPlainModel(title=self.title, genre=self.genre, author_id=author["author_id"])
            return None
