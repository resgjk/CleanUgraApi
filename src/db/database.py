from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase



url_base = 'sqlite+aiosqlite:///database.db'

async_engine = create_async_engine(url_base, echo=True)

async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession,
                                         expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def create_all_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session():
    async with async_session_maker as session:
        yield session
    
