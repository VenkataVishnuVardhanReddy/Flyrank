from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

app = FastAPI(
    title="Auth API",
    description="A secure API demonstrating authentication using Supabase.",
    version="1.0"
)

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

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        user = supabase.auth.get_user(token)
        if not user:
             raise HTTPException(status_code=401, detail='{"error": "Invalid or expired token"}')
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail='{"error": "Invalid or expired token"}')

@app.post("/auth/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Supabase JWTs are stateless but we can try to call sign_out
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    return

@app.get("/public/info", status_code=status.HTTP_200_OK)
def public_info():
    return {"message": "Welcome stranger! This info is public."}

@app.get("/protected/profile", status_code=status.HTTP_200_OK)
def protected_profile(user = Depends(get_current_user)):
    return {"message": "Welcome to your profile!", "user": user}

@app.get("/protected/dashboard", status_code=status.HTTP_200_OK)
def protected_dashboard(user = Depends(get_current_user)):
    return {"message": "Dashboard access granted.", "user": user}
