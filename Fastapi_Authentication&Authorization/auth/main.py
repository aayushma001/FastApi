from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, utils
from auth_database import get_db


SECRET_KEY = "t57t1AR5VSQyDeq5f2n6j8JeIrAKvQ-cBO4Xu_eJ2vo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30