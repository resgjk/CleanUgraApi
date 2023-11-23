from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base

class NewsModel(Base):
    __tablename__ = 'news'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, 
                                    nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    decsription: Mapped[str] = mapped_column(nullable=False)
    img: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(nullable=False)
    
    def __repr__(self) -> str:
        return f'{self.id} {self.title} {self.decsription} {self.img} {self.date}'
