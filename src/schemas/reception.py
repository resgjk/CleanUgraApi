from pydantic import BaseModel


class PointCreate(BaseModel):
    title: str
    coord_x: str
    coord_y: str
    time: str
    addres: str
    description: str
    phone_number: str
    category: int
