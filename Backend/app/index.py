import os
import global_value as g
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from Mail.MailSender import MailSender

# routers import
from Routers.Login import LoginRouter

load_dotenv()
g.DB_HOST = os.environ['DB_HOST']
g.DB_DATABASE = os.environ['DB_DATABASE']
g.DB_USER = os.environ['DB_USER']
g.DB_PASS = os.environ['DB_PASS']
g.ENCRYPT_STR = os.environ['ENCRYPT_STR']
g.SMTP_HOST = os.environ['SMTP_HOST']
g.SMTP_PORT = os.environ['SMTP_PORT']
g.FROM_ADDRESS = os.environ['FROM_ADDRESS']
g.FROM_ADDRESS_PASSWORD = os.environ['FROM_ADDRESS_PASSWORD']


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(LoginRouter.router)

@app.get("/")
def Hello():
    return {"Hello":"World!"}

@app.get("/mail_test")
def mail_test():
    MailSender().send('kzy83ishi15@gmail.com', 'test', 'testaaa')
    return { "mail": "送ったよ" }