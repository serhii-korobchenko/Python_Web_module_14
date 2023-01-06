from sqlalchemy.orm import sessionmaker
from models import db_connect, create_table, Author, Quote, Tag
from sqlalchemy import create_engine
def data_load():
    with Session() as session:
        exist_authors = session.query(Author.name).all()

    for author_item in exist_authors:
        print(author_item[0])

if __name__ == "__main__":
    engine = create_engine("sqlite:///scrapy_quotes.db")
    Session = sessionmaker(bind=engine)
    data_load()