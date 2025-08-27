from sqlalchemy.orm import Session
from . import models, schemas

def get_quotes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Quote).offset(skip).limit(limit).all()

def get_quote(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()

def search_quotes(db: Session, author: str = None, keyword: str = None):
    query = db.query(models.Quote)
    if author:
        query = query.filter(models.Quote.author.contains(author))
    if keyword:
        query = query.filter(models.Quote.text.contains(keyword))
    return query.all()

def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def update_quote(db: Session, quote_id: int, data: schemas.QuoteUpdate):
    db_quote = get_quote(db, quote_id)
    if not db_quote:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(db_quote, key, value)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def delete_quote(db: Session, quote_id: int):
    db_quote = get_quote(db, quote_id)
    if db_quote:
        db.delete(db_quote)
        db.commit()
        return True
    return False
