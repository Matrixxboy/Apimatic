from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
import uvicorn

# ==============================
# Config
# ==============================
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Fake user DB
fake_user = {
    "username": "admin",
    "password": "admin123"  # <- in real app, store hashed password
}

# ==============================
# App & Middleware
# ==============================
app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log each request/response."""
    print(f"➡️ Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"⬅️ Response status: {response.status_code}")
    return response


# ==============================
# Auth Helpers
# ==============================
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username != fake_user["username"]:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# ==============================
# Routes
# ==============================
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login and get JWT token."""
    if form_data.username == fake_user["username"] and form_data.password == fake_user["password"]:
        access_token = create_access_token(
            data={"sub": fake_user["username"]},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get("/public")
def public():
    """Open route - no auth needed."""
    return {"msg": "This is a public endpoint 🚀"}


@app.get("/protected")
def protected(username: str = Depends(verify_token)):
    """Protected route - needs valid token."""
    return {"msg": f"Welcome {username}, this is a protected endpoint 🔐"}


# ==============================
# Run
# ==============================
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)
