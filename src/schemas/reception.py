from pydantic import BaseModel


class ShortPoint(BaseModel):
    title: str
    coord_x: str
    coord_y: str
    address: str
    category: int
    img: str | None = None


class Point(ShortPoint):
    id: int
    time: str
    address: str
    description: str
    phone_number: str
    vk_ref: str
    tg_ref: str
    category: int
