"""
Alumni Management System - Core API Entry Point
Week 1 - Basic Routes Implementation
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Alumni Management System API",
    description="Backend API service for managing alumni network, profiles, mentorship, and career opportunities.",
    version="0.1.0",
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """System information and root endpoint."""
    return {
        "message": "Welcome to the Alumni Management System API",
        "project": "Alumni Management System",
        "version": "0.1.0",
        "status": "operational",
        "docs_url": "/docs",
        "milestone": "Week 1 - Basic Routes",
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
        "version": "0.1.0",
        "routes": [
            "/",
            "/hello",
            "/hello/{name}",
            "/sum/{a}/{b}",
            "/about",
            "/health",
            "/docs",
        ],
    }


@app.get("/health")
def health():
    """Liveness probe."""
    return {"status": "ok"}
