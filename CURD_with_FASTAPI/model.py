from sqlalchemy import Boolean, Column, Integer, String

from db_handler import Base

    
class Movies(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    movie_id = Column(String, unique=True, index=True, nullable=False)
    # Here the Index construct is created externally to the table which it corresponds, using Column objects directly. 
    # Index also supports “inline” definition inside the Table, using string names to identify columns. 
    # There are many way to use index. for more information you can refer sqlAlchemy documentation page
    
    movie_name = Column(String(255), index=True, nullable=False)
    director = Column(String(100), index=True, nullable=False)
    geners = Column(String, index=True, nullable=False)
    membership_required = Column(Boolean, nullable=False, default=True)
    cast = Column(String(255), index=True, nullable=False)
    streaming_platform = Column(String, index=True)

    
    
