# 🧠 The Complete Backend Bible: OrbitHire — AI-Powered Freelance Marketplace

> **Who is this for?** Absolute beginners. If you have never built a backend before, this document will take you from zero to understanding every single line of code in this project. You will never need to open another tutorial.

---

## 📖 Table of Contents

1. [What Even Is a Backend?](#1-what-even-is-a-backend)
2. [The Tech Stack (Tools We Used)](#2-the-tech-stack)
3. [Project Folder Structure (The Map)](#3-project-folder-structure)
4. [Phase 0: The Foundation Files](#4-phase-0-the-foundation-files)
5. [Phase 1: Database Models (The Blueprint)](#5-phase-1-database-models)
6. [Phase 1: Pydantic Schemas (The Bodyguard)](#6-phase-1-pydantic-schemas)
7. [Phase 1: Authentication (The Bouncer)](#7-phase-1-authentication)
8. [Phase 1: API Endpoints (The Waiters)](#8-phase-1-api-endpoints)
9. [Phase 2: Escrow Engine (The Bank Vault)](#9-phase-2-escrow-engine)
10. [Phase 2: Reviews & Ratings (The Reputation)](#10-phase-2-reviews--ratings)
11. [Phase 2: Real-Time Messaging (The Conversation)](#11-phase-2-real-time-messaging)
12. [Phase 2: File Uploads (The Locker Room)](#12-phase-2-file-uploads)
13. [Phase 3: AI Engine with LangGraph](#13-phase-3-ai-engine-with-langgraph)
14. [Phase 3: Email Notifications (The Mailroom)](#14-phase-3-email-notifications)
15. [Phase 3: Rate Limiting (The Traffic Police)](#15-phase-3-rate-limiting)
16. [Phase 3: Background Jobs (The Night Shift)](#16-phase-3-background-jobs)
17. [Phase 3: Admin Dashboard (Mission Control)](#17-phase-3-admin-dashboard)
18. [How Everything Connects (The Full Flow)](#18-how-everything-connects)
19. [Common Mistakes We Made (and Fixed)](#19-common-mistakes-we-made)
20. [API Cheat Sheet (Complete)](#20-api-cheat-sheet)
21. [Going to Production](#21-going-to-production)
22. [The Universal Backend Blueprint](#22-the-universal-backend-blueprint)
23. [The Developer Memory Framework](#23-the-developer-memory-framework)

---

## 🗺️ How This Document Flows

Before you dive in, here's a map showing how every section connects. Each section builds on the one before it — no skipping!

```mermaid
flowchart TD
    S1["🍽️ 1. What Is a Backend?\n(The Big Picture)"]
    S2["🧰 2. Tech Stack\n(The Tools)"]
    S3["📂 3. Folder Structure\n(The Map)"]
    S4["⚙️ 4. Foundation Files\n(Config + DB + Entry Point)"]
    S5["📦 5. Database Models\n(Tables & Relationships)"]
    S6["🛡️ 6. Pydantic Schemas\n(Input/Output Guards)"]
    S7["🔐 7. Authentication\n(JWT + Passwords)"]
    S8["🌐 8. API Endpoints\n(The URLs)"]
    S9["🏦 9. Escrow Engine\n(Payment Vault)"]
    S10["⭐ 10. Reviews\n(Reputation System)"]
    S11["💬 11. Messaging\n(Real-time Chat)"]
    S12["📎 12. File Uploads\n(The Locker Room)"]
    S13["🤖 13. AI Engine\n(LangGraph Workflows)"]
    S14["📧 14. Email\n(Notifications)"]
    S15["🚦 15. Rate Limiting\n(Traffic Police)"]
    S16["🌙 16. Background Jobs\n(The Night Shift)"]
    S17["🎛️ 17. Admin Dashboard\n(Mission Control)"]
    S18["🔗 18. Full Flow\n(How It All Connects)"]
    S19["🐛 19. Common Mistakes\n(Learn From Our Bugs)"]
    S20["📋 20. API Cheat Sheet\n(Quick Reference)"]
    S21["🚀 21. Going to Production\n(Deploy Checklist)"]
    S22["📐 22. Universal Blueprint\n(Build ANY Backend)"]
    S23["🧠 23. Memory Framework\n(Remember It Forever)"]

    S1 -->|"Understand the concept"| S2
    S2 -->|"Know your tools"| S3
    S3 -->|"Navigate the code"| S4
    S4 -->|"Foundation ready"| S5
    S5 -->|"Tables exist"| S6
    S6 -->|"Validation ready"| S7
    S7 -->|"Auth ready"| S8
    S8 -->|"Basic API done"| S9
    S8 -->|"Basic API done"| S10
    S8 -->|"Basic API done"| S11
    S8 -->|"Basic API done"| S12
    S9 -->|"Advanced features"| S13
    S10 -->|"Advanced features"| S13
    S13 -->|"AI done"| S14
    S14 -->|"Email done"| S15
    S15 -->|"Security done"| S16
    S16 -->|"Jobs done"| S17
    S17 -->|"Admin done"| S18
    S18 -->|"Understand the whole system"| S19
    S19 -->|"Learn from mistakes"| S20
    S20 -->|"Quick reference ready"| S21
    S21 -->|"Know how to deploy"| S22
    S22 -->|"Generalize the knowledge"| S23

    style S1 fill:#1e3a5f,stroke:#4a9eff,color:#fff
    style S2 fill:#1e3a5f,stroke:#4a9eff,color:#fff
    style S3 fill:#1e3a5f,stroke:#4a9eff,color:#fff
    style S4 fill:#2d4a1e,stroke:#6abf40,color:#fff
    style S5 fill:#2d4a1e,stroke:#6abf40,color:#fff
    style S6 fill:#2d4a1e,stroke:#6abf40,color:#fff
    style S7 fill:#2d4a1e,stroke:#6abf40,color:#fff
    style S8 fill:#2d4a1e,stroke:#6abf40,color:#fff
    style S9 fill:#5a2d1e,stroke:#ff8c42,color:#fff
    style S10 fill:#5a2d1e,stroke:#ff8c42,color:#fff
    style S11 fill:#5a2d1e,stroke:#ff8c42,color:#fff
    style S12 fill:#5a2d1e,stroke:#ff8c42,color:#fff
    style S13 fill:#5a2d1e,stroke:#ff8c42,color:#fff
    style S14 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S15 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S16 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S17 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S18 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S19 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
    style S20 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
    style S21 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
    style S22 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
    style S23 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
```

> **🎨 Color Key:**
> - 🔵 **Blue** = Conceptual Foundation (Sections 1–3) — Understand before you code
> - 🟢 **Green** = Phase 1: Core Backend (Sections 4–8) — The bread and butter
> - 🟠 **Orange** = Phase 2–3: Features (Sections 9–13) — Escrow, Reviews, Chat, Files, AI
> - 🟣 **Purple** = Phase 3: Infrastructure (Sections 14–18) — Email, Security, Jobs, Admin, Flow
> - 🔴 **Red** = Level Up (Sections 19–23) — Mistakes, Cheat Sheet, Production, Blueprints, Memory

---

## 1. What Even Is a Backend?

### 🍽️ The Restaurant Story

Imagine you walk into a restaurant called **OrbitHire Bistro**:

- **Frontend** = The dining room. It's what you (the customer) see — the menu, the tables, the decor. In our case, this is the **Vite + React** website.
- **Backend** = The kitchen. You never see it, but it's where all the real work happens — cooking the food, storing ingredients, checking if you've paid your bill.
- **Database** = The fridge and pantry. It stores all the raw ingredients (data) that the kitchen needs.
- **API** = The waiter. Takes orders from the dining room (frontend), walks them to the kitchen (backend), and brings the food (data) back.

Now, OrbitHire Bistro isn't a simple restaurant. It has **7 departments**:

| Department | What It Does | Real Feature |
|---|---|---|
| 🔐 **Security Desk** | Checks your ID at the door | User authentication (JWT) |
| 📋 **Job Board** | Posts help-wanted signs | Job posting & discovery |
| 📝 **Proposal Counter** | Where freelancers submit pitches | Proposal submission |
| 🏦 **Bank Vault** | Holds money safely until work is done | Escrow payments |
| 💬 **Communication Hub** | Internal phone system | Real-time messaging |
| ⭐ **Review Board** | Customer satisfaction scores | Ratings & reviews |
| 🤖 **AI Assistant** | A genius robot that matches people | AI matching & drafting |

**Our backend handles ALL of these departments.** When you understand this document, you'll know how every single one works under the hood.

---

## 2. The Tech Stack

### 🧰 The Toolbox — What Each Tool Does

| Tool | What It Does | Analogy |
|---|---|---|
| **Python 3.12** | The programming language | The language the chef speaks |
| **FastAPI** | Web framework that creates API endpoints | The restaurant's ordering system |
| **SQLAlchemy** | Talks to the database using Python | A translator between chef and pantry |
| **SQLite / PostgreSQL** | The database (SQLite for dev, PostgreSQL for prod) | The fridge that stores everything |
| **Pydantic** | Validates incoming data | The quality inspector at the kitchen door |
| **JWT (PyJWT)** | Login sessions (proves who you are) | Your restaurant loyalty card |
| **Argon2** | Hashes passwords securely | A one-way padlock on your locker |
| **LangChain + LangGraph** | Orchestrates AI workflows | An AI sous-chef that helps with recipes |
| **Groq** | The LLM provider (runs the AI model) | The brain of the AI sous-chef |
| **slowapi** | Rate limiting (prevents abuse) | A bouncer counting how fast you're ordering |
| **APScheduler** | Background jobs on a timer | The night-shift cleaner who works after hours |
| **Uvicorn** | ASGI server that runs our app | The power supply keeping the kitchen running |
| **Vite + React** | The frontend (what users see) | The beautiful dining room |
| **Wouter** | Client-side routing in React | The hostess directing you to your table |

### The Python Dependencies

```
# Core Framework
fastapi              ← The web framework
uvicorn              ← ASGI server (runs FastAPI)
pydantic             ← Data validation
pydantic-settings    ← Loads config from .env files

# Database
sqlalchemy           ← Database ORM (Object-Relational Mapper)
aiosqlite            ← Async SQLite driver (development)
asyncpg              ← Async PostgreSQL driver (production)

# Security
pyjwt                ← Creates and verifies JWT tokens
passlib              ← Password hashing framework
argon2-cffi          ← Argon2 password hashing algorithm

# AI
langchain            ← AI orchestration library
langgraph            ← Multi-step AI workflow engine
langchain-groq       ← Connects LangChain to Groq's LLMs

# Infrastructure
slowapi               ← API rate limiting
apscheduler           ← Background job scheduling
python-multipart      ← Handles file uploads in forms
aiofiles              ← Async file I/O

# Document Generation
python-docx           ← Generates Word documents
python-pptx           ← Generates PowerPoint presentations
```

### 🧐 Why Argon2 Instead of Bcrypt?

**Story time:** We originally used `bcrypt` for password hashing (the industry standard). But in 2025, the `bcrypt` Python library released version 5.0 which broke compatibility with `passlib` — the wrapper we use. Every time a user tried to register, the server crashed with:

```
ValueError: password cannot be longer than 72 bytes
```

**The fix:** We switched to **Argon2** — which is actually *newer and better* than bcrypt. It won the [Password Hashing Competition](https://en.wikipedia.org/wiki/Argon2) in 2015 and is now the recommended algorithm by OWASP. Think of it as upgrading from a good padlock to a biometric fingerprint lock.

```python
# OLD (broken):
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# NEW (works):
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
```

The beauty of `passlib`'s `CryptContext` is that this one-line change automatically handles everything — hashing, verifying, and even auto-upgrading old bcrypt hashes to argon2 when users log in.

---

## 3. Project Folder Structure

```
free/
├── .env                              ← 🔑 Secret keys (NEVER commit to GitHub)
├── pyproject.toml                    ← Python project configuration
├── freelance_saas.db                 ← The SQLite database file (auto-created)
│
├── app/                              ← ALL backend code lives here
│   ├── __init__.py                   ← Makes "app" a Python package
│   ├── main.py                       ← 🚀 THE ENTRY POINT (starts the server)
│   │
│   ├── core/                         ← ⚙️ INFRASTRUCTURE (the building's pipes & wires)
│   │   ├── config.py                 ← App settings (loaded from .env)
│   │   ├── database.py               ← Database connection + session factory
│   │   ├── security.py               ← JWT token creation + user auth guard
│   │   ├── email_service.py          ← 📧 SMTP email notifications
│   │   ├── rate_limiter.py           ← 🚦 slowapi rate limiting setup
│   │   ├── scheduler.py              ← 🌙 Background job scheduler
│   │   ├── payment_service.py        ← 💳 Razorpay payment integration
│   │   └── ai_service.py             ← 🤖 AI credit checking + deduction
│   │
│   ├── models/                       ← 📦 DATABASE TABLES (what gets stored)
│   │   ├── __init__.py               ← Registers ALL models for SQLAlchemy
│   │   ├── tenant.py                 ← Multi-tenant organizations
│   │   ├── user.py                   ← User accounts + Freelancer profiles + Company profiles
│   │   ├── job.py                    ← Job postings by clients
│   │   ├── proposal.py               ← Freelancer proposals / bids
│   │   ├── credit.py                 ← Credit wallet + transaction history
│   │   ├── escrow.py                 ← Payment escrow vault
│   │   ├── milestone.py              ← Project milestones / deliverables
│   │   ├── review.py                 ← Ratings & reviews
│   │   ├── message.py                ← Conversations + Messages
│   │   ├── notification.py           ← In-app notifications
│   │   ├── file.py                   ← Uploaded file metadata
│   │   └── dispute.py                ← Escrow dispute records
│   │
│   ├── schemas/                      ← 🛡️ DATA VALIDATORS (what the API accepts/returns)
│   │   ├── user.py                   ← User registration, login, profile schemas
│   │   ├── job.py                    ← Job create/update/list schemas
│   │   ├── proposal.py               ← Proposal create/response schemas
│   │   ├── credit.py                 ← Credit wallet/purchase schemas
│   │   ├── escrow.py                 ← Escrow create/response schemas
│   │   ├── review.py                 ← Review create/response schemas
│   │   └── message.py                ← Message/conversation schemas
│   │
│   ├── api/v1/                       ← 🌐 API ENDPOINTS (the URLs the frontend calls)
│   │   ├── auth.py                   ← POST /register, POST /login, GET /me
│   │   ├── freelancers.py            ← Profile CRUD + Browse freelancers
│   │   ├── clients.py                ← Company profile CRUD
│   │   ├── jobs.py                   ← Job CRUD + Search + AI matching
│   │   ├── proposals.py              ← Submit, withdraw, accept/reject + AI draft
│   │   ├── escrow.py                 ← Create, fund, release, dispute + webhook
│   │   ├── milestones.py             ← Create, update, complete milestones
│   │   ├── credits.py                ← Balance, history, purchase packs
│   │   ├── messages.py               ← Conversations + Messages + WebSocket chat
│   │   ├── reviews.py                ← Submit + View reviews
│   │   ├── notifications.py          ← List + Mark-read notifications
│   │   ├── uploads.py                ← Upload, download, delete files
│   │   └── admin.py                  ← Platform stats, user management, disputes
│   │
│   ├── ai/                           ← 🤖 AI ENGINE (LangGraph workflows)
│   │   ├── state.py                  ← AI state definitions (TypedDicts)
│   │   ├── matchmaker.py             ← AI freelancer ranking
│   │   └── drafter.py                ← AI proposal drafting
│   │
│   └── ai_engine/                    ← 📄 DOCUMENT GENERATORS
│       └── generators/
│           ├── docx_builder.py       ← Generate Word proposals
│           └── pptx_builder.py       ← Generate PowerPoint pitches
│
└── freelance-ai-marketplace/         ← 🎨 FRONTEND (Vite + React)
    └── client/
        └── src/
            ├── App.tsx               ← Root component with routes
            ├── lib/api.ts            ← API client (fetch wrapper)
            ├── contexts/AuthContext.tsx ← Authentication state
            ├── components/           ← Reusable UI components
            └── pages/                ← Page components (15 pages)
                ├── Home.tsx          ← Landing page
                ├── Login.tsx         ← Login form
                ├── Register.tsx      ← Registration form
                ├── Dashboard.tsx     ← Main dashboard
                ├── Jobs.tsx          ← Job listing + proposal dialog
                ├── PostJob.tsx       ← Job composer
                ├── Proposals.tsx     ← Proposal management
                ├── Wallet.tsx        ← Credit wallet + purchases
                ├── Messages.tsx      ← Chat interface
                ├── Reviews.tsx       ← Review history
                ├── Profile.tsx       ← Freelancer profile editor
                ├── ClientProfile.tsx ← Company profile editor
                ├── Admin.tsx         ← Admin dashboard
                └── Settings.tsx      ← Account settings
```

### Why This Structure?

Think of it like a **hospital**:
- **`core/`** = The hospital's infrastructure (power, water, security cameras, phone system)
- **`models/`** = The patient records system (what data gets stored in filing cabinets)
- **`schemas/`** = The intake forms (what information we collect from visitors at the front desk)
- **`api/`** = The reception desk (where visitors make requests)
- **`ai/`** = The specialist doctors (advanced AI-powered diagnostics)

Each folder has ONE job. This is called **Separation of Concerns** — the #1 rule of professional software engineering. The receptionist doesn't fix the wiring. The electrician doesn't treat patients.

---

## 4. Phase 0: The Foundation Files

Before we write a single API endpoint, we need to set up three foundational systems: Configuration, Database, and the Entry Point.

Think of it like building a house: you don't start with the furniture. You start with the foundation, the plumbing, and the electrical wiring.

---

### 4A. Configuration — `app/core/config.py`

```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Freelance AI Saas"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "super_secret_jwt_key_change_me_in_prod"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    DATABASE_URL: str = "sqlite+aiosqlite:///./freelance_saas.db"

    # AI
    GROQ_API_KEY: Optional[str] = None

    # Credit System
    FREE_MONTHLY_CREDITS: int = 5
    PROPOSAL_BASE_CREDIT_COST: int = 1
    AI_PROPOSAL_CREDIT_COST: int = 2

    # Razorpay (Payment Gateway)
    RAZORPAY_KEY_ID: Optional[str] = None
    RAZORPAY_KEY_SECRET: Optional[str] = None

    # SMTP Email
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USERNAME: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    # Platform fee (10% from each side)
    PLATFORM_FEE_PERCENT: float = 10.0
    ESCROW_HOLD_DAYS: int = 7

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
```

**What is this?** A single source of truth for every setting in the entire app.

**Why do we need it?**
- Instead of typing `"sqlite+aiosqlite:///./freelance_saas.db"` in 15 different files, we type `settings.DATABASE_URL` once.
- The `env_file=".env"` part means: "If there's a `.env` file, load secrets from there." This way, your passwords never appear in your code.
- The `extra="ignore"` part means: "If the `.env` file has extra variables I don't know about, just ignore them."

**The `Optional[str] = None` Pattern:**
Many settings (like `GROQ_API_KEY`, `RAZORPAY_KEY_ID`, `SMTP_HOST`) are optional. The app works without them — AI features gracefully degrade, payments run in simulation mode, and emails are logged to console instead of sent. This lets you develop locally without configuring everything upfront.

**Key Settings:**
| Setting | Default | What It Controls |
|---|---|---|
| `SECRET_KEY` | `"super_secret..."` | JWT encryption key. **Change in production!** |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | 11,520 (8 days) | How long a login session lasts |
| `DATABASE_URL` | SQLite | Where data is stored |
| `FREE_MONTHLY_CREDITS` | 5 | Free credits given to each user monthly |
| `PLATFORM_FEE_PERCENT` | 10.0 | Fee taken from each side of a transaction |
| `ESCROW_HOLD_DAYS` | 7 | Days before auto-releasing escrowed funds |

---

### 4B. Database Connection — `app/core/database.py`

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# Step 1: Create the "engine" (the connection to the database)
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# Step 2: Create a "session factory" (produces fresh database sessions)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Step 3: Define the "Base" class (all models inherit from this)
class Base(DeclarativeBase):
    pass

# Step 4: The dependency function (gives each API request its own session)
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
```

**🏗️ The Construction Analogy:**

1. **Engine** = The phone line to the database. `echo=True` means it prints every SQL query to the console (great for debugging, turn off in production).

2. **Session Factory** = A machine that produces fresh conversations with the database. Every API request gets its own conversation — like giving each customer their own waiter.

3. **Base** = The parent class for ALL database tables. Every model (User, Job, Proposal) inherits from `Base`, which tells SQLAlchemy: "This Python class should become a real database table."

4. **`get_db()`** = A "dependency" function. FastAPI automatically calls this before each request and gives the endpoint a fresh session. The `yield` keyword means: "Give the session to the endpoint, wait for it to finish, then clean up."

**Why `async`?** Normal database operations BLOCK your server — while one request waits for the database, no other request can run. `async` means many requests run simultaneously. It's like having 10 waiters instead of 1.

---

### 4C. The Entry Point — `app/main.py`

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import Base, engine
from app.core.rate_limiter import setup_rate_limiting
from app.core.scheduler import start_scheduler, scheduler

# Import ALL routers (13 total)
from app.api.v1.auth import router as auth_router
from app.api.v1.freelancers import router as freelancer_router
from app.api.v1.jobs import router as jobs_router
from app.api.v1.escrow import router as escrow_router
from app.api.v1.proposals import router as proposals_router
from app.api.v1.credits import router as credits_router
from app.api.v1.clients import router as clients_router
from app.api.v1.milestones import router as milestones_router
from app.api.v1.reviews import router as reviews_router
from app.api.v1.messages import router as messages_router
from app.api.v1.notifications import router as notifications_router
from app.api.v1.uploads import router as uploads_router
from app.api.v1.admin import router as admin_router

# Import all models so SQLAlchemy discovers them
import app.models  # noqa: F401

# Lifespan: runs on startup & shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP: Create tables + start background jobs
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    start_scheduler()
    yield
    # SHUTDOWN: Stop background jobs
    scheduler.shutdown(wait=False)

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

# Rate Limiting
setup_rate_limiting(app)

# CORS: Allow the frontend to talk to our backend
app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Wire up every router with a URL prefix
app.include_router(auth_router,          prefix="/api/v1/auth",          tags=["Authentication"])
app.include_router(freelancer_router,    prefix="/api/v1/freelancers",   tags=["Freelancers"])
app.include_router(clients_router,       prefix="/api/v1/clients",       tags=["Clients"])
app.include_router(jobs_router,          prefix="/api/v1/jobs",          tags=["Jobs"])
app.include_router(proposals_router,     prefix="/api/v1/proposals",     tags=["Proposals"])
app.include_router(escrow_router,        prefix="/api/v1/escrow",        tags=["Escrow"])
app.include_router(milestones_router,    prefix="/api/v1/milestones",    tags=["Milestones"])
app.include_router(credits_router,       prefix="/api/v1/credits",       tags=["Credits"])
app.include_router(messages_router,      prefix="/api/v1/messages",      tags=["Messages"])
app.include_router(reviews_router,       prefix="/api/v1/reviews",       tags=["Reviews"])
app.include_router(notifications_router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(uploads_router,       prefix="/api/v1/uploads",       tags=["Uploads"])
app.include_router(admin_router,         prefix="/api/v1/admin",         tags=["Admin"])
```

**What is this?** The control center. It:
1. Creates the FastAPI application.
2. Sets up the **lifespan** (startup/shutdown hooks) — creates all database tables and starts the background scheduler.
3. Enables **CORS** (so the React frontend can talk to the backend).
4. Enables **rate limiting** (prevents API abuse).
5. Connects all **13 routers** to URL prefixes.

**What is CORS?** By default, a website at `localhost:3001` (React) cannot call an API at `localhost:8000` (FastAPI) because browsers block "cross-origin" requests for security. CORS middleware says: "These specific origins are trusted — let them through."

**What is a Router?** Instead of writing all 40+ endpoints in `main.py` (which would be a 3,000-line nightmare), we split them into separate files. Each file has its own `APIRouter()`. Then `main.py` connects them all together with `include_router()`. Like separate departments in a company — each with their own manager.

**Why `import app.models`?** SQLAlchemy only knows about a model if Python has actually executed the file. By importing `app.models` (which re-exports all models in its `__init__.py`), we guarantee every table is registered before `create_all` runs.

**What's the `lifespan` pattern?** The old `@app.on_event("startup")` decorator is deprecated. The modern FastAPI way is to use an `asynccontextmanager`: everything before `yield` runs on startup, everything after runs on shutdown. Clean and Pythonic.

---

## 5. Phase 1: Database Models

A **model** is a Python class that represents a database table. Each attribute of the class becomes a column in the table.

### 🏗️ Building Analogy

If the database is an apartment building:
- Each **model** is a floor plan (blueprint for one type of apartment)
- Each **row** in the table is one actual apartment built from that plan
- Each **column** is a feature of the apartment (number of rooms, area, floor number)
- **Foreign keys** are the hallways connecting apartments on different floors
- **Relationships** are the elevators that let you quickly jump between connected floors

---

### 5A. The Tenant Model — `app/models/tenant.py`

```python
class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    custom_domain: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
    branding: Mapped[dict] = mapped_column(JSON, default=dict)
```

**What is a Tenant?** This app is "multi-tenant" — meaning multiple companies can use the same backend. Think of it like an apartment building: each apartment (tenant) is separate, but they all share the same building (server). By default, everyone joins the "OrbitHire" tenant.

**Key concepts:**
- `primary_key=True` → This column uniquely identifies every row. Like a passport number.
- `default=lambda: str(uuid.uuid4())` → Auto-generates a random unique ID. `uuid4()` creates IDs like `"a1b2c3d4-e5f6-7890-abcd-ef1234567890"`.
- `nullable=False` → This field MUST have a value. You can't leave it empty.
- `unique=True` → No two tenants can have the same slug or domain.
- `index=True` → Creates a search index (makes lookups much faster, like an index in a textbook).

---

### 5B. The User Model — `app/models/user.py`

```python
class UserRole(str, enum.Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    TENANT_ADMIN = "TENANT_ADMIN"
    CLIENT = "CLIENT"
    FREELANCER = "FREELANCER"

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=...)
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=True)  # Nullable for Google OAuth
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(Enum(UserRole), default=UserRole.FREELANCER)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    google_id: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=...)

    # Relationships — think of these as "elevators" to connected tables
    tenant: Mapped["Tenant"] = relationship("Tenant", back_populates="users")
    freelancer_profile: Mapped["FreelancerProfile"] = relationship(back_populates="user", uselist=False)
    credit_wallet: Mapped["CreditWallet"] = relationship(back_populates="user", uselist=False)
```

**New concepts:**

**`ForeignKey("tenants.id")`** → A link to another table. It says: "Every user MUST belong to a tenant." Like saying every employee must work at a company. If you try to create a user with a `tenant_id` that doesn't exist in the `tenants` table, the database will reject it.

**`relationship()`** → Creates a navigation shortcut. Instead of writing a SQL query to find a user's profile, you can just write `user.freelancer_profile` and SQLAlchemy automatically fetches it from the related table.

**`back_populates`** → Makes the relationship two-way. If `User` has `freelancer_profile`, then `FreelancerProfile` has `user`. They point to each other like a two-way street.

**`uselist=False`** → "This relationship returns ONE object, not a list." A user has ONE profile, not many. Without this, SQLAlchemy would return a list like `[profile]` instead of just `profile`.

**`cascade="all, delete-orphan"`** → "If I delete the user, automatically delete their profile too." No orphan data left behind. Like cancelling a phone plan automatically cancels the number.

**Why `password_hash` and not `password`?** We NEVER store raw passwords. We run them through Argon2 (a one-way encryption algorithm) that turns `"mypassword123"` into `"$argon2id$v=19$m=65536,t=3,p=4$..."`. Even if a hacker steals the entire database, they can't reverse the hash to get the original password. It's mathematically impossible.

**Why is `password_hash` nullable?** Because users who sign in with Google OAuth don't have a password at all — they authenticate through Google's servers instead.

---

### 5C. The FreelancerProfile Model

```python
class FreelancerProfile(Base):
    __tablename__ = "freelance_profiles"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=...)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), unique=True)
    title: Mapped[str] = mapped_column(String(150), nullable=True)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    skills: Mapped[list] = mapped_column(JSON, default=list)
    hourly_rate: Mapped[float] = mapped_column(Float, default=0.0)
    portfolio: Mapped[dict] = mapped_column(JSON, default=list)
    avg_rating: Mapped[float] = mapped_column(Float, default=0.0)
    jobs_completed: Mapped[int] = mapped_column(Integer, default=0)
    success_rate: Mapped[float] = mapped_column(Float, default=0.0)
```

**Why a separate table?** Not every user is a freelancer. Clients don't need `skills`, `hourly_rate`, or `portfolio`. By putting this in a separate table with a `user_id` foreign key, we keep the User table lean and only create profile rows for actual freelancers. This is called **table normalization**.

**`JSON` columns:** `skills` stores a Python list like `["React", "Python", "FastAPI"]` as a JSON string in the database. SQLite and PostgreSQL both support JSON columns natively.

---

### 5D. The Complete Model Map

Here's how ALL 13 models connect to each other:

```
                          ┌─────────┐
                          │ TENANT  │
                          └────┬────┘
                               │ has many
                          ┌────┴────┐
                    ┌─────┤  USER   ├─────┐
                    │     └────┬────┘     │
                    │          │          │
              ┌─────┴──┐  ┌───┴───┐  ┌───┴──────┐
              │FREELANCE│  │CREDIT │  │ COMPANY  │
              │PROFILE  │  │WALLET │  │ PROFILE  │
              └────┬────┘  └───┬───┘  └──────────┘
                   │           │
    ┌──────────────┼───────────┼──────────────┐
    │              │           │              │
┌───┴────┐   ┌────┴───┐  ┌───┴─────┐  ┌────┴─────┐
│JOB POST│   │PROPOSAL│  │ CREDIT  │  │  REVIEW  │
│        ├───┤        │  │  TRANS  │  │          │
└───┬────┘   └────────┘  └─────────┘  └──────────┘
    │
    ├──────────┬────────────┐
    │          │            │
┌───┴───┐ ┌───┴──────┐ ┌───┴────────┐
│ESCROW │ │MILESTONE │ │CONVERSATION│
└───┬───┘ └──────────┘ └──────┬─────┘
    │                         │
┌───┴────┐              ┌────┴────┐
│DISPUTE │              │ MESSAGE │
└────────┘              └─────────┘
```

**State machines** (models that have a `status` field that progresses through stages):
- **JobPost**: `OPEN → IN_PROGRESS → COMPLETED / CANCELLED`
- **Proposal**: `SUBMITTED → SHORTLISTED → APPROVED / REJECTED / WITHDRAWN`
- **Escrow**: `PENDING_PAYMENT → HELD → RELEASED / DISPUTED → REFUNDED`
- **Milestone**: `PENDING → IN_PROGRESS → COMPLETED → APPROVED`
- **Dispute**: `OPEN → UNDER_REVIEW → RESOLVED_CLIENT / RESOLVED_FREELANCER / RESOLVED_SPLIT`

---

## 6. Phase 1: Pydantic Schemas

### Models vs Schemas: What's the Difference?

| | Model | Schema |
|---|---|---|
| **Lives in** | `app/models/` | `app/schemas/` |
| **Purpose** | Defines database tables | Validates API input/output |
| **Talks to** | The database | The frontend |
| **Analogy** | The fridge layout (where to store things) | The menu (what customers can order) |

**Why do we need both?**

Imagine this: the `User` model has a `password_hash` column. If we returned the model directly to the frontend, the user would see their hashed password in the API response! Schemas let us control exactly what data goes in and comes out.

### Types of Schemas

**Response Schema** (what we send back to the frontend):
```python
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Read from DB objects
    id: str
    email: str
    full_name: str
    role: UserRole
    is_active: bool
    is_verified: bool
    created_at: datetime
    # Notice: NO password_hash! We NEVER expose this.
```

**Input Schema** (what we receive from the frontend):
```python
class UserRegister(BaseModel):
    full_name: str
    email: EmailStr                  # Validates email format automatically
    password: str
    role: UserRole = UserRole.FREELANCER
    tenant_id: str = "default-tenant"
    # Notice: NO id, NO password_hash, NO is_active, NO created_at
    # These are all set AUTOMATICALLY by the server.
```

**Why are input schemas so small?** Because we never trust the frontend! If we let the frontend send `client_id`, a hacker could open browser DevTools, change the value to someone else's ID, and impersonate them. Instead, we pull `client_id` from the JWT token (which is cryptographically signed and cannot be tampered with).

### The `from_attributes=True` Setting

```python
model_config = ConfigDict(from_attributes=True)
```

This tells Pydantic: "I'm going to give you a SQLAlchemy database object (not a dictionary). Please read its attributes to build the response." Without this, Pydantic would crash when you try to return a database row because it doesn't know how to read SQLAlchemy objects.

### Optional Fields

```python
release_date: datetime | None = None
updated_at: datetime | None = None
```

The `| None = None` syntax means: "This field can either be a `datetime` or `None`, and it defaults to `None`." We use this for fields that might not have a value yet (e.g., `release_date` is empty until payment is confirmed).

**Golden Rule:** If the database column has `nullable=True`, the schema field MUST use `| None = None`. Otherwise, Pydantic will crash when it reads a null value from the database.

---

## 7. Phase 1: Authentication

### 🔐 The Nightclub Bouncer Analogy

Think of authentication like getting into a nightclub:

1. **Registration** = Getting your ID card made (you give your name and photo, they create a membership)
2. **Login** = Showing your ID at the door (bouncer checks it's real and lets you in)
3. **JWT Token** = Your wristband (once inside, you show the wristband to access VIP areas — you don't show your ID every time)
4. **Token Expiry** = The wristband expires at 2 AM (you need to come back to the door to get a new one)

---

### 7A. Password Security — `app/api/v1/auth.py`

```python
from passlib.context import CryptContext

# The password hasher — using Argon2 (winner of the Password Hashing Competition)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Hashing: "password123" → "$argon2id$v=19$m=65536,t=3,p=4$..."
hashed = pwd_context.hash("password123")

# Verifying: Does "password123" match the hash?
is_valid = pwd_context.verify("password123", hashed)  # True
is_valid = pwd_context.verify("wrongpassword", hashed)  # False
```

**How Argon2 works (simplified):**
1. Take the password: `"password123"`
2. Add random "salt": `"password123" + "xK9mQ2"` (different every time)
3. Run through a memory-hard, CPU-intensive function
4. Output: `"$argon2id$v=19$m=65536,t=3,p=4$..."` (impossible to reverse)

Even if two users have the same password, their hashes will be different (because the salt is random). Even if a hacker steals the entire database, they can't reverse the hashes. It would take centuries of computing power to crack even one.

**Why Argon2 over bcrypt?**
- bcrypt limits passwords to 72 bytes (breaks with modern library versions)
- Argon2 uses both CPU and RAM, making hardware-based attacks much harder
- Argon2 won the international [Password Hashing Competition](https://en.wikipedia.org/wiki/Argon2) — it's the scientific consensus for best practice

---

### 7B. JWT Tokens — How Login Works

```python
import jwt
from datetime import datetime, timedelta

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
```

**What is a JWT?** A JWT (JSON Web Token) is a digitally signed ID card. After you log in, the server gives you a token like:

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyLTEyMyIsInJvbGUiOiJGUkVFTEFOQ0VSIn0.abc123
```

If you paste this into [jwt.io](https://jwt.io), you'll see it has three parts separated by dots:
- **Header**: `{"alg": "HS256"}` — The encryption algorithm
- **Payload**: `{"sub": "user-123", "role": "FREELANCER", "tenant_id": "abc", "exp": 1692...}` — The data
- **Signature**: A cryptographic proof that our server created this token (if anyone modifies the payload, the signature breaks)

The frontend stores this token in `localStorage` and sends it with every request as: `Authorization: Bearer eyJhbG...`

**Why not just use cookies/sessions?** JWTs are **stateless** — the server doesn't need to store anything. A session-based system needs a "sessions" table in the database that gets queried on every request. With JWT, the token itself contains all the information. This makes scaling to millions of users much easier.

---

### 7C. The Auth Guard — `get_current_user()`

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
```

**The flow (step by step):**
1. Frontend sends: `Authorization: Bearer eyJhbG...`
2. `oauth2_scheme` extracts the token from the `Authorization` header
3. `jwt.decode()` verifies the signature and extracts `{"sub": "user-123", "role": "FREELANCER"}`
4. We query the database to make sure the user still exists (maybe they were banned since they logged in)
5. We return the full `User` object to the endpoint

**This function is a "dependency."** Any endpoint that needs to know who's making the request just adds `current_user: User = Depends(get_current_user)` to its parameters. FastAPI automatically calls `get_current_user()` before the endpoint runs. It's like a security checkpoint — every protected room in the building requires a badge scan.

---

## 8. Phase 1: API Endpoints

### The Pattern Every Endpoint Follows

Every single API endpoint in the history of software follows this 5-step pattern. Remember **VACDR** (like "VADER" from Star Wars):

```
V → Validate      (Pydantic schema checks the input)
A → Authenticate   (JWT proves who you are)
C → Check role     (Are you allowed to do this?)
D → Database       (Read or write data)
R → Return         (Send the response)
```

If you're debugging an endpoint and it's not working, walk through VACDR step by step. The bug is always in one of these 5 steps.

---

### 8A. Registration — `POST /api/v1/auth/register`

```python
@router.post("/register", response_model=TokenResponse, status_code=201)
@limiter.limit("5/minute")  # Rate limit: max 5 registrations per minute per IP
async def register(request: Request, payload: UserRegister, db: AsyncSession = Depends(get_db)):
    # V: Pydantic already validated `payload` (email format, required fields)
    
    # Password strength check
    if len(payload.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")

    # Check for duplicate email
    existing = await db.execute(select(User).where(User.email == payload.email))
    if existing.scalar_one_or_none() is not None:
        raise HTTPException(status_code=409, detail="An account with this email already exists")

    # Ensure tenant exists (auto-create default if needed)
    tenant_id = await ensure_default_tenant(db)

    # D: Create user with hashed password
    hashed_pass = pwd_context.hash(payload.password)
    new_user = User(
        full_name=payload.full_name,
        email=payload.email,
        password_hash=hashed_pass,
        role=payload.role.value,
        tenant_id=tenant_id,
    )
    db.add(new_user)          # "Hey database, I want to save this"
    await db.flush()          # Get the auto-generated ID without committing yet

    # Create credit wallet with 5 free welcome credits
    wallet = CreditWallet(user_id=new_user.id, balance=5)
    db.add(wallet)

    await db.commit()         # "Okay, NOW actually write everything to disk"
    await db.refresh(new_user) # "Reload from DB so I have the auto-generated fields"

    # Generate JWT token
    access_token = create_access_token(
        data={"sub": str(new_user.id), "role": new_user.role, "tenant_id": new_user.tenant_id}
    )

    # Send welcome email (non-blocking, fails silently if SMTP not configured)
    try:
        send_welcome_email(new_user.email, new_user.full_name, new_user.role)
    except Exception:
        pass

    # R: Return token + user data
    return TokenResponse(access_token=access_token, token_type="Bearer", user=UserResponse.model_validate(new_user))
```

**Key operations explained:**
- **`db.add()`** → "I want to save this object." Nothing is written yet.
- **`db.flush()`** → "Execute the SQL INSERT but don't commit the transaction yet." This gives us the auto-generated `id` so we can use it to create the wallet.
- **`db.commit()`** → "Now actually save everything permanently." If something fails between `flush` and `commit`, everything is rolled back — no half-saved data.
- **`db.refresh()`** → "Reload this object from the database." This populates auto-generated fields like `id` and `created_at`.

---

### 8B. Login — `POST /api/v1/auth/login`

```python
@router.post("/login", response_model=TokenResponse)
@limiter.limit("10/minute")  # Rate limit: max 10 login attempts per minute per IP
async def login(request: Request, payload: UserLogin, db: AsyncSession = Depends(get_db)):
    # Find user by email
    query = select(User).where(User.email == payload.email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="This account has been suspended")

    # Google OAuth users can't use password login
    if user.password_hash is None:
        raise HTTPException(status_code=400, detail="This account uses Google sign-in")

    # Verify password against stored hash
    is_valid = pwd_context.verify(payload.password, user.password_hash)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(
        data={"sub": str(user.id), "role": user.role, "tenant_id": user.tenant_id}
    )

    return TokenResponse(access_token=access_token, token_type="Bearer", user=UserResponse.model_validate(user))
```

**Security note:** We use the same error message `"Invalid email or password"` for both "email not found" and "wrong password". This prevents attackers from discovering which emails are registered in our system (called **user enumeration**).

**HTTP Status Codes:**
| Code | Meaning | When We Use It |
|---|---|---|
| 200 | OK | Everything worked |
| 201 | Created | New resource created (registration, new job, etc.) |
| 400 | Bad Request | Invalid data sent |
| 401 | Unauthorized | Not logged in or bad password |
| 402 | Payment Required | Not enough credits |
| 403 | Forbidden | Logged in but wrong role |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate (email already registered) |
| 413 | Payload Too Large | Uploaded file too big |
| 429 | Too Many Requests | Rate limit exceeded |

---

### 8C. Creating a Freelancer Profile

```python
@router.post("/profile")
async def create_profile(payload: ProfileCreate, db, current_user):
    if current_user.role != UserRole.FREELANCER:
        raise HTTPException(status_code=403, detail="Only freelancers can create profiles")

    profile = FreelancerProfile(
        user_id=current_user.id,  # ← Pulled from JWT, NOT from the frontend!
        title=payload.title,
        bio=payload.bio,
        skills=payload.skills,
        hourly_rate=payload.hourly_rate,
    )
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile
```

**Key Security Pattern:** `user_id = current_user.id` — we NEVER let the frontend tell us who they are. We pull it from the verified JWT token. This is the **#1 security rule** in backend development.

---

## 9. Phase 2: Escrow Engine

### 💰 The Used Car Story

Imagine you're buying a car from a stranger on the internet:
- You don't want to pay first (they might take the money and disappear).
- They don't want to ship first (you might receive the car and never pay).
- **Solution:** A trusted middleman (escrow) holds the money. Once you confirm the car arrived safely, the middleman releases the money to the seller.

**OrbitHire IS that middleman.** When a client hires a freelancer, the money goes into escrow — a protected vault. The freelancer can see the money is there (motivation to do great work), but can't touch it until the client confirms delivery.

### The Escrow State Machine

```
Client clicks "Hire"
         ↓
   PENDING_PAYMENT
         ↓
Razorpay confirms payment
         ↓
       HELD (7-day timer starts)
         ↓
  ┌──────┴──────────────────────┐
  ↓                             ↓
Day 3: Dispute raised?    Day 7: No dispute?
  ↓                             ↓
DISPUTED                    RELEASED
  ↓                    (Freelancer gets paid)
Admin resolves:
50/50 split (REFUNDED)
```

### The Fee Calculation — How OrbitHire Makes Money

```python
fee_rate = settings.PLATFORM_FEE_PERCENT / 100  # 0.10 (10%)
client_fee = payload.amount * fee_rate           # Client pays 10% extra
freelancer_fee = payload.amount * fee_rate       # Freelancer receives 10% less
total_charged = payload.amount + client_fee      # What the client actually pays
net_payout = payload.amount - freelancer_fee     # What the freelancer receives
```

For a **$1,000 project**:
| | Amount |
|---|---|
| Project budget | $1,000 |
| Client fee (10%) | +$100 |
| **Client pays** | **$1,100** |
| Freelancer fee (10%) | -$100 |
| **Freelancer receives** | **$900** |
| **OrbitHire keeps** | **$200** |

This is exactly how Upwork's fee structure works (they charge 10% from both sides too).

### Creating an Escrow — `POST /api/v1/escrow/create_order`

```python
@router.post("/create_order", response_model=EscrowResponse, status_code=201)
async def create_escrow_order(payload: EscrowCreate, db, current_user):
    # Validate: Does the job exist?
    result = await db.execute(select(JobPost).where(JobPost.id == payload.job_id))
    job = result.scalar_one_or_none()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    # Validate: Is this the actual client who posted the job?
    if job.client_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the client for this job")

    # Calculate fees (10% from each side)
    fee_rate = settings.PLATFORM_FEE_PERCENT / 100
    client_fee = payload.amount * fee_rate
    freelancer_fee = payload.amount * fee_rate
    total_charged = payload.amount + client_fee
    net_payout = payload.amount - freelancer_fee

    escrow = Escrow(
        job_id=payload.job_id,
        client_id=current_user.id,
        freelancer_id=payload.freelancer_id,
        amount=payload.amount,
        client_fee=client_fee,
        freelancer_fee=freelancer_fee,
        total_charged=total_charged,
        net_payout=net_payout,
        status=EscrowStatus.PENDING_PAYMENT,
    )
    db.add(escrow)
    await db.commit()
    return escrow
```

### The Razorpay Webhook — When Real Money Arrives

```python
@router.post("/webhook/razorpay")
async def razorpay_webhook(request: Request, db):
    data = await request.json()
    event = data.get("event")
    payload = data.get("payload", {})

    if event == "payment.captured":
        payment = payload.get("payment", {})
        order_id = payment.get("entity", {}).get("order_id")

        if order_id:
            result = await db.execute(select(Escrow).where(Escrow.razorpay_order_id == order_id))
            escrow = result.scalar_one_or_none()
            if escrow and escrow.status == EscrowStatus.PENDING_PAYMENT:
                escrow.status = EscrowStatus.HELD
                escrow.release_date = datetime.now(timezone.utc) + timedelta(days=7)
                await db.commit()

    return {"status": "ok"}
```

**What is a Webhook?** Unlike normal API calls where the FRONTEND calls US, a webhook is when a THIRD-PARTY SERVICE calls us. When Razorpay processes a payment, it sends a POST request to our `/webhook/razorpay` endpoint saying: "Payment confirmed." We then move the escrow from `PENDING_PAYMENT` to `HELD`.

**Why no `get_current_user`?** Webhooks don't come from logged-in users. They come from Razorpay's servers. In production, you'd verify Razorpay's cryptographic signature instead.

---

## 10. Phase 2: Reviews & Ratings

### ⭐ The Reputation System

Reviews are the trust currency of a marketplace. Without them, clients wouldn't know which freelancers to hire, and freelancers couldn't build a reputation.

```python
class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=...)
    job_id: Mapped[str] = mapped_column(String(36), ForeignKey("job_posts.id"))
    reviewer_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))
    reviewee_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  # 1-5
    communication_rating: Mapped[int] = mapped_column(Integer, nullable=True)
    quality_rating: Mapped[int] = mapped_column(Integer, nullable=True)
    timeliness_rating: Mapped[int] = mapped_column(Integer, nullable=True)
    comment: Mapped[str] = mapped_column(Text, nullable=True)
```

**Key validations:**
- Only completed jobs can be reviewed (`job.status == COMPLETED`)
- Each person can only review once per job (duplicate check)
- Rating must be 1-5 (database constraint)
- The freelancer's `avg_rating` is automatically recalculated after each review

---

## 11. Phase 2: Real-Time Messaging

### 💬 The Chat System

Our messaging system has two layers — like a phone system with both voicemail (REST) and live calls (WebSocket):

**Layer 1: REST API (the voicemail)** — For creating conversations, sending messages, and loading history. Works offline.

**Layer 2: WebSocket (the live call)** — For instant message delivery. When you send a message, everyone in the conversation sees it immediately without refreshing.

```python
class ConnectionManager:
    """Keeps track of which WebSocket connections are listening to which conversations."""
    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, conversation_id: str, websocket: WebSocket):
        await websocket.accept()
        if conversation_id not in self.active_connections:
            self.active_connections[conversation_id] = []
        self.active_connections[conversation_id].append(websocket)

    async def broadcast(self, conversation_id: str, message: dict):
        """Send a message to ALL connected clients in a conversation."""
        for ws in self.active_connections.get(conversation_id, []):
            await ws.send_json(message)
```

When a message is sent via the REST API, the server:
1. Saves it to the database
2. Creates an in-app notification
3. Sends an email notification (if SMTP is configured)
4. Broadcasts it via WebSocket to all connected clients

---

## 12. Phase 2: File Uploads

### 📎 The Locker Room

Users can upload images, documents, and videos. Think of it like a locker room at a gym — each user gets their own locker (folder), and the system keeps track of what's inside.

```python
ALLOWED_TYPES = {
    "image": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "document": [".pdf", ".doc", ".docx", ".pptx", ".xlsx", ".txt", ".md"],
    "video": [".mp4", ".webm", ".mov"],
}
```

**Security measures:**
- **File size limit:** 10MB max (configurable via `MAX_UPLOAD_SIZE_MB`)
- **Type whitelist:** Only allowed extensions are accepted (prevents uploading `.exe` files)
- **Unique filenames:** Files are renamed to UUIDs (`a1b2c3d4.pdf`) to prevent conflicts and path traversal attacks
- **User isolation:** Each user's files are stored in their own directory (`uploads/{user_id}/`)

---

## 13. Phase 3: AI Engine with LangGraph

### 🤖 The AI Sous-Chef

LangGraph is a framework for building multi-step AI workflows. Instead of making one giant prompt, you break the AI task into small, focused steps called **nodes**, and LangGraph runs them in sequence.

Think of it like an **assembly line**:
```
Raw Materials → Cut → Paint → Assemble → Quality Check → Final Product
```

Each station (node) does one job, then passes the result to the next station.

### The Matchmaker — `app/ai/matchmaker.py`

This AI reads a job description and ranks the best freelancers.

**Node 1: Extract Skills** — The LLM reads the job and extracts required skills.
**Node 2: Fetch Freelancers** — Queries the database for candidates with matching skills.
**Node 3: Rank Candidates** — The LLM scores each candidate on fit.

```python
workflow = StateGraph(MatchmakerState)
workflow.add_node("extract_skills", extract_skills)
workflow.add_node("fetch_freelancers", fetch_freelancers)
workflow.add_node("rank_candidates", rank_candidates)

workflow.add_edge(START, "extract_skills")
workflow.add_edge("extract_skills", "fetch_freelancers")
workflow.add_edge("fetch_freelancers", "rank_candidates")
workflow.add_edge("rank_candidates", END)

matchmaker_chain = workflow.compile()
```

### The Proposal Drafter — `app/ai/drafter.py`

This AI reads a freelancer's profile and a job description, then writes a professional proposal:

```python
def generate_draft(state: DraftState):
    prompt = f"""You are a senior copywriter.
    Write a professional proposal for this job using the tone of the freelancer.
    Job: {state['job_description']}
    Freelancer Bio: {state['freelancer_profile']}
    """
    response = llm.invoke(prompt)
    return {"drafted_proposal": response.content}
```

**This is OrbitHire's secret weapon.** Upwork doesn't have AI-powered matching or proposal drafting. Freelancers on OrbitHire can submit high-quality proposals in seconds instead of spending 30 minutes writing each one.

---

## 14. Phase 3: Email Notifications

### 📧 The Mailroom

The email service sends branded HTML emails for every important event. Think of it like a hotel concierge who sends you a note whenever something happens:

| Event | Recipient | Email Subject |
|---|---|---|
| Registration | New user | "Welcome to OrbitHire!" |
| New proposal | Client | "New proposal for [Job Title]" |
| Proposal accepted | Freelancer | "Your proposal was accepted!" |
| Escrow funded | Freelancer | "Escrow funded: $X,XXX" |
| Payment released | Freelancer | "Payment released: $X,XXX" |
| New message | Recipient | "New message from [Name]" |
| New review | Reviewee | "New review from [Name]" |

**How it works:**

```python
def send_email(to_email, subject, title, body, cta_text="", cta_url=""):
    smtp = _get_smtp_connection()
    if smtp is None:
        # No SMTP configured → log to console instead (development mode)
        logger.info(f"[EMAIL STUB] To: {to_email} | Subject: {subject}")
        return False

    # Build branded HTML email and send via SMTP
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = settings.SMTP_FROM_EMAIL
    msg["To"] = to_email
    msg.attach(MIMEText(html_content, "html"))
    smtp.sendmail(msg["From"], [to_email], msg.as_string())
```

**The graceful degradation pattern:** If SMTP is not configured (no `SMTP_HOST` in `.env`), the email service logs what it *would* have sent to the console instead of crashing. This means development works perfectly without any email setup.

---

## 15. Phase 3: Rate Limiting

### 🚦 The Traffic Police

Without rate limiting, a hacker could make 1 million requests per second and either:
- **Crash your server** (Denial of Service attack)
- **Brute-force passwords** (try millions of password combinations)
- **Spam registrations** (create thousands of fake accounts)

```python
# app/core/rate_limiter.py
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)  # Keyed by IP address

def setup_rate_limiting(app):
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

**Current limits:**
| Endpoint | Limit | Why |
|---|---|---|
| `POST /auth/register` | 5/minute | Prevent spam account creation |
| `POST /auth/login` | 10/minute | Prevent brute-force password attacks |

When the limit is exceeded, the user gets a `429 Too Many Requests` response.

---

## 16. Phase 3: Background Jobs

### 🌙 The Night Shift Worker

Some tasks don't need to happen during a user request — they need to happen on a schedule, like a night-shift cleaner who mops the floors after everyone goes home.

```python
# app/core/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def start_scheduler():
    # Check for escrows to auto-release every hour
    scheduler.add_job(check_escrow_releases, 'interval', hours=1)
    # Replenish free credits every day
    scheduler.add_job(replenish_monthly_credits, 'interval', days=1)
    scheduler.start()
```

**Job 1: Auto-Release Escrows** — Every hour, check if any escrow has passed its 7-day hold period. If so, automatically release the funds to the freelancer and mark the job as completed.

**Job 2: Monthly Credit Replenishment** — Every day, check if any user's last credit replenishment was 30+ days ago. If so, give them 5 free credits. This is the "freemium" model — free users get 5 credits/month to try the platform.

---

## 17. Phase 3: Admin Dashboard

### 🎛️ Mission Control

The admin panel lets platform operators monitor and manage everything:

```python
@router.get("/stats")
async def platform_stats(db, current_user):
    require_admin(current_user)  # Only SUPER_ADMIN or TENANT_ADMIN

    total_users = (await db.execute(select(func.count()).select_from(User))).scalar()
    total_jobs = (await db.execute(select(func.count()).select_from(JobPost))).scalar()
    total_escrow_value = (await db.execute(select(func.sum(Escrow.amount)))).scalar()
    open_disputes = (await db.execute(
        select(func.count()).select_from(Dispute).where(Dispute.status == DisputeStatus.OPEN)
    )).scalar()

    return {
        "total_users": total_users,
        "total_jobs": total_jobs,
        "total_escrow_value": total_escrow_value,
        "open_disputes": open_disputes,
    }
```

**Admin capabilities:**
- View platform-wide stats (users, jobs, revenue, disputes)
- Search and list all users with filters
- Ban/unban users (toggle `is_active`)
- View and resolve disputes

---

## 18. How Everything Connects

### The Complete Request Journey

Here's what happens when a Freelancer clicks **"Draft Proposal with AI"** on the frontend:

```
1. Frontend (React) sends:
   GET /api/v1/proposals/draft/job-456
   Headers: { Authorization: "Bearer eyJhbG..." }

2. FastAPI receives the request at proposals.py

3. get_current_user() runs FIRST (the security checkpoint):
   → Extracts token from Authorization header
   → Decodes JWT → gets user_id = "user-789"
   → Queries database → finds User object
   → Returns User(id="user-789", role="FREELANCER")

4. get_db() runs (opens a fresh database session)

5. The endpoint function runs:
   a. Checks: Is user a FREELANCER? ✅
   b. Checks: Does user have enough credits? ✅ (deducts 2 credits)
   c. Queries DB: Find JobPost where id = "job-456" ✅
   d. Queries DB: Find FreelancerProfile where user_id = "user-789" ✅
   e. Calls drafter_chain.invoke({
        "job_description": "Build a React dashboard...",
        "freelancer_profile": {"title": "Senior React Developer", ...}
      })
   f. LangGraph runs the generate_draft node
   g. Groq LLM generates a professional proposal

6. Endpoint returns:
   { "draft": "Dear Hiring Manager, I am excited to apply..." }

7. Frontend displays the AI-generated proposal to the Freelancer
```

### The Dependency Injection Chain

```
FastAPI Request arrives
    ├── get_db() → AsyncSession (fresh database connection)
    ├── get_current_user() → User object (authenticated user)
    │       ├── oauth2_scheme → extracts Bearer token from header
    │       ├── jwt.decode() → extracts user_id from token payload
    │       └── db.execute(select User) → fetches user from database
    └── Pydantic Schema → validates request body (rejects bad data)
```

---

## 19. Common Mistakes We Made (and Fixed)

These are real bugs we encountered while building this project. Learn from them!

| # | Bug | Error | Fix |
|---|---|---|---|
| 1 | Used `bcrypt` which broke with newer versions | `ValueError: password > 72 bytes` | Switched to `argon2` |
| 2 | Missing imports (`AsyncSession`, `select`) | `NameError` | Always check imports at the top |
| 3 | `return HTTPException(...)` instead of `raise` | Returns 200 OK with error object | Always `raise HTTPException(...)` |
| 4 | Letting frontend send `client_id` | Security vulnerability | Pull identity from `current_user.id` |
| 5 | Used `@app.on_event("startup")` | Deprecation warning | Use `lifespan` context manager |
| 6 | `EscrowStatus.PENDING` instead of `.PENDING_PAYMENT` | `AttributeError` | Check exact Enum member names |
| 7 | Copy-pasted role check into wrong endpoint | Every freelancer gets 403 | Think about WHO uses the endpoint |
| 8 | `updated_at: datetime` when DB allows NULL | Pydantic crash | Use `datetime \| None = None` |
| 9 | Freelancer jobs not loading | Silent failure | `getJobs()` was blocked by `if (!token)` check |
| 10 | White text on white background | Text invisible | CSS audit: replaced `text-white` with `text-[#202124]` |

---

## 20. API Cheat Sheet (Complete)

### Authentication (3 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/auth/register` | None | Create account (rate-limited: 5/min) |
| POST | `/auth/login` | None | Get JWT token (rate-limited: 10/min) |
| GET | `/auth/me` | JWT | Get current user info |

### Freelancers (4 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/freelancers/profile` | JWT (Freelancer) | Create profile |
| GET | `/freelancers/profile` | JWT (Freelancer) | Get own profile |
| PUT | `/freelancers/profile` | JWT (Freelancer) | Update profile |
| GET | `/freelancers/browse` | None | Search/filter freelancers |

### Clients (3 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/clients/company/create` | JWT (Client) | Create company profile |
| GET | `/clients/company` | JWT (Client) | Get company profile |
| PUT | `/clients/company` | JWT (Client) | Update company profile |

### Jobs (4 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/jobs/` | JWT (Client) | Post a new job |
| GET | `/jobs/` | None | Search/filter jobs (public) |
| GET | `/jobs/my-jobs` | JWT (Client) | Get own posted jobs |
| GET | `/jobs/{id}/match` | JWT (Client) | AI freelancer recommendations |

### Proposals (7 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/proposals/` | JWT (Freelancer) | Submit proposal (costs credits) |
| GET | `/proposals/my-proposals` | JWT (Freelancer) | View own proposals |
| GET | `/proposals/job/{id}` | JWT (Client) | View proposals for your job |
| PUT | `/proposals/{id}/status` | JWT (Client) | Accept/reject proposal |
| DELETE | `/proposals/{id}` | JWT (Freelancer) | Withdraw proposal |
| GET | `/proposals/draft/{job_id}` | JWT (Freelancer) | AI-draft a proposal |
| POST | `/proposals/{id}/export/docx` | JWT | Export as Word document |

### Escrow (6 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/escrow/create_order` | JWT (Client) | Create escrow order |
| POST | `/escrow/fund/{id}` | JWT (Client) | Fund escrow (move to HELD) |
| POST | `/escrow/release/{id}` | JWT (Client) | Release funds to freelancer |
| POST | `/escrow/dispute/{id}` | JWT | Raise a dispute |
| GET | `/escrow/status/{id}` | JWT | Check escrow status |
| POST | `/escrow/webhook/razorpay` | None | Razorpay payment webhook |

### Milestones (4 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/milestones/` | JWT (Client) | Create milestone |
| GET | `/milestones/job/{id}` | JWT | List milestones for job |
| PUT | `/milestones/{id}` | JWT | Update milestone |
| PUT | `/milestones/{id}/complete` | JWT (Freelancer) | Mark as complete |

### Credits (4 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| GET | `/credits/balance` | JWT | Check credit balance |
| GET | `/credits/history` | JWT | Transaction history |
| GET | `/credits/packs` | None | Available credit packs |
| POST | `/credits/purchase` | JWT | Buy a credit pack |

### Messages (4 endpoints + WebSocket)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/messages/conversations` | JWT (Client) | Start conversation |
| GET | `/messages/conversations` | JWT | List conversations |
| POST | `/messages/conversations/{id}/messages` | JWT | Send message |
| GET | `/messages/conversations/{id}/messages` | JWT | Get message history |
| WS | `/messages/ws/chat/{id}` | None | Real-time WebSocket |

### Reviews (3 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/reviews/` | JWT | Submit review (completed jobs only) |
| GET | `/reviews/user/{id}` | None | Get user's reviews (public) |
| GET | `/reviews/job/{id}` | None | Get job's reviews (public) |

### Notifications (2 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| GET | `/notifications/` | JWT | List notifications |
| PUT | `/notifications/{id}/read` | JWT | Mark as read |

### Uploads (4 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| POST | `/uploads/upload` | JWT | Upload a file |
| GET | `/uploads/files/{id}` | None | Download a file |
| GET | `/uploads/my-files` | JWT | List own files |
| DELETE | `/uploads/files/{id}` | JWT | Delete own file |

### Admin (4 endpoints)
| Method | Endpoint | Auth | What It Does |
|---|---|---|---|
| GET | `/admin/stats` | JWT (Admin) | Platform statistics |
| GET | `/admin/users` | JWT (Admin) | List/search users |
| PUT | `/admin/users/{id}/ban` | JWT (Admin) | Ban/unban user |
| PUT | `/admin/disputes/{id}/resolve` | JWT (Admin) | Resolve dispute |

**Total: 52 endpoints across 13 routers** — a full production API surface.

---

## 21. Going to Production

### 1. Switch the Database
```bash
# Development (current — file-based, good for one developer)
DATABASE_URL="sqlite+aiosqlite:///./freelance_saas.db"

# Production (server-based, handles millions of users)
DATABASE_URL="postgresql+asyncpg://user:password@db-server:5432/freelance_saas"
```
SQLite is a single file — great for development, terrible for production (no concurrent writes, no backups, no scaling). PostgreSQL handles millions of simultaneous users.

### 2. Secure Your Secrets
```bash
# .env file (NEVER commit this to GitHub!)
SECRET_KEY=a-64-character-random-string-generated-with-openssl
GROQ_API_KEY=gsk_abc123...
RAZORPAY_KEY_ID=rzp_live_...
RAZORPAY_KEY_SECRET=...
SMTP_HOST=smtp.gmail.com
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=app-specific-password
DATABASE_URL=postgresql+asyncpg://...
```

### 3. Add to `.gitignore`
```
.env
freelance_saas.db
uploads/
__pycache__/
.venv/
```

### 4. Deploy
- **Frontend**: Deploy to **Vercel** (free for React apps, auto-deploys from GitHub)
- **Backend**: Deploy to **Railway** or **Render** (support Python + PostgreSQL)
- **Database**: Use **Neon** (free PostgreSQL) or **Supabase** (free PostgreSQL + dashboard)

### 5. Production Checklist
```
□ Change SECRET_KEY to a random 64-character string
□ Set DATABASE_URL to PostgreSQL
□ Configure SMTP for real emails
□ Add Razorpay production keys
□ Set CORS to your actual domain (not localhost)
□ Turn off SQLAlchemy echo (echo=False)
□ Add HTTPS (automatic on Vercel/Railway)
□ Set up database backups
```

---

## 22. The Universal Backend Blueprint

No matter what language, framework, or product you're building — every backend in the world follows the same **7-step construction order**. Memorize this. This is how professionals build backends.

### The 7-Step Construction Order

```
Step 1: PLAN         → What does the product do? Who are the users? What data exists?
Step 2: FOUNDATION   → Config, Database connection, Entry point
Step 3: DATA LAYER   → Database models (tables) and relationships
Step 4: VALIDATION   → Pydantic/Zod schemas (what goes in, what comes out)
Step 5: SECURITY     → Authentication (who are you?) + Authorization (what can you do?)
Step 6: BUSINESS API → CRUD endpoints (Create, Read, Update, Delete)
Step 7: ADVANCED     → AI, Background jobs, Webhooks, File uploads, Email, Caching
```

**Why this order?** You cannot build Step 6 without Step 5 (how do you protect an endpoint if auth doesn't exist?). You cannot build Step 5 without Step 3 (how do you verify a user if the User table doesn't exist?). **Every step depends on the one before it.**

### The "New Feature" Recipe

After your backend is built, every new feature follows a **4-step mini-recipe**:

```
1. MODEL    → Does this feature need a new database table? Create it in models/
2. SCHEMA   → What data comes in? What goes out? Create schemas in schemas/
3. ENDPOINT → What URL does the frontend call? Create the route in api/v1/
4. WIRE     → Register the router in main.py with include_router()
```

That's it. Every feature. Every time. Forever. 🎯

---

## 23. The Developer Memory Framework

You've read 1,200+ lines. Here are the mental models and mnemonics to compress everything into your permanent memory.

### 🧠 Mnemonic #1: "FIVE DOSA" (The Folder Structure)

Every backend has 5 core folders:

```
F → Foundation  (core/)        → Config, DB, Security, Email, Rate-limiting
I → Items       (models/)      → Database tables (13 models)
V → Validators  (schemas/)     → Input/Output rules (7 schema files)
E → Endpoints   (api/)         → The URLs (13 router files, 52 endpoints)
+ DOSA = "Data Organized in Separated Areas"
```

### 🧠 Mnemonic #2: "VACDR" (The Endpoint Pattern)

Every API endpoint follows this order (like "VADER" from Star Wars):

```
V → Validate      (Pydantic checks the input)
A → Authenticate   (JWT proves who you are)
C → Check role     (Are you allowed to do this?)
D → Database       (Read or write data)
R → Return         (Send the response)
```

### 🧠 Mnemonic #3: "ACR" (Database Write)

```
A → db.add(object)       ← "I want to save this"
C → await db.commit()    ← "Do it now"
R → await db.refresh()   ← "Reload with auto-generated fields"
```

### 🧠 Mnemonic #4: "SEN" (Database Read)

```
S → select(Model).where(Model.field == value)   ← Build the query
E → await db.execute(query)                      ← Run the query
N → result.scalar_one_or_none()                  ← Get the result (or None)
```

---

### 🧠 The Golden Rules

#### Rule 1: "Never Trust the Frontend"
```
❌ BAD:  client_id = payload.client_id    (hacker can change this)
✅ GOOD: client_id = current_user.id      (from verified JWT token)
```

#### Rule 2: "Raise, Don't Return"
```
❌ BAD:  return HTTPException(status_code=404, detail="Not found")
✅ GOOD: raise HTTPException(status_code=404, detail="Not found")
```

#### Rule 3: "Hash, Never Store"
```
❌ BAD:  user.password = "mypassword123"
✅ GOOD: user.password_hash = pwd_context.hash("mypassword123")
```

#### Rule 4: "Schema Mirrors Model (But Smaller)"
```
Model (in database):     id, tenant_id, email, password_hash, role, created_at
Response Schema (to API): id, email, full_name, role, created_at
Input Schema (from API):  email, password, full_name, role
```

#### Rule 5: "Nullable = Optional"
```
Database:  mapped_column(DateTime, nullable=True)
Schema:    updated_at: datetime | None = None
```

---

### 🧠 The 60-Second Interview Recap

> I built an **AI-powered freelance marketplace backend** using **FastAPI** (Python).
>
> **Architecture:** Modular folder structure with separation between models (SQLAlchemy ORM), schemas (Pydantic validation), and API routes (FastAPI routers). 13 routers with 52 endpoints. Config loaded from `.env` via `pydantic-settings`.
>
> **Auth:** JWT-based authentication with **Argon2** password hashing. A `get_current_user` dependency extracts the user from the Bearer token on every protected route. Rate-limited with **slowapi** (5 registrations/min, 10 logins/min).
>
> **Security:** Role-based access control (Client, Freelancer, Admin). User identity always pulled from JWT, never from request body. All exceptions properly raised.
>
> **Payments:** Razorpay integration with a state-machine Escrow engine (`PENDING → HELD → RELEASED/DISPUTED`). 7-day hold window with 10% dual-sided platform fees. Background auto-release via APScheduler.
>
> **AI:** Two LangGraph workflows — a 3-node **Matchmaker** (extract skills → fetch candidates → rank) and a **Proposal Drafter** that generates cover letters. AI-generated DOCX/PPTX exports.
>
> **Real-time:** WebSocket-based chat with conversation management. Email notifications for all key events. In-app notification system.
>
> **Infrastructure:** Async SQLAlchemy with SQLite (dev) / PostgreSQL (prod). File upload system with type/size validation. Multi-tenant architecture. Admin dashboard with dispute resolution.

---

> **Congratulations!** 🎉
>
> You now understand every single file, every design decision, and every security pattern in this entire backend. You didn't just copy code — you understand WHY each piece exists and HOW they all connect together.
>
> You have the blueprint. You have the mnemonics. You have the decision tree. You can now build ANY backend from scratch, for any product, in any domain.
>
> **OrbitHire Backend Stats:**
> - 13 database models
> - 7 schema files
> - 13 API routers
> - 52 endpoints
> - 2 AI workflows
> - 2 background jobs
> - 1 WebSocket endpoint
> - 7 email templates
> - Rate limiting, escrow, credits, disputes, milestones, reviews, file uploads, admin panel
>
> **What's Next?** Deploy to production with PostgreSQL + Vercel and start onboarding real users! 🚀
