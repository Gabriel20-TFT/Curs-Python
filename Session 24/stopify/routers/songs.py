import csv

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/songs", tags=["songs"])


def get_musician_by_id(musician_id: str):
    with open('db/musicians.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for musician in csv_dict_reader:
            if musician['id'] == musician_id:
                return musician
        raise HTTPException(status_code=404, detail="Musician not found")


@router.get('')
def get_songs():
    with open('db/songs.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        songs = list(csv_dict_reader)
        for song in songs:
            song.pop("id")
            musician_id = song.pop("musician id")
            musician = get_musician_by_id(musician_id)
            song["muscian_name"] = musician["name"]
        return songs


@router.get('/{song_title}')
def get_song(song_title: str):
    with open('db/songs.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for song in csv_dict_reader:
            if song_title.lower() in song['title'].lower():
                song.pop("id")
                musician_id = song.pop("musician id")
                musician = get_musician_by_id(musician_id)
                song["muscian_name"] = musician["name"]
                return song
        raise HTTPException(status_code=404, detail="Song not found")


@router.post('/create')
def create_song(title: str, released: str, duration: str, musician_name: str):
    field_names = ["id", "title", "released", "duration", "musician_id"]

    song_musician = None

    with open('db/musicians.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for musician in csv_dict_reader:
            if musician['name'] == musician_name:
                song_musician = musician
    if song_musician is None:
        raise HTTPException(status_code=404, detail="Musician not found")

    with open('db/songs.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())

        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_dict_writer.writerow({"id": lines, "title": title, "released": released, "duration": duration,
                                  "musician_id": song_musician["id"]})
        return "Added song successfully"
