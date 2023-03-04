from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import user, income

router = APIRouter(
    prefix="/api/income",
    tags=['Income']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowIncome]) 
async def all_incomes(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.income_get_all(db)

@router.get('/{year}/{month}/', response_model = List[schemas.ShowIncome], status_code=200)
async def show_income_by_date(year: str, month: str , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.income_show_by_date(year, month, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowIncome)
async def show_income(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.income_show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_income(request: schemas.Income, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.income_create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_income(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.income_destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_income(id:int , request: schemas.Income, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.income_update(id, request, db) 

