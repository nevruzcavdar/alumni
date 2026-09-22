"""
Alumni Management System - Core API Entry Point
Week 1 Initial Baseline
"""

import os
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
    """System information & health check endpoint."""
    return {
        "project": "Alumni Management System",
        "version": "0.1.0",
        "status": "operational",
        "docs_url": "/docs",
        "milestone": "Week 1 - Stack Setup & Repository Initialization",
    }


@app.get("/health")
def health():
    """Liveness probe."""
    return {"status": "ok"}
