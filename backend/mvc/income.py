import re
import string
import random
from datetime import date
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc

# Create random Income Number
def get_income_number():
  the_number=random.randint(101, 999999)
  letters = string.ascii_uppercase
  the_letter = ''.join(random.choice(letters) for i in range(1))
  today = date.today()
  the_day = today.strftime("%d%m%y-")
  income_number = str(the_day) + str(the_letter) + str(the_number)
  print("income_number:", income_number)
  return income_number

# Show All Income ##.order_by(desc('date'))
def income_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    income = db.query(models.Income).offset(offset).limit(limit).all()
    return income

# Show a Specific income by date year: str, month: str,
def income_show_by_date(year:str, month:str, db: Session):
    income = db.query(models.Income).filter(models.Income.date >= f'{year}-{month}-01', models.Income.date <= f'{year}-{month}-31').all()
    return income

# Show a Specific Income by id
def income_show(id: int, db: Session):
    income = db.query(models.Income).filter(models.Income.id == id).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The income with ID {id} is not found')
    return income

def income_create(request: schemas.Income, db: Session):
    new_income = models.Income(income_number=get_income_number(),start_date=request.start_date, due_date=request.due_date, title = request.title, description = request.description, tags = request.tags, active = request.active, status=request.status, priority = request.priority,  owner_id = request.owner_id)
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income

def income_update(id: int, request: schemas.Income, db: Session):
    db.query(models.Income).filter(models.Income.id == id).update({ 'start_date': request.start_date,"due_date": request.due_date,'title': request.title, 'description': request.description, 'tags': request.tags, 'active': request.active, 'status': request.status,  'priority': request.priority, 'owner_id': request.owner_id })
    db.commit()
    return "Income updated!"
    
def income_destroy(id: int, db: Session):
    income = db.query(models.Income).filter(models.Income.id == id)
    if not income.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Income with id {id} is not found") 
    income.delete(synchronize_session=False)
    db.commit()
    return "Income deleted!"
