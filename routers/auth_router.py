from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from database import supabase
from auth import hash_password, verify_password, create_access_token

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@auth_router.post("/register", status_code=201)
def register_user(request: UserRegistration):
    if request.role not in ["seeker", "recruiter"]:
        raise HTTPException(status_code=400, detail="Role must be seeker or recruiter")
    
    existing = supabase.table("users").select("id").eq("email", request.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(request.password)
    user_data = {
        "email": request.email,
        "password_hash": hashed_password,
        "full_name": request.full_name,
        "role": request.role
    }
    response = supabase.table("users").insert(user_data).execute()
    user_id = response.data[0]["id"]
    
    if request.role == "seeker":
        supabase.table("seeker_profiles").insert({"user_id": user_id}).execute()
    elif request.role == "recruiter":
        supabase.table("recruiter_profiles").insert({"user_id": user_id}).execute()
    
    return {
        "access_token": create_access_token(user_id, request.role),
        "user_id": user_id
    }

@auth_router.post("/login", status_code=200)
def login_user(request: UserLogin):
    response = supabase.table("users").select("*").eq("email", request.email).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="User not found")
    
    user = response.data[0]
    if not verify_password(request.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return {
        "access_token": create_access_token(user["id"], user["role"])
    }