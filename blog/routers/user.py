from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from .. import schemas, database
from ..repository import user
router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db)):
    return user.get(id, db)