from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from blog import schemas, database
from blog.repository import blog
from blog.oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def index(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    blog.update(id, request, db)
    return 'updated'


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    db.delete(id, db)
    return 'done'