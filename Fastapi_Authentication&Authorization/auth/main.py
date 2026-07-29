from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, utils
from auth_database import get_db
from jose import jwt
from datetime import datetime, timedelta


SECRET_KEY = "t57t1AR5VSQyDeq5f2n6j8JeIrAKvQ-cBO4Xu_eJ2vo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#helper function that takes user data
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = date.utcnow()