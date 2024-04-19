from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, StrictInt, PositiveInt


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
    )
    description: Optional[str] = Field(
        None, min_length=1
    )
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: StrictInt
    fully_invested: bool = False
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
