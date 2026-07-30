from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt 
from passlib.context import CryptoContext

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_db = {
    "tim": {
        "username": "tim",
        "full_name": "TimRusscia",
        "email": "tim@gmail.com",
        "hashed_password": "",
        "disabled": False
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None or None

class User(BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    disabled: bool or None = None
class UserInDB(User):
    hashed_password: str

pwd_context = CryptoContext(schemas=["bycrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")
app = FastAPI()

def verify_password(plain_password, hashed_passwords):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)

def authenticate_user(db, username: str, password:str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         Ddetail="could not validate credentials", headers = {"WWW.Aauthenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credential_exception
    return user















# fake_db = {
#     "pwd_policy_setup": {
#         "policy_id": ,
#         "policy_name":,
#         "description":,
#         "length_min":,
#         "cap_required":,
#         "num_required":,
#         "spchar_required":,
#         "expiry_days":
#     }
# }

# app = FastAPI()
# class Data(BaseModel):
#     name:str
#     policy_id = Column(String(5), primary_key=True, index=True)

# @app.post("/create/")
# async def create(data: Data):
#     return {"data": data}

# @app.get("/test/{item_id}/")
# async def test(item_id: str, query: int = 1):
#     return {"Hello": item_id}