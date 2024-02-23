# crud.py
from sqlalchemy.orm import Session
from models import Currency

def get_currency_by_code(db: Session, code: str):
    return db.query(Currency).filter(Currency.code == code).first()

def update_currency_rate(db: Session, code: str, new_rate: float):
    currency = get_currency_by_code(db, code)
    if currency:
        currency.rate = new_rate
        db.commit()
        db.refresh(currency)
        return currency
    return None
