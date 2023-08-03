from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.core.db import Base


class CustomBase(Base):

    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    def __repr__(self):
        return f'<{self.__class__.__name__}(id={self.id}, full_amount={self.full_amount}, ' \
               f'invested_amount={self.invested_amount}, fully_invested={self.fully_invested}, ' \
               f'create_date={self.create_date}, close_date={self.close_date})>'
