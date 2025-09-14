from pydantic import BaseModel


class MusicianCreateModel(BaseModel):
    name: str
    style: str
    label: str


class SongCreateModel(BaseModel):
    title: str
    released: str
    duration: str
    musician_name: str
