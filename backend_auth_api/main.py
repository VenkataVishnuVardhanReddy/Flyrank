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

from fastapi import Header

@app.get("/public/info", status_code=status.HTTP_200_OK)
def public_info():
    return {"message": "Welcome stranger! This info is public."}

@app.get("/protected/profile", status_code=status.HTTP_200_OK)
def protected_profile(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail='{"error": "Access token required"}')
    
    token = authorization.split(" ")[1]
    try:
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(status_code=401, detail='{"error": "Invalid or expired token"}')
        return {"message": "Welcome to your profile!", "user": user}
    except Exception as e:
        raise HTTPException(status_code=401, detail='{"error": "Invalid or expired token"}')
