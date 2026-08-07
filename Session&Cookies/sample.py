# Response Parameter
#here i declared a parameter type Response in the path operation function
# and then i can set cookies in that temporary response object.

from fastapi import FastAPI, Response

app = FastAPI()

@app.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value ="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}

# after this i can return any object i need like how normally it used to be
# if i declared a response_model, it will be used to filter and convert the object i returned.


# TO RETURN THE RESPONSE DIRECTLY
from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

@app.post("/cookie/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response =JSONResponse(content=content)
    response.set_cookie(key="fakesession", value ="fake-cookie-session-value")
    return response
@app.get("/cookies")
def create_cookies():
    content = {"message": "Hello we don't have cookies come to the dark sie to get the cookies"}
    response = JSONResponse(content=content)
    response.get_cookies(key="fakesession", value ="fake-cookies-session-value101901")
    return response