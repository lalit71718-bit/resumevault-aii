from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import supabase
from auth import get_current_user

vault_router = APIRouter(prefix="/vault", tags=["Resume Vault"])

# ── Skills ──────────────────────────────────────────
class SkillCreate(BaseModel):
    name: str
    category: Optional[str] = None
    proficiency_level: Optional[str] = None
    years_of_experience: Optional[int] = None

@vault_router.post("/skills", status_code=201)
def add_skill(skill: SkillCreate, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    data = {"user_id": user_id, **skill.dict()}
    response = supabase.table("skills").insert(data).execute()
    return response.data[0]

@vault_router.get("/skills")
def get_skills(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    response = supabase.table("skills").select("*").eq("user_id", user_id).execute()
    return response.data

@vault_router.delete("/skills/{skill_id}")
def delete_skill(skill_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    supabase.table("skills").delete().eq("id", skill_id).eq("user_id", user_id).execute()
    return {"message": "Skill deleted"}

# ── Projects ─────────────────────────────────────────
class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    tech_stack: Optional[List[str]] = None
    github_link: Optional[str] = None
    live_link: Optional[str] = None
    is_featured: Optional[bool] = False

@vault_router.post("/projects", status_code=201)
def add_project(project: ProjectCreate, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    data = {"user_id": user_id, **project.dict()}
    response = supabase.table("projects").insert(data).execute()
    return response.data[0]

@vault_router.get("/projects")
def get_projects(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    response = supabase.table("projects").select("*").eq("user_id", user_id).execute()
    return response.data

@vault_router.delete("/projects/{project_id}")
def delete_project(project_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    supabase.table("projects").delete().eq("id", project_id).eq("user_id", user_id).execute()
    return {"message": "Project deleted"}

# ── Experiences ───────────────────────────────────────
class ExperienceCreate(BaseModel):
    company_name: str
    role_title: str
    employment_type: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    is_current: Optional[bool] = False
    description: Optional[str] = None
    achievements: Optional[List[str]] = None

@vault_router.post("/experiences", status_code=201)
def add_experience(exp: ExperienceCreate, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    data = {"user_id": user_id, **exp.dict()}
    response = supabase.table("experiences").insert(data).execute()
    return response.data[0]

@vault_router.get("/experiences")
def get_experiences(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    response = supabase.table("experiences").select("*").eq("user_id", user_id).execute()
    return response.data

@vault_router.delete("/experiences/{exp_id}")
def delete_experience(exp_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    supabase.table("experiences").delete().eq("id", exp_id).eq("user_id", user_id).execute()
    return {"message": "Experience deleted"}

# ── Certifications ────────────────────────────────────
class CertificationCreate(BaseModel):
    name: str
    issuing_organization: Optional[str] = None
    issue_date: Optional[str] = None
    expiry_date: Optional[str] = None
    credential_url: Optional[str] = None

@vault_router.post("/certifications", status_code=201)
def add_certification(cert: CertificationCreate, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    data = {"user_id": user_id, **cert.dict()}
    response = supabase.table("certifications").insert(data).execute()
    return response.data[0]

@vault_router.get("/certifications")
def get_certifications(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    response = supabase.table("certifications").select("*").eq("user_id", user_id).execute()
    return response.data

@vault_router.delete("/certifications/{cert_id}")
def delete_certification(cert_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    supabase.table("certifications").delete().eq("id", cert_id).eq("user_id", user_id).execute()
    return {"message": "Certification deleted"}
