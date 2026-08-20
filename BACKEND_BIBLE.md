# 🧠 The Complete Backend Bible: Freelance AI SaaS Platform

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
10. [Phase 3: AI Engine with LangGraph](#10-phase-3-ai-engine-with-langgraph)
11. [How Everything Connects (The Full Flow)](#11-how-everything-connects)
12. [Common Mistakes We Made (and Fixed)](#12-common-mistakes-we-made)
13. [API Cheat Sheet](#13-api-cheat-sheet)
14. [Going to Production](#14-going-to-production)
15. [The Universal Backend Blueprint](#15-the-universal-backend-blueprint-how-any-backend-is-built)
16. [The Developer Memory Framework](#16-the-developer-memory-framework-how-to-remember-this-for-life)

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
    S10["🤖 10. AI Engine\n(LangGraph Workflows)"]
    S11["🔗 11. Full Flow\n(How It All Connects)"]
    S12["🐛 12. Common Mistakes\n(Learn From Our Bugs)"]
    S13["📋 13. API Cheat Sheet\n(Quick Reference)"]
    S14["🚀 14. Going to Production\n(Deploy Checklist)"]
    S15["📐 15. Universal Blueprint\n(Build ANY Backend)"]
    S16["🧠 16. Memory Framework\n(Remember It Forever)"]

    S1 -->|"Understand the concept"| S2
    S2 -->|"Know your tools"| S3
    S3 -->|"Navigate the code"| S4
    S4 -->|"Foundation ready"| S5
    S5 -->|"Tables exist"| S6
    S6 -->|"Validation ready"| S7
    S7 -->|"Auth ready"| S8
    S8 -->|"Basic API done"| S9
    S8 -->|"Basic API done"| S10
    S9 -->|"Advanced features done"| S11
    S10 -->|"Advanced features done"| S11
    S11 -->|"Understand the whole system"| S12
    S12 -->|"Learn from mistakes"| S13
    S13 -->|"Quick reference ready"| S14
    S14 -->|"Know how to deploy"| S15
    S15 -->|"Generalize the knowledge"| S16

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
    style S11 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S12 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S13 fill:#4a1e5a,stroke:#c06aff,color:#fff
    style S14 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
    style S15 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
    style S16 fill:#5a1e3a,stroke:#ff4a6a,color:#fff
```

> **🎨 Color Key:**
> - 🔵 **Blue** = Conceptual Foundation (Sections 1–3) — Understand before you code
> - 🟢 **Green** = Phase 1: Core Backend (Sections 4–8) — The bread and butter
> - 🟠 **Orange** = Phase 2–3: Advanced Features (Sections 9–10) — Escrow + AI
> - 🟣 **Purple** = Connecting the Dots (Sections 11–13) — See the big picture
> - 🔴 **Red** = Level Up (Sections 14–16) — Production, blueprints, memory tricks

---

## 1. What Even Is a Backend?

Imagine a restaurant:
- **Frontend** = The dining room. It's what the customer (user) sees — the menu, the tables, the decor. In our case, this is the Next.js website.
- **Backend** = The kitchen. The customer never sees it, but it's where all the real work happens — cooking the food, storing ingredients, checking if the customer has paid.
- **Database** = The fridge/pantry. It stores all the raw ingredients (data) that the kitchen (backend) needs.
- **API** = The waiter. The waiter takes orders from the dining room (frontend), walks them to the kitchen (backend), and brings the food (data) back.

**Our backend does 4 things:**
1. **Stores data** (users, jobs, proposals, payments) in a database.
2. **Protects data** (only you can see your own stuff via login/passwords).
3. **Processes payments** (Escrow: holds money safely until work is done).
4. **Runs AI** (LangGraph: automatically matches freelancers to jobs and drafts proposals).

---

## 2. The Tech Stack

| Tool | What It Does | Real-World Analogy |
|------|-------------|-------------------|
| **Python** | The programming language we write everything in | The language the chef speaks |
| **FastAPI** | The web framework that creates our API endpoints | The restaurant's ordering system |
| **SQLAlchemy** | Talks to the database using Python (instead of raw SQL) | A translator between the chef and the pantry |
| **SQLite** | The actual database (a single file on disk) | The fridge that stores everything |
| **Pydantic** | Validates incoming data (rejects garbage input) | The quality inspector at the kitchen door |
| **JWT (JSON Web Tokens)** | Handles login sessions (proves who you are) | Your restaurant loyalty card |
| **bcrypt** | Hashes passwords (makes them unreadable) | A padlock on your locker |
| **LangChain + LangGraph** | Orchestrates AI workflows with LLMs | An AI sous-chef that helps with recipes |
| **Groq** | The LLM provider (runs the AI model) | The brain of the AI sous-chef |
| **Uvicorn** | The server that actually runs our app | The power supply that keeps the kitchen running |

### The `requirements.txt` File
```
fastapi          ← The web framework
langchain        ← AI orchestration library
langgraph        ← Multi-step AI workflow engine
langchain-groq   ← Connects LangChain to Groq's LLMs
uvicorn          ← ASGI server (runs FastAPI)
pydantic         ← Data validation
sqlalchemy       ← Database ORM (Object-Relational Mapper)
aiosqlite        ← Async SQLite driver
pydantic-settings← Loads config from .env files
pyjwt            ← Creates and verifies JWT tokens
passlib[bcrypt]  ← Password hashing
python-multipart ← Handles file uploads in forms
python-docx      ← Generates Word documents
python-pptx      ← Generates PowerPoint presentations
reportlab        ← Generates PDF documents
langsmith        ← LangChain observability/tracing
```

---

## 3. Project Folder Structure

```
free/
├── .env                          ← Secret keys (NEVER commit this to GitHub)
├── requirements.txt              ← List of Python packages to install
├── freelance_saas.db             ← The SQLite database file (auto-created)
│
├── app/                          ← ALL backend code lives here
│   ├── __init__.py               ← Makes "app" a Python package
│   ├── main.py                   ← 🚀 THE ENTRY POINT (starts the server)
│   │
│   ├── core/                     ← ⚙️ Configuration, Database, Security
│   │   ├── config.py             ← App settings (loaded from .env)
│   │   ├── database.py           ← Database connection and session management
│   │   └── security.py           ← JWT token creation and user authentication
│   │
│   ├── models/                   ← 📦 DATABASE TABLES (what gets stored)
│   │   ├── __init__.py           ← Registers all models so SQLAlchemy sees them
│   │   ├── tenant.py             ← Multi-tenant organization model
│   │   ├── user.py               ← User accounts + Freelancer profiles
│   │   ├── job.py                ← Job postings by clients
│   │   ├── proposal.py           ← Freelancer proposals/bids
│   │   ├── credit.py             ← Credit wallet and transactions
│   │   └── escrow.py             ← Payment escrow vault
│   │
│   ├── schemas/                  ← 🛡️ DATA VALIDATORS (what the API accepts/returns)
│   │   ├── user.py               ← User input/output validation
│   │   ├── job.py                ← Job input/output validation
│   │   ├── proposal.py           ← Proposal input/output validation
│   │   ├── credit.py             ← Credit wallet validation
│   │   └── escrow.py             ← Escrow input/output validation
│   │
│   ├── api/v1/                   ← 🌐 API ENDPOINTS (the URLs the frontend calls)
│   │   ├── auth.py               ← POST /register, POST /login
│   │   ├── freelancers.py        ← POST /profile
│   │   ├── jobs.py               ← POST /, GET /{job_id}/match
│   │   ├── proposals.py          ← POST /, GET /draft/{job_id}
│   │   ├── escrow.py             ← POST /create_order, POST /webhook/razorpay
│   │   └── credits.py            ← GET /balance
│   │
│   └── ai/                       ← 🤖 AI ENGINE (LangGraph workflows)
│       ├── state.py              ← Defines what data the AI remembers
│       ├── matchmaker.py         ← AI that ranks freelancers for a job
│       └── drafter.py            ← AI that writes proposals for freelancers
```

### Why This Structure?

Think of it like a hospital:
- **`core/`** = The hospital's infrastructure (power, water, security cameras)
- **`models/`** = The patient records system (what data gets stored)
- **`schemas/`** = The intake forms (what information we collect from visitors)
- **`api/`** = The reception desk (where visitors make requests)
- **`ai/`** = The specialist doctors (advanced AI-powered services)

Each folder has ONE job. This is called **Separation of Concerns** — the #1 rule of professional software engineering.

---

## 4. Phase 0: The Foundation Files

Before we write a single API endpoint, we need to set up three foundational systems: Configuration, Database, and the Entry Point.

---

### 4A. Configuration — `app/core/config.py`

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Freelance AI Saas"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "super_secret_jwt_key_change_me_in_prod"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    FREE_MONTHLY_CREDITS: int = 10  # Free credits each freelancer gets per month

    DATABASE_URL: str = "sqlite+aiosqlite:///./freelance_saas.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
```

**What is this?** A single source of truth for every setting in the entire app.

**Why do we need it?**
- Instead of typing `"sqlite+aiosqlite:///./freelance_saas.db"` in 15 different files, we type `settings.DATABASE_URL` once.
- The `env_file=".env"` part means: "If there's a `.env` file, load secrets from there." This way, your passwords never appear in your code.
- The `extra="ignore"` part means: "If the `.env` file has extra variables I don't know about, just ignore them."

**Key Settings:**
| Setting | What It Controls |
|---------|-----------------|
| `SECRET_KEY` | The encryption key for JWT tokens. Change this in production! |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | How long a login session lasts (8 days) |
| `DATABASE_URL` | Where the database file lives |
| `FREE_MONTHLY_CREDITS` | How many free credits each freelancer gets (10) |

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

**What is this?** The plumbing that connects our Python code to the SQLite database.

**Breaking it down for a fresher:**

1. **Engine** = Think of it as a phone line to the database. `echo=True` means it prints every SQL query (helpful for debugging).

2. **Session** = A conversation with the database. Every time the frontend makes an API call, we open a fresh conversation (`session`), do our work, and close it.

3. **Base** = The parent class for ALL our database tables. Every model (User, Job, Proposal, etc.) inherits from `Base`, which tells SQLAlchemy: "Hey, this Python class should become a real database table."

4. **`get_db()`** = A "dependency" function. FastAPI automatically calls this function before each request and gives the endpoint a fresh `session`. The `yield` keyword means: "Give the session to the endpoint, wait for it to finish, then close the session."

**Why `async`?** Normal database operations block your server — while one request is waiting for the database, no other request can run. `async` means multiple requests can run simultaneously, making your server much faster.

---

### 4C. The Entry Point — `app/main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import Base, engine
# Import all routers
from app.api.v1.auth import router as auth_router
from app.api.v1.freelancers import router as freelance_router
# ... (all other routers)
import app.models  # Forces SQLAlchemy to discover ALL models

app = FastAPI(title=settings.PROJECT_NAME)

# CORS: Allow the frontend (Next.js) to talk to our backend
app.add_middleware(CORSMiddleware, allow_origins=["*"], ...)

# On startup: Create all database tables automatically
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Wire up every router with a URL prefix
app.include_router(auth_router,      prefix="/api/v1/auth",      tags=["Authentication"])
app.include_router(freelance_router,  prefix="/api/v1/freelancers", tags=["Freelancers"])
# ... (all other routers)
```

**What is this?** The control center. It:
1. Creates the FastAPI application.
2. Enables CORS (so the Next.js frontend can talk to the backend).
3. Auto-creates all database tables on startup.
4. Connects every API router to a URL prefix.

**What is CORS?** By default, a website at `localhost:3000` (Next.js) cannot call an API at `localhost:8000` (FastAPI) because browsers block "cross-origin" requests for security. CORS middleware says: "It's okay, let them through."

**What is a Router?** Instead of writing all 12 endpoints in `main.py` (which would be a mess), we split them into separate files. Each file has its own `APIRouter()`. Then `main.py` connects them all together with `include_router()`.

**Why `import app.models`?** SQLAlchemy only knows about a model if Python has actually executed the file. By importing `app.models` (which imports every model file in `__init__.py`), we guarantee every table is registered before `create_all` runs.

---

## 5. Phase 1: Database Models

A **model** is a Python class that represents a database table. Each attribute of the class becomes a column in the table.

---

### 5A. The Tenant Model — `app/models/tenant.py`

```python
class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
```

**What is a Tenant?** This app is "multi-tenant" — meaning multiple companies can use the same backend. Think of it like an apartment building: each apartment (tenant) is separate, but they all share the same building (server).

**Key concepts:**
- `primary_key=True` → This column uniquely identifies every row. Like a passport number.
- `default=lambda: str(uuid.uuid4())` → Auto-generates a random unique ID for every new tenant.
- `nullable=False` → This field MUST have a value. You can't leave it empty.
- `unique=True` → No two tenants can have the same slug.
- `index=True` → Creates a search index (makes lookups faster, like an index in a textbook).

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

    id: Mapped[str] = mapped_column(String(36), primary_key=True, ...)
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"))
    email: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(Enum(UserRole), default=UserRole.FREELANCER)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    tenant: Mapped["Tenant"] = relationship("Tenant", back_populates="users")
    freelancer_profile: Mapped["FreelancerProfile"] = relationship(...)
    credit_wallet: Mapped["CreditWallet"] = relationship(...)
```

**New concepts:**

**`ForeignKey("tenants.id")`** → This is a link to another table. It says: "Every user MUST belong to a tenant." It's like saying every employee must work at a company.

**`relationship()`** → This creates a navigation link. Instead of writing a SQL query to find a user's profile, you can just write `user.freelancer_profile` and SQLAlchemy automatically fetches it.

**`back_populates`** → This makes the relationship two-way. If `User` has `freelancer_profile`, then `FreelancerProfile` has `user`. They point to each other.

**`uselist=False`** → "This relationship returns ONE object, not a list." A user has ONE profile, not many.

**`cascade="all, delete-orphan"`** → "If I delete the user, automatically delete their profile too." No orphan data left behind.

**Why `password_hash` and not `password`?** We NEVER store raw passwords. We run them through `bcrypt` (a one-way encryption algorithm) that turns `"mypassword123"` into `"$2b$12$LJ3..."`. Even if a hacker steals the database, they can't reverse the hash to get the original password.

---

### 5C. Other Models (Same Patterns)

**FreelancerProfile** → Separate table because not every user is a freelancer. Uses `JSON` columns for `skills` (lists) and `portfolio` (dictionaries).

**JobPost** → Uses `Enum(JobStatus)` for a state machine: `OPEN → IN_PROGRESS → COMPLETED / CANCELLED`.

**Proposal** → Links `freelancer_id` to `job_id` with `cover_letter` and `bid_amount`.

**CreditWallet** → One wallet per user. `CreditTransaction` logs every credit spent/purchased (audit trail).

**Escrow** → Payment vault with state machine: `PENDING_PAYMENT → HELD → RELEASED / DISPUTED → REFUNDED`.

---

## 6. Phase 1: Pydantic Schemas

### Models vs Schemas: What's the Difference?

| | Model | Schema |
|--|-------|--------|
| **Lives in** | `app/models/` | `app/schemas/` |
| **Purpose** | Defines database tables | Validates API input/output |
| **Talks to** | The database | The frontend |
| **Analogy** | The fridge layout | The menu |

**Why do we need both?**

Imagine this: the `User` model has a `password_hash` column. If we returned the model directly to the frontend, the user would see their hashed password in the API response! Schemas let us control exactly what data goes in and comes out.

### Types of Schemas

**Response Schema** (what we send back):
```python
class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Read from DB objects
    id: str
    email: str
    full_name: str
    role: UserRole
    # Notice: NO password_hash field! We never expose this.
```

**Input Schema** (what we receive):
```python
class JobCreate(BaseModel):
    title: str
    description: str
    category: str
    budget: float
    required_skills: list[str]
    # Notice: NO id, NO client_id, NO tenant_id, NO status, NO created_at
    # These are all set AUTOMATICALLY by the server.
```

**Why are input schemas so small?** Because we never trust the frontend! If we let the frontend send `client_id`, a hacker could change it to someone else's ID. Instead, we pull `client_id` from the JWT token (which is cryptographically signed and cannot be tampered with).

### The `from_attributes=True` Setting

```python
model_config = ConfigDict(from_attributes=True)
```

This tells Pydantic: "I'm going to give you a SQLAlchemy database object (not a dictionary). Please read its attributes to build the response." Without this, Pydantic would crash when you try to return a database row.

### Optional Fields

```python
release_date: datetime | None = None
updated_at: datetime | None = None
```

The `| None = None` syntax means: "This field can either be a `datetime` or `None`, and it defaults to `None`." We use this for fields that might not have a value yet (e.g., `release_date` is empty until payment is confirmed).

---

## 7. Phase 1: Authentication

### 7A. Password Security — `app/core/security.py`

```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashing: "password123" → "$2b$12$LJ3m9..."
hashed = pwd_context.hash("password123")

# Verifying: Does "password123" match the hash?
is_valid = pwd_context.verify("password123", hashed)  # True
```

**How bcrypt works (simplified):**
1. Take the password: `"password123"`
2. Add random "salt": `"password123" + "xK9mQ2"` (different every time)
3. Run through a one-way math function 12 times
4. Output: `"$2b$12$LJ3m9..."` (impossible to reverse)

Even if two users have the same password, their hashes will be different (because the salt is random).

---

### 7B. JWT Tokens — How Login Works

```python
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

This token contains:
- **Header**: Algorithm used (HS256)
- **Payload**: `{"sub": "user-123", "role": "FREELANCER", "exp": 1692...}`
- **Signature**: A cryptographic proof that the server created this token

The frontend stores this token and sends it with every request. The backend decodes it to know who is making the request.

**Why not just use sessions/cookies?** JWTs are stateless — the server doesn't need to store anything. This makes scaling to millions of users much easier.

---

### 7C. The Auth Guard — `get_current_user()`

```python
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

**The flow:**
1. Frontend sends: `Authorization: Bearer eyJhbG...`
2. `oauth2_scheme` extracts the token from the header.
3. `jwt.decode()` verifies the signature and extracts the user ID.
4. We query the database to make sure the user still exists.
5. We return the full `User` object to the endpoint.

**This function is a "dependency."** Any endpoint that needs to know who is making the request just adds `current_user: User = Depends(get_current_user)` to its parameters. FastAPI automatically calls `get_current_user()` before the endpoint runs.

---

## 8. Phase 1: API Endpoints

### The Pattern Every Endpoint Follows

```
1. VALIDATE INPUT     → Pydantic schema checks the data
2. AUTHENTICATE       → get_current_user() verifies the JWT
3. AUTHORIZE          → Check if the user has the right ROLE
4. DATABASE OPERATION → Read/Write to the database
5. RETURN RESPONSE    → Send data back to the frontend
```

---

### 8A. Registration — `POST /api/v1/auth/register`

```python
@router.post("/register")
async def register(payload: UserRegister, db: AsyncSession = Depends(get_db)):
    hashed_pass = pwd_context.hash(payload.password)     # Step 1: Hash password
    new_user = User(                                      # Step 2: Create DB object
        full_name=payload.full_name,
        email=payload.email,
        password_hash=hashed_pass,
        role=payload.role,
        tenant_id=payload.tenant_id,
    )
    db.add(new_user)          # Step 3: Add to session
    await db.commit()         # Step 4: Save to database
    await db.refresh(new_user) # Step 5: Reload with auto-generated fields (id, created_at)
    return new_user
```

- **`db.add()`** → "Hey database, I want to save this object."
- **`db.commit()`** → "Okay, NOW actually write it to disk."
- **`db.refresh()`** → "Reload this object from the database so I have the auto-generated `id` and `created_at`."

---

### 8B. Login — `POST /api/v1/auth/login`

```python
@router.post("/login")
async def login(payload: UserLogin, db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.email == payload.email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if user is None:
        return {"error": "User not found"}

    is_valid = pwd_context.verify(payload.password, user.password_hash)
    if not is_valid:
        return {"error": "Incorrect password"}

    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
    return {"access_token": access_token, "token_type": "Bearer"}
```

1. Find the user by email.
2. Compare the submitted password against the stored hash.
3. If valid, generate a JWT token and return it.

---

### 8C. Creating a Freelancer Profile — `POST /api/v1/freelancers/profile`

```python
@router.post("/profile")
async def create_profile(payload: ProfileCreate, db, current_user):
    if current_user.role != UserRole.FREELANCER:
        raise HTTPException(status_code=403, detail="Only freelancers can create profiles")
    profile = FreelancerProfile(
        user_id=current_user.id,  # Pulled from JWT, NOT from the frontend!
        title=payload.title,
        bio=payload.bio,
        skills=payload.skills,
        hourly_rate=payload.hourly_rate
    )
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile
```

**Key Security Pattern:** `user_id = current_user.id` — we NEVER let the frontend tell us who they are. We pull it from the verified JWT token. This prevents impersonation attacks.

**HTTP Status Codes:**
| Code | Meaning | When We Use It |
|------|---------|----------------|
| 200 | OK | Everything worked |
| 400 | Bad Request | Invalid data sent |
| 401 | Unauthorized | Not logged in / bad token |
| 403 | Forbidden | Logged in but wrong role |
| 404 | Not Found | Resource doesn't exist |

---

## 9. Phase 2: Escrow Engine

### What Is Escrow?

Imagine you're buying a car from a stranger on the internet:
- You don't want to pay first (they might take the money and disappear).
- They don't want to ship first (you might receive the car and never pay).
- **Solution:** A trusted middleman (escrow) holds the money. Once you confirm the car arrived safely, the middleman releases the money to the seller.

Our platform IS that middleman.

### The Escrow State Machine

```
Client clicks "Hire" → PENDING_PAYMENT
                              ↓
Razorpay confirms payment → HELD (7-day timer starts)
                              ↓
     ┌────────────────────────┴────────────────────────┐
     ↓                                                 ↓
Day 3: Dispute raised?                        Day 7: No dispute?
     ↓                                                 ↓
  DISPUTED                                         RELEASED
     ↓                                         (Freelancer gets paid)
50/50 split (REFUNDED)
```

### The 10% Fee Calculation

```python
total_amount = payload.amount * 1.10  # Client pays 10% extra
```

For a $1,000 project:
- Client pays: $1,100 (project + 10% fee)
- Platform keeps: $200 (10% from client + 10% from freelancer)
- Freelancer receives: $900 (project minus 10% fee)

### Creating an Escrow Order — `POST /api/v1/escrow/create_order`

```python
@router.post("/create_order")
async def create_escrow_order(payload, db, current_user):
    # 1. Find the job
    job = await db.execute(select(JobPost).where(JobPost.id == payload.job_id))
    job = job.scalar_one_or_none()

    # 2. Validate: Does the job exist?
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    # 3. Validate: Is this the actual client who posted the job?
    if job.client_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the client")

    # 4. Validate: Is the job still open?
    if job.status != JobStatus.OPEN:
        raise HTTPException(status_code=400, detail="Job is not open")

    # 5. Calculate total with platform fee
    total_amount = payload.amount * 1.10

    # 6. Create the escrow vault
    escrow = Escrow(
        job_id=payload.job_id,
        client_id=current_user.id,
        freelancer_id=payload.freelancer_id,
        amount=total_amount,
    )
    db.add(escrow)
    await db.commit()
    return escrow
```

### The Razorpay Webhook — `POST /api/v1/escrow/webhook/razorpay`

```python
@router.post("/webhook/razorpay")
async def razorpay_webhook(request: Request, db):
    data = await request.json()
    event = data.get("event")
    payload = data.get("payload")

    if event == "payment.captured":
        payment = payload.get("payment")
        escrow = await db.execute(select(Escrow).where(Escrow.id == payment.get("order_id")))
        escrow = escrow.scalar_one_or_none()
        escrow.status = EscrowStatus.HELD
        escrow.release_date = datetime.utcnow() + timedelta(days=7)
        await db.commit()
        return escrow
```

**What is a Webhook?** Unlike normal API calls where the FRONTEND calls US, a webhook is when a THIRD-PARTY SERVICE calls us. When Razorpay processes a payment, it sends a POST request to our `/webhook/razorpay` endpoint to say: "Payment confirmed."

**Why no `get_current_user`?** Webhooks don't come from logged-in users. They come from Razorpay's servers. In production, you'd verify Razorpay's signature instead.

**Why `Request` instead of a Pydantic schema?** Payment gateway payloads are complex and unpredictable. Using `Request` lets us parse the raw JSON ourselves, which is the industry standard for webhooks.

---

## 10. Phase 3: AI Engine with LangGraph

### What is LangGraph?

LangGraph is a framework for building multi-step AI workflows. Instead of making one giant prompt, you break the AI task into small, focused steps (called **nodes**), and LangGraph runs them in sequence.

Think of it like an assembly line:
```
Raw Materials → Cut → Paint → Assemble → Quality Check → Final Product
```

Each station (node) does one job, then passes the result to the next station.

---

### 10A. The State — `app/ai/state.py`

```python
from typing import TypedDict

class MatchmakerState(TypedDict):
    job_description: str
    required_skills: list[str]
    candidate_freelancers: list[dict]
    final_recommendations: list[dict]

class DraftState(TypedDict):
    freelancer_profile: dict
    job_description: str
    drafted_proposal: str
```

**What is the State?** It's the AI's memory. As data flows through each node, the state accumulates results. Node 1 fills in `required_skills`, Node 2 fills in `candidate_freelancers`, Node 3 fills in `final_recommendations`.

**Why `TypedDict`?** It tells Python (and your IDE) exactly what keys the state dictionary should have and what types they are. This catches bugs before they happen.

---

### 10B. The Matchmaker — `app/ai/matchmaker.py`

This AI reads a job description and ranks the best freelancers.

**Node 1: Extract Skills** — The LLM reads the job description and extracts required skills as a comma-separated list.

**Node 2: Fetch Freelancers** — Queries the database for candidate freelancers. *(Right now this uses hardcoded fake data for testing. In the real version, it will query the actual database to find real freelancers.)*

**Node 3: Rank Candidates** — The LLM reads all candidate bios and ranks them by best fit for the job.

**Compiling the Graph:**
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

**The flow:** `START → extract_skills → fetch_freelancers → rank_candidates → END`

---

### 10C. The Proposal Drafter — `app/ai/drafter.py`

This AI reads a freelancer's profile and a job description, then writes a professional proposal.

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

This graph only has ONE node (because drafting is a single-step task), but we still use LangGraph for consistency and future extensibility.

---

## 11. How Everything Connects

### The Complete Request Journey

Here's what happens when a Freelancer clicks "Draft Proposal with AI" on the frontend:

```
1. Frontend (Next.js) sends:
   GET /api/v1/proposals/draft/job-456
   Headers: { Authorization: "Bearer eyJhbG..." }

2. FastAPI receives the request at proposals.py

3. get_current_user() runs FIRST:
   → Extracts token from header
   → Decodes JWT → gets user_id = "user-789"
   → Queries database → finds User object
   → Returns User(id="user-789", role="FREELANCER")

4. get_db() runs:
   → Opens a fresh database session

5. The endpoint function runs:
   a. Checks: Is user a FREELANCER? ✅
   b. Queries DB: Find JobPost where id = "job-456" ✅
   c. Queries DB: Find FreelancerProfile where user_id = "user-789" ✅
   d. Calls drafter_chain.invoke({
        "job_description": "Build a React dashboard...",
        "freelancer_profile": "I'm a senior React developer..."
      })
   e. LangGraph runs the generate_draft node
   f. Groq LLM generates a professional proposal

6. Endpoint returns:
   { "draft": "Dear Hiring Manager, I am excited to apply..." }

7. Frontend displays the AI-generated proposal to the Freelancer
```

### The Dependency Injection Chain

```
FastAPI Request
    ├── get_db() → AsyncSession (database connection)
    ├── get_current_user() → User object (authenticated user)
    │       ├── oauth2_scheme → extracts Bearer token
    │       ├── jwt.decode() → extracts user_id
    │       └── db.execute(select User) → fetches user from DB
    └── Pydantic Schema → validates request body
```

---

## 12. Common Mistakes We Made (and Fixed)

These are real bugs we encountered while building this project. Learn from them!

| # | Bug | Error | Fix |
|---|-----|-------|-----|
| 1 | Missing imports (`AsyncSession`, `select`) | `NameError` | Always check imports at the top of every file |
| 2 | `return HTTPException(...)` instead of `raise` | Returns 200 OK with error object | Always `raise HTTPException(...)` |
| 3 | Letting frontend send `client_id` | Security vulnerability | Pull user identity from `current_user.id` |
| 4 | `EscrowStatus.PENDING` instead of `.PENDING_PAYMENT` | `AttributeError` | Check the exact Enum member name |
| 5 | Saved to `ranked` but read from `best_ids` | `NameError` | Use consistent variable names |
| 6 | Copy-pasted `job.client_id != current_user.id` into a Freelancer endpoint | Every freelancer gets 403 | Think about WHO uses the endpoint |
| 7 | `updated_at: datetime` when DB is `nullable=True` | Pydantic validation error | Use `datetime | None = None` |
| 8 | Inheriting `EscrowStatus` from SQLAlchemy `Enum` instead of `enum.Enum` | Class definition crash | Use `import enum` and inherit from `enum.Enum` |

---

## 13. API Cheat Sheet

### Authentication
| Method | Endpoint | Auth | Role | What It Does |
|--------|----------|------|------|-------------|
| POST | `/api/v1/auth/register` | None | Any | Create a new account |
| POST | `/api/v1/auth/login` | None | Any | Get a JWT token |

### Freelancers
| Method | Endpoint | Auth | Role | What It Does |
|--------|----------|------|------|-------------|
| POST | `/api/v1/freelancers/profile` | JWT | Freelancer | Create your profile |

### Jobs
| Method | Endpoint | Auth | Role | What It Does |
|--------|----------|------|------|-------------|
| POST | `/api/v1/jobs/` | JWT | Client | Post a new job |
| GET | `/api/v1/jobs/{job_id}/match` | JWT | Client | AI freelancer recommendations |

### Proposals
| Method | Endpoint | Auth | Role | What It Does |
|--------|----------|------|------|-------------|
| POST | `/api/v1/proposals/` | JWT | Freelancer | Submit a proposal |
| GET | `/api/v1/proposals/draft/{job_id}` | JWT | Freelancer | AI-drafted proposal |

### Escrow
| Method | Endpoint | Auth | Role | What It Does |
|--------|----------|------|------|-------------|
| POST | `/api/v1/escrow/create_order` | JWT | Client | Lock money in escrow |
| POST | `/api/v1/escrow/webhook/razorpay` | None | Razorpay | Confirm payment |

### Credits
| Method | Endpoint | Auth | Role | What It Does |
|--------|----------|------|------|-------------|
| GET | `/api/v1/credits/balance` | JWT | Any | Check credit balance |

---

## 14. Going to Production

Right now, this backend runs locally with SQLite. To go to production, here's what changes:

### 1. Switch the Database
```
# Development (current)
DATABASE_URL = "sqlite+aiosqlite:///./freelance_saas.db"

# Production
DATABASE_URL = "postgresql+asyncpg://user:password@db-server:5432/freelance_saas"
```
SQLite is a single file — great for development, terrible for production (no concurrent writes). PostgreSQL handles millions of simultaneous users.

### 2. Use Alembic for Migrations
Right now, `Base.metadata.create_all` creates tables from scratch. In production, you use **Alembic** to track changes to your database schema over time (like Git for your database).

### 3. Secure Your Secrets
```bash
# .env file (NEVER commit this to GitHub)
SECRET_KEY=a-very-long-random-string-here
GROQ_API_KEY=gsk_abc123...
DATABASE_URL=postgresql+asyncpg://...
```

### 4. Add Rate Limiting
Without rate limiting, a hacker could make 1 million requests per second and crash your server. Add middleware like `slowapi` to limit requests per IP.

### 5. Deploy with Docker
```dockerfile
FROM python:3.12-slim
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 6. Use a Reverse Proxy (Nginx)
Nginx sits in front of Uvicorn and handles SSL certificates (HTTPS), load balancing, and static file serving.

### 7. Fix Login Error Handling
Right now, the login endpoint returns `{"error": "User not found"}` with a 200 status code. In production:
```python
raise HTTPException(status_code=401, detail="Invalid credentials")
```

---

## 15. The Universal Backend Blueprint (How ANY Backend Is Built)

No matter what language, framework, or product you're building — every backend in the world follows the same 7-step construction order. Memorize this. Tattoo it on your brain. This is how professionals build backends.

### The 7-Step Construction Order

```
Step 1: PLAN         → What does the product do? Who are the users? What data exists?
Step 2: FOUNDATION   → Config, Database connection, Entry point
Step 3: DATA LAYER   → Database models (tables) and relationships
Step 4: VALIDATION   → Pydantic/Zod schemas (what goes in, what comes out)
Step 5: SECURITY     → Authentication (who are you?) + Authorization (what can you do?)
Step 6: BUSINESS API → CRUD endpoints (Create, Read, Update, Delete)
Step 7: ADVANCED     → AI, Background jobs, Webhooks, File uploads, Caching
```

### Why This Order?

You cannot build Step 6 without Step 5 (how do you protect an endpoint if auth doesn't exist?).
You cannot build Step 5 without Step 3 (how do you verify a user if the User table doesn't exist?).
You cannot build Step 3 without Step 2 (how do you create a table if there's no database connection?).

**Every step depends on the one before it.** If you try to skip ahead, you will waste hours debugging missing dependencies.

### How We Applied This Blueprint to Our Project

| Step | What We Built | Files Created |
|------|--------------|---------------|
| **1. Plan** | Drew the architecture diagram, identified 4 user roles, mapped out the Escrow flow, designed the credit economy | `master_architecture_blueprint.md` |
| **2. Foundation** | Created settings, database engine, session factory, main.py entry point | `config.py`, `database.py`, `main.py` |
| **3. Data Layer** | Built 6 database models with relationships and enums | `tenant.py`, `user.py`, `job.py`, `proposal.py`, `credit.py`, `escrow.py` |
| **4. Validation** | Created input/output schemas for every model | `schemas/user.py`, `schemas/job.py`, etc. |
| **5. Security** | Built JWT token creation, password hashing, and the `get_current_user` guard | `security.py` |
| **6. Business API** | Built all CRUD endpoints with role-based access control | `auth.py`, `freelancers.py`, `jobs.py`, `proposals.py`, `escrow.py`, `credits.py` |
| **7. Advanced** | Integrated LangGraph AI for matchmaking and proposal drafting, built Razorpay webhooks | `state.py`, `matchmaker.py`, `drafter.py` |

### The Universal Backend Checklist (Use This for EVERY Project)

Before you write a single line of code for any new project, answer these questions:

```
□ WHO are the users? (roles: admin, client, freelancer, etc.)
□ WHAT data do they create? (jobs, posts, orders, messages, etc.)
□ HOW do they authenticate? (JWT, OAuth, session cookies?)
□ WHAT are the relationships? (one-to-one, one-to-many, many-to-many?)
□ WHAT business rules exist? (only clients can post jobs, only freelancers can bid, etc.)
□ WHAT are the state machines? (order: pending → paid → shipped → delivered)
□ WHERE does money flow? (payments, refunds, fees, escrow?)
□ WHAT third-party services are involved? (Razorpay, Stripe, Google OAuth, SendGrid?)
```

Once you have these answers, the code practically writes itself.

---

### The "New Feature" Recipe

After your backend is built, every new feature you add follows a 4-step mini-recipe:

```
1. MODEL   → Does this feature need a new database table? Create it in models/
2. SCHEMA  → What data comes in? What goes out? Create schemas in schemas/
3. ENDPOINT→ What URL does the frontend call? Create the route in api/v1/
4. WIRE    → Register the router in main.py with include_router()
```

That's it. Every feature. Every time. Forever.

---

## 16. The Developer Memory Framework (How to Remember This for Life)

You've read 900+ lines. Here are the mental models, mnemonics, and patterns to compress everything into your permanent memory.

---

### 🧠 Mnemonic #1: "FIVE DOSA" (The File Structure)

Every backend has 5 core folders. Remember them with **FIVE DOSA**:

```
F → Foundation  (core/)        → Config, DB, Security
I → Items       (models/)      → Database tables
V → Validators  (schemas/)     → Input/Output rules
E → Endpoints   (api/)         → The URLs
+ DOSA = "Data Organized in Separated Areas"
```

When someone says "build me a backend," your brain should instantly picture these 5 folders.

---

### 🧠 Mnemonic #2: "VACDR" (The Endpoint Pattern)

Every single API endpoint in the history of software follows this order. Remember **VACDR** (like "VADER" from Star Wars):

```
V → Validate     (Pydantic checks the input)
A → Authenticate  (JWT proves who you are)
C → Check role    (Are you allowed to do this?)
D → Database      (Read or write data)
R → Return        (Send the response)
```

If you're debugging an endpoint and it's not working, walk through VACDR step by step. The bug is always in one of these 5 steps.

---

### 🧠 Mnemonic #3: "ACR" (The Database Operation)

Every time you save something to the database, it's always 3 lines:

```
A → db.add(object)       ← "I want to save this"
C → await db.commit()    ← "Do it now"
R → await db.refresh()   ← "Reload with auto-generated fields"
```

**ACR. Add, Commit, Refresh.** You will write these 3 lines hundreds of times in your career.

---

### 🧠 Mnemonic #4: "SEN" (The Database Read)

Every time you read from the database, it's always 3 lines:

```
S → select(Model).where(Model.field == value)   ← Build the query
E → await db.execute(query)                      ← Run the query  
N → result.scalar_one_or_none()                  ← Get the result (or None)
```

**SEN. Select, Execute, None-check.** Every database read in every endpoint.

---

### 🧠 The Golden Rules (Burn These Into Your Brain)

These are the rules that, if violated, will cause security breaches, data corruption, or production outages:

#### Rule 1: "Never Trust the Frontend"
```
❌ BAD:  client_id = payload.client_id    (hacker can change this)
✅ GOOD: client_id = current_user.id      (from verified JWT token)
```
**Why:** The frontend is controlled by the user. The user could be a hacker. Always pull identity from the server-side JWT token.

#### Rule 2: "Raise, Don't Return"
```
❌ BAD:  return HTTPException(status_code=404, detail="Not found")
✅ GOOD: raise HTTPException(status_code=404, detail="Not found")
```
**Why:** `return` sends a 200 OK response containing the exception as data. `raise` actually triggers the error with the correct status code.

#### Rule 3: "Hash, Never Store"
```
❌ BAD:  user.password = "mypassword123"
✅ GOOD: user.password_hash = bcrypt.hash("mypassword123")
```
**Why:** If your database is ever breached, raw passwords are instantly compromised. Hashes are irreversible.

#### Rule 4: "Import Before You Use"
```
❌ BAD:  Using AsyncSession, select, JobPost without importing them
✅ GOOD: Checking every name in your function has a corresponding import at the top
```
**Why:** Python throws `NameError` at runtime. It won't warn you until the code actually executes.

#### Rule 5: "Schema Mirrors Model (But Smaller)"
```
Model (in database):     id, tenant_id, email, password_hash, role, created_at
Response Schema (to API): id, email, full_name, role, created_at
Input Schema (from API):  email, password, full_name, role
```
**Why:** The model stores EVERYTHING. The response schema hides sensitive fields. The input schema only accepts what the user should control.

#### Rule 6: "Nullable = Optional"
```
Database:  mapped_column(DateTime, nullable=True)
Schema:    updated_at: datetime | None = None
```
**Why:** If the database allows `NULL`, the schema MUST allow `None`. Otherwise Pydantic will crash when it reads a null value.

---

### 🧠 The "Build Any Backend" Decision Tree

When you're starting a brand new project and feel overwhelmed, follow this decision tree:

```
START: "I need to build a backend"
  │
  ├── Do users need to log in?
  │     YES → Build JWT Auth (security.py + auth.py)
  │     NO  → Skip auth, use API keys
  │
  ├── What data exists?
  │     → For EACH data type (user, post, order, etc.):
  │         1. Create a model in models/
  │         2. Create a schema in schemas/
  │         3. Create CRUD endpoints in api/
  │
  ├── Do different users have different permissions?
  │     YES → Add role-based checks in every endpoint
  │     NO  → Skip authorization
  │
  ├── Does money flow through the system?
  │     YES → Build an Escrow/Payment state machine
  │     NO  → Skip payment logic
  │
  ├── Does the app need AI?
  │     YES → Build LangGraph workflows in ai/
  │     NO  → Skip AI
  │
  └── Wire everything into main.py → DONE
```

---

### 🧠 The Mental Model: "Layers of a Cake"

Think of the backend as a 4-layer cake. Each layer ONLY talks to the layer directly above or below it:

```
┌─────────────────────────────────────────┐
│          LAYER 4: API ENDPOINTS          │  ← Talks to the frontend
│    (auth.py, jobs.py, proposals.py)      │
├─────────────────────────────────────────┤
│          LAYER 3: BUSINESS LOGIC         │  ← Rules, calculations, AI
│    (escrow fees, role checks, LangGraph) │
├─────────────────────────────────────────┤
│          LAYER 2: DATA ACCESS            │  ← Reads/writes the database
│    (models, schemas, db.execute)         │
├─────────────────────────────────────────┤
│          LAYER 1: FOUNDATION             │  ← Infrastructure
│    (config, database, security)          │
└─────────────────────────────────────────┘
```

**Rule:** Layer 4 should NEVER directly access the database config. Layer 1 should NEVER know about job postings. Each layer has its own job.

---

### 🧠 The 60-Second Recap (Read This Before Every Interview)

> I built an **AI-powered freelance marketplace backend** using **FastAPI** (Python).
>
> **Architecture:** Modular folder structure with separation between models (SQLAlchemy ORM), schemas (Pydantic validation), and API routes (FastAPI routers). Config loaded from `.env` via `pydantic-settings`.
>
> **Auth:** JWT-based authentication with `bcrypt` password hashing. A `get_current_user` dependency extracts the user from the Bearer token on every protected route.
>
> **Security:** Role-based access control (Client vs Freelancer). User identity always pulled from JWT, never from request body. All exceptions properly raised (not returned).
>
> **Payments:** Razorpay integration with a state-machine Escrow engine (`PENDING → HELD → RELEASED/DISPUTED`). 7-day hold window with 10% dual-sided platform fees.
>
> **AI:** Two LangGraph workflows — a 3-node **Matchmaker** (extract skills → fetch candidates → rank by fit) and a single-node **Proposal Drafter** that generates cover letters from freelancer profiles.
>
> **Database:** Async SQLAlchemy with SQLite (dev) / PostgreSQL (prod). Models use `mapped_column` with `Mapped[]` type hints. Relationships with cascade deletes.

---

> **Congratulations!** 🎉
>
> You now understand every single file, every design decision, and every security pattern in this entire backend. You didn't just copy code — you understand WHY each piece exists and HOW they all connect together.
>
> You have the blueprint. You have the mnemonics. You have the decision tree. You can now build ANY backend from scratch, for any product, in any domain.
>
> **What's Next?** Phase 4: Building the Next.js Frontend that talks to this API.
