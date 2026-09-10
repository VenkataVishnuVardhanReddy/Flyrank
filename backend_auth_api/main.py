from fastapi import FastAPI
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

app = FastAPI()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")

# Client initialization
if url and key:
    supabase: Client = create_client(url, key)
else:
    supabase = None

@app.on_event("startup")
def startup_event():
    print("Server running and connected to Supabase")
