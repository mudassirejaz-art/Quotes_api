from pydantic import BaseModel

class QuoteBase(BaseModel):
    author: str
    text: str
    category: str | None = None

class QuoteCreate(QuoteBase):
    pass

class QuoteUpdate(BaseModel):
    author: str | None = None
    text: str | None = None
    category: str | None = None

class QuoteOut(QuoteBase):
    id: int

    class Config:
        orm_mode = True
