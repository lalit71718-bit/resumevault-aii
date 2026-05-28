from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth_router, profile_router, vault_router

app = FastAPI(title="ResumeVault AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(vault_router)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ResumeVault AI is running"}
