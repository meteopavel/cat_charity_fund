from sqlalchemy import Column, String, Text

from app.models.base import Investment


class CharityProject(Investment):
    name = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (f'{super().__repr__()},'
                f'Имя благотворительного проекта: {self.name}, '
                f'Описание: {self.description}')
