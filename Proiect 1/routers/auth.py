import csv

from fastapi import APIRouter, HTTPException
from models import UserModel

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post('/register')
def register(new_user: UserModel):
    with open('db/users.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        users = list(csv_dict_reader)
        for user in users:
            if user["username"].lower() == new_user.username.lower():
                raise HTTPException(status_code=422, detail="Username already registered")

    with open('db/users.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())

        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["user_id", "username", "password"])
        csv_dict_writer.writerow({"user_id": lines, "username": new_user.username, "password": new_user.password})
        return "Added user successfully"


@router.post('/login')
def login(login_user: UserModel):
    with open('db/users.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        users = list(csv_dict_reader)
        for user in users:
            if user["username"].lower() == login_user.username.lower():
                if user["password"] == login_user.password:
                    return {"status": "Success"}
                else:
                    raise HTTPException(status_code=401, detail="Incorrect password")

        raise HTTPException(status_code=401, detail="Non existing user")
