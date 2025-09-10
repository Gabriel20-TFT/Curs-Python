import csv

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/musicians", tags=["musicians"])


@router.get('')
def get_musicians():
    with open('db/musicians.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        musicians = list(csv_dict_reader)
        for musician in musicians:
            musician.pop("id")
        return musicians


@router.get('/{musician_name}')
def get_musician(musician_name: str):
    with open('db/musicians.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for musician in csv_dict_reader:
            if musician_name.lower() in musician['name'].lower():
                musician.pop("id")
                return musician
        raise HTTPException(status_code=404, detail="Musician not found")


@router.post('/create')
def create_musician(name: str, style: str, label: str):
    field_names = ["id", "name", "style", "label"]

    with open('db/musicians.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())

        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_dict_writer.writerow({"id": lines, "name": name, "style": style, "label": label})
        return "Added musician successfully"
