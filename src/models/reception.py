from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.db.database import Base


class ReceptionPointModel(Base):
    __tablename__ = 'reception_points'
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    coord_x: Mapped[str] = mapped_column(nullable=False)
    coord_y: Mapped[str] = mapped_column(nullable=False)
    time: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    vk_ref: Mapped[str] = mapped_column(nullable=False)
    tg_ref: Mapped[str] = mapped_column(nullable=False)
    img: Mapped[str] = mapped_column(nullable=True)
    
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    
    def __repr__(self) -> str:
        return f'{self.id} {self.title} {self.coord_x} {self.coord_y} {self.time} {self.address} {self.description} {self.category}'
