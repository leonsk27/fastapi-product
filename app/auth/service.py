from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlmodel import select
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.db import SessionDep
from app.auth import models, schemas, utils


class AuthService:
    # CREATE USER
    # ----------------------
    def create_user(self, user: schemas.UserCreate, db: SessionDep):
        query = select(models.User).where(models.User.username == user.username)
        db_user = db.exec(query).first()        
        if db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

        hashed_password = utils.get_password_hash(user.password)
        user_data_dict = user.model_dump(exclude_unset=True)
        del user_data_dict['password']
        user_data_dict['password_hash'] = hashed_password
        new_user = models.User(**user_data_dict)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    def login_for_access_token(
            self,
            db:SessionDep, 
            form_data: OAuth2PasswordRequestForm = Depends()
        ):
        user = utils.authenticate_user(db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=utils.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=utils.REFRESH_TOKEN_EXPIRE_DAYS)
        
        access_token = utils.create_access_token(
            data={
                'sub': user.username,
                'id': user.id,
                'email': user.email,
            }, 
            expires_delta=access_token_expires
        )
        
        refresh_token = utils.create_access_token(
            data={
                'sub': user.username,
                'id': user.id,
                'email': user.email,
            },
            expires_delta=refresh_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}
    
    def refresh_access_token(self, db: SessionDep, refresh_token: str):
        try:
            payload = utils.decode_token(refresh_token)
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        
        user = utils.get_user(db, username)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        
        access_token_expires = timedelta(minutes=utils.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = utils.create_access_token(
            data={
                'sub': user.username,
                'id': user.id,
                'email': user.email,
            },
            expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
        
    def logout(self, db: SessionDep, token: str):
        try:
            payload = utils.decode_token(token)
            user_id: int = payload.get("id")
            if user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
        revoked_token = models.UserRevokedToken(token=token, user_id=user_id)
        db.add(revoked_token)
        db.commit()