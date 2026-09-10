from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

app = FastAPI()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")
supabase: Client = create_client(url, key) if url and key else None

@app.on_event("startup")
def startup_event():
    print("Server running and connected to Supabase")

class AuthDetails(BaseModel):
    email: str
    password: str

@app.post("/auth/signup", status_code=status.HTTP_201_CREATED)
def signup(auth_details: AuthDetails):
    if not auth_details.email or not auth_details.password:
        raise HTTPException(status_code=400, detail="Email and password required")
    try:
        res = supabase.auth.sign_up({"email": auth_details.email, "password": auth_details.password})
        return res.user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/auth/login", status_code=status.HTTP_200_OK)
def login(auth_details: AuthDetails):
    if not auth_details.email or not auth_details.password:
        raise HTTPException(status_code=400, detail="Email and password required")
    try:
        res = supabase.auth.sign_in_with_password({"email": auth_details.email, "password": auth_details.password})
        return res.session
    except Exception as e:
        raise HTTPException(status_code=401, detail='{"error": "Invalid login credentials"}')
