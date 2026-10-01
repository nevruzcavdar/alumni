"""
Alumni Management System - Core API Entry Point
CRUD on /api/users + Swagger UI at /api/swagger
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.database import Base, engine
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create DB tables automatically on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Alumni Management System API",
    description="Backend API service for managing alumni network, profiles, mentorship, and career opportunities.",
    version="0.2.0",
    docs_url="/api/swagger",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(users.router)


@app.get("/docs", include_in_schema=False)
def redirect_to_custom_swagger():
    """Redirect standard /docs to /api/swagger."""
    return RedirectResponse(url="/api/swagger")


@app.get("/")
def root():
    """System information and root endpoint."""
    return {
        "message": "Welcome to the Alumni Management System API",
        "project": "Alumni Management System",
        "version": "0.2.0",
        "status": "operational",
        "docs_url": "/api/swagger",
        "users_api": "/api/users",
        "milestone": "CRUD on /api/users + Swagger UI at /api/swagger",
    }


@app.get("/hello")
def hello():
    """Returns a default greeting message."""
    return {"message": "Hello, World!"}


@app.get("/hello/{name}")
def hello_name(name: str):
    """Returns a personalized greeting message."""
    return {"message": f"Hello, {name}!"}


@app.get("/sum/{a}/{b}")
def calculate_sum(a: int, b: int):
    """Calculates the sum of two integers."""
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.get("/about")
def about():
    """Returns information about the project."""
    return {
        "project": "Alumni Management System",
        "description": "A modern web platform connecting graduates, students, and institutions for lifelong engagement and mentorship.",
        "author": "Nevruz Çavdar",
        "version": "0.2.0",
        "routes": [
            "/",
            "/api/swagger",
            "/api/users",
            "/hello",
            "/hello/{name}",
            "/sum/{a}/{b}",
            "/about",
            "/health",
        ],
    }


@app.get("/health")
def health():
    """Liveness probe."""
    return {"status": "ok"}
