from fastapi import FastAPI, HTTPException, Depends
from models import UserCreate, UserLogin, Token
from utils import hash_password, verify_password
from auth import create_access_token
from database import users_db
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from routes import anomaly_detection

app = FastAPI()
app.include_router(anomaly_detection.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/register")
def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists.")
    hashed = hash_password(user.password)
    users_db[user.username] = {
        "username": user.username,
        "password": hashed,
        "role": user.role
    }
    return {"message": "User registered successfully."}

@app.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username, "role": db_user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}
