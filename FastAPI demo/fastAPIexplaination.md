# API Documentation

## Fastapi API Endpoints

### `POST /login`
- **Endpoint:** `POST /login`
- **Source File:** `fastapiAPIdemo.py`
- **Logic Explanation:**
  - The endpoint authenticates a user's login credentials. It first checks if the provided username and password match the fake user's credentials. If they match, it generates an access token with the user's username and returns it along with the token type. If the credentials are incorrect, it raises a 401 HTTP exception.
- **Handlers:**
  - Handler 1:
```python
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login and get JWT token."""
    if form_data.username == fake_user["username"] and form_data.password == fake_user["password"]:
        access_token = create_access_token(
            data={"sub": fake_user["username"]},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")
```
- **Query Params:**
  _None_
- **Request Body:**
  The request body contains the user's login credentials.

### `GET /protected`
- **Endpoint:** `GET /protected`
- **Source File:** `fastapiAPIdemo.py`
- **Logic Explanation:**
  - The endpoint returns a welcome message for a user with a valid token. It first verifies the token using the 'verify_token' dependency, then returns a JSON response with the user's username and a message.
- **Handlers:**
  - Handler 1:
```python
def protected(username: str = Depends(verify_token)):
    """Protected route - needs valid token."""
    return {"msg": f"Welcome {username}, this is a protected endpoint 🔐"}
```
- **Query Params:**
  _None_
- **Request Body:**
  _None_

### `GET /public`
- **Endpoint:** `GET /public`
- **Source File:** `fastapiAPIdemo.py`
- **Logic Explanation:**
  - The public endpoint returns a simple JSON response with a message indicating that it is a public endpoint.
- **Handlers:**
  - Handler 1:
```python
def public():
    """Open route - no auth needed."""
    return {"msg": "This is a public endpoint 🚀"}
```
- **Query Params:**
  _None_
- **Request Body:**
  _None_
