from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from src.app.libs.helper import is_isbn_or_key
from src.app.models.base import Base, db
from src.app import login_manager
from src.app.models.gift import Gift
from src.app.models.wish import Wish
from src.app.spider.FishBook import FishBook
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(UserMixin, Base):
    __tablename__ = 'user'
    # __bind_key__ = 'fisher'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    # gifts = relationship('Gift')

    _password = Column('password', String(100), nullable=False)

    # def __init__(self, nickname, email, password, phone_number=None):
    #     self.nickname = nickname
    #     self._password = generate_password_hash(password)
    #     self.email = email
    #     self.phone_number = phone_number
    #     super(User, self).__init__()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def get_id(self):
        return self.id

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        fishbook = FishBook()
        fishbook.search_by_isbn(isbn)
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not fishbook.first:
            return False
        if not gifting and not wishing:
            return True
        else:
            return False

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
