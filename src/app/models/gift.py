from flask import current_app
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, desc, func
from sqlalchemy.orm import relationship
from src.app.models.base import Base, db
from src.app.models.wish import Wish
from src.app.spider.FishBook import FishBook


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        if self.uid == uid:
            return True

    @classmethod
    def get_wish_count(cls, isbn_list):
        wish_count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).all()
        wish_count_dict = [{'count': w[0], 'isbn': w[1]} for w in wish_count_list]
        return wish_count_dict

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(launched=False, uid=uid).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @property
    def book(self):
        fishbook = FishBook()
        fishbook.search_by_isbn(self.isbn)
        return fishbook.first

    @classmethod
    def rencent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
