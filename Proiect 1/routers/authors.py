import csv

from fastapi import APIRouter, HTTPException

from models import AuthorModel

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get('')
def get_authors():
    with open('db/authors.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        return [AuthorModel(**author) for author in csv_dict_reader]


@router.get('/{full_name}')
def get_authors_by_name(full_name: str):
    with open('db/authors.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        authors = [AuthorModel(**author) for author in csv_dict_reader if
                            full_name.lower() in author['full_name'].lower()]
        if len(authors) == 0:
            raise HTTPException(status_code=404, detail="Authors not found")
        return authors


@router.post('/create')
def create_author(new_author: AuthorModel):
    with open('db/authors.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())

        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["author_id", "full_name", "birth_year"])
        csv_dict_writer.writerow(
            {"author_id": lines, "full_name": new_author.full_name, "birth_year": new_author.birth_year})
        return "Added author successfully"
