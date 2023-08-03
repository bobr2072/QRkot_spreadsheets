from sqlalchemy import Column, String, Text

from .base import CustomBase


class CharityProject(CustomBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f'<CharityProject(id={self.id}, name=\'{self.name}\', description=\'{self.description[:50]}...\')>'
