from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import schemas, utils
from app.core.db import SessionDep
from app.auth.service import AuthService

router = APIRouter()
service = AuthService()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: SessionDep):
    '''
    create new user

    This function will create a new user with the encrypted password
    '''
    return service.create_user(user,db)


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    db: SessionDep, 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return service.login_for_access_token(db,form_data)


@router.get("/users/me/", response_model=schemas.UserResponse)
async def read_users_me(current_user: schemas.User = Depends(utils.get_current_user)):
    return current_user

@router.post("/token/refresh", response_model=schemas.Token)
async def refresh_access_token(
    db: SessionDep, 
    refresh_token: str
):
    return service.refresh_access_token(db, refresh_token)