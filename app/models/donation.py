from sqlalchemy import Column, ForeignKey, Integer, Text
from .base import CustomBase


class Donation(CustomBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return f'<Donation(id={self.id}, user_id={self.user_id}, comment=\'{self.comment[:50]}...\')>'
