from pydantic import BaseModel

class ShortPoint(BaseModel):
    title: str
    coord_x: str
    coord_y: str
    category: int
    img: str


class Point(BaseModel):
    id: int
    title: str
    coord_x: str
    coord_y: str
    time: str
    address: str
    description: str
    phone_number: str
    vk_ref: str
    tg_ref: str
    img: str
    category: int
