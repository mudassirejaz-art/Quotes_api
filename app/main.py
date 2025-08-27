from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Quotes API", version="1.0")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/quotes/", response_model=list[schemas.QuoteOut])
def list_quotes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_quotes(db, skip, limit)

@app.get("/quotes/search", response_model=list[schemas.QuoteOut])
def search_quotes(author: str = None, keyword: str = None, db: Session = Depends(get_db)):
    return crud.search_quotes(db, author, keyword)

@app.post("/quotes/", response_model=schemas.QuoteOut)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db), user: dict = Depends(auth.get_current_user)):
    return crud.create_quote(db, quote)

@app.put("/quotes/{quote_id}", response_model=schemas.QuoteOut)
def update_quote(quote_id: int, data: schemas.QuoteUpdate, db: Session = Depends(get_db), user: dict = Depends(auth.get_current_user)):
    updated = crud.update_quote(db, quote_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Quote not found")
    return updated

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db), user: dict = Depends(auth.get_current_user)):
    success = crud.delete_quote(db, quote_id)
    if not success:
        raise HTTPException(status_code=404, detail="Quote not found")
    return {"message": "Deleted"}
