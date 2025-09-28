import csv

from fastapi import APIRouter, HTTPException

from models import UserModel

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post('/{title}')
def loan_book(title: str, login_user: UserModel):
    with open('db/users.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        users = list(csv_dict_reader)
        for user in users:
            if user["username"].lower() == login_user.username.lower():
                if user["password"] == login_user.password:
                    break
                else:
                    raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=401, detail="Non existing user")

    with open('db/books.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for book in csv_dict_reader:
            if book['title'] == title:
                break
        else:
            raise HTTPException(status_code=404, detail="Book not found")

    with open('db/loans.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for loan in csv_dict_reader:
            if loan['book_id'] == book['book_id'] and loan["returned"] == "False":
                raise HTTPException(status_code=422, detail="Book is still loaned")

    with open('db/loans.csv', "a", newline="", encoding="utf-8") as csvfile:
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["book_id", "user_id", "returned"])
        csv_dict_writer.writerow({"book_id": book["book_id"], "user_id": user["user_id"], "returned": False})
        return "Loaned book successfully"


@router.post('/{title}/return')
def return_book(title: str, login_user: UserModel):
    with open('db/users.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        users = list(csv_dict_reader)
        for user in users:
            if user["username"].lower() == login_user.username.lower():
                if user["password"] == login_user.password:
                    break
                else:
                    raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=401, detail="Non existing user")

    with open('db/books.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for book in csv_dict_reader:
            if book['title'] == title:
                break
        else:
            raise HTTPException(status_code=404, detail="Book not found")

    with open('db/loans.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for line, loan in enumerate(csv_dict_reader):
            if loan['book_id'] == book['book_id'] and loan["returned"] == "False":
                if loan["user_id"] == user["user_id"]:
                    break
                else:
                    raise HTTPException(status_code=422, detail="Book is loaned by someone else")
        else:
            raise HTTPException(status_code=422, detail="Book is not currently loaned")

    with open('db/loans.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        loans =  [loan for loan in csv_dict_reader]
        loans[line]["returned"] = "True"

    with open('db/loans.csv', "w", newline="", encoding="utf-8") as csvfile:
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["book_id", "user_id", "returned"])
        csv_dict_writer.writeheader()
        csv_dict_writer.writerows(loans)
        return "Returned book successfully"



@router.get('/stats/top-books')
def get_top_books():
    with open('db/books.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        books_dict = {book["book_id"]: book["title"] for book in csv_dict_reader}

    loans_counter_dict = {}
    with open('db/loans.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for loan in csv_dict_reader:
            if loan["book_id"] not in loans_counter_dict:
                loans_counter_dict[loan["book_id"]] = 0
            loans_counter_dict[loan["book_id"]] += 1

    if not loans_counter_dict:
        return "No books loaned yet"

    books_stats = list(loans_counter_dict.items())
    books_stats.sort(key=lambda book_stat: book_stat[1], reverse=True)
    books_stats = [{"title": books_dict[book_stat[0]], "loaned_counter": book_stat[1]} for book_stat in books_stats[:5]]

    return books_stats
