from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import blog, user

router = APIRouter(
    prefix="/api/blog",
    tags=['Blog']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.Blog])
async def all_blog(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', response_model=List[schemas.Blog], status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

#  
@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_blog(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id:int , request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db) 

# @router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
@router.get('/{id}', status_code=200, response_model=schemas.Blog)
async def show_Blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)