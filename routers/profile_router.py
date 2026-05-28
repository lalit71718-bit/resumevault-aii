from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import supabase
from auth import get_current_user

profile_router = APIRouter(prefix="/profile", tags=["Profile"])


class ProfileUpdate(BaseModel):
    headline: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    availability_status: Optional[str] = None
    company_name: Optional[str] = None
    industry: Optional[str] = None


@profile_router.get("/me")
def get_my_profile(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    role = current_user["role"]

    user = supabase.table("users").select("id, email, full_name, role, created_at").eq("id", user_id).execute()
    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")

    if role == "seeker":
        profile = supabase.table("seeker_profiles").select("*").eq("user_id", user_id).execute()
    else:
        profile = supabase.table("recruiter_profiles").select("*").eq("user_id", user_id).execute()

    profile_data = profile.data[0] if profile.data else {}
    return {**user.data[0], **profile_data}


@profile_router.put("/update")
def update_profile(update_data: ProfileUpdate, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    role = current_user["role"]

    if role == "seeker":
        fields = {}
        if update_data.headline: fields["headline"] = update_data.headline
        if update_data.bio: fields["bio"] = update_data.bio
        if update_data.location: fields["location"] = update_data.location
        if update_data.availability_status: fields["availability_status"] = update_data.availability_status

        if fields:
            supabase.table("seeker_profiles").update(fields).eq("user_id", user_id).execute()

    elif role == "recruiter":
        fields = {}
        if update_data.company_name: fields["company_name"] = update_data.company_name
        if update_data.industry: fields["industry"] = update_data.industry
        if update_data.location: fields["location"] = update_data.location

        if fields:
            supabase.table("recruiter_profiles").update(fields).eq("user_id", user_id).execute()

    return {"message": "Profile updated successfully"}