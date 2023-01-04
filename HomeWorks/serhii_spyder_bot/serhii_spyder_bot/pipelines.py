# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from .models import db_connect, create_table, Author, Quote, Tag


class SerhiiSpyderBotPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)



    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()

        author = Author()
        author.name = item["author"][0]
        author.ref = item["about"][0]
        quote = Quote()
        quote.quote_content = item["quote"][0]



        # check whether the author exists
        exist_author = session.query(Author).filter_by(name = author.name).first()
        try:
            if exist_author is None:  # the current author exists

                session.add(author)

            print(f"--------->  {session.query(Author).filter_by(name=author.name).first().id}")
            quote.author_id = session.query(Author).filter_by(name=author.name).first().id
            session.add(quote)
            session.commit()


            for tag_item in item["keywords"]:
                exist_tag = session.query(Tag).filter_by(name=tag_item).first()
                if exist_tag is None:
                    tag = Tag()
                    tag.name = tag_item
                    tag.quote_id = session.query(Quote).filter_by(quote_content=quote.quote_content).first().id
                    session.add(tag)
                    session.commit()


        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

###########################################################################
    # def process_item(self, item, spider):
    #     """Save quotes in the database
    #     This method is called for every item pipeline component
    #     """
    #     session = self.Session()
    #     quote = Quote()
    #     author = Author()
    #     tag = Tag()
    #     author.name = item["author"]
    #     author.birthday = item["author_birthday"]
    #     author.bornlocation = item["author_bornlocation"]
    #     author.bio = item["author_bio"]
    #     quote.quote_content = item["quote"]
    #
    #     # check whether the author exists
    #     exist_author = session.query(Author).filter_by(name = author.name).first()
    #     if exist_author is not None:  # the current author exists
    #         quote.author = exist_author
    #     else:
    #         quote.author = author
    #
    #     # check whether the current quote has tags or not
    #     if "keywords" in item:
    #         for tag_name in item["keywords"]:
    #             tag = Tag(name=tag_name)
    #             # check whether the current tag already exists in the database
    #             exist_tag = session.query(Tag).filter_by(name = tag.name).first()
    #             if exist_tag is not None:  # the current tag exists
    #                 tag = exist_tag
    #             quote.tags.append(tag)
    #
    #     try:
    #
    #         session.add(quote)
    #         session.commit()
    #
    #     except:
    #         session.rollback()
    #         raise
    #
    #     finally:
    #         session.close()
    #
    #     return item

