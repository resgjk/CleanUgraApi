from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base


class CategoryModel(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    rules: Mapped[str] = mapped_column(nullable=False)
    not_take: Mapped[str] = mapped_column(nullable=True)
    img: Mapped[str] = mapped_column(nullable=False)
    
    
    def __repr__(self) -> str:
        return f'{self.id} {self.title} {self.rules} {self.not_take} {self.img}'
