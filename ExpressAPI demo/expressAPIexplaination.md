# API Documentation

## Express API Endpoints

### `POST /api/users`
- **Endpoint:** `POST /api/users`
- **Source File:** `expressAPIdemo.js`
- **Logic Explanation:**
  - The endpoint creates a new user with the provided name and email. It first validates the request body for the presence of both 'name' and 'email'. If either is missing, it returns a 400 error. If the request is valid, it creates a new user object and returns it with a 201 status code.
- **Handlers:**
  - Handler 1:
```javascript
(req, res, next) => {
  const token = req.headers['authorization'];
  if (!token || token !== "Bearer secret123") {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
}
```
  - Handler 2:
```javascript
(req, res) => {
  const { name, email } = req.body; // request body
  if (!name || !email) {
    return res.status(400).json({ error: "Name and email are required" });
  }
  const newUser = { id: Date.now(), name, email, status: "active" };
  res.status(201).json(newUser);
}
```
- **Query Params:**
  _None_
- **Request Body:**
  Request body for creating a new user.
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "email"
  ]
}
```

### `DELETE /api/users/:id`
- **Endpoint:** `DELETE /api/users/:id`
- **Source File:** `expressAPIdemo.js`
- **Logic Explanation:**
  - The endpoint checks for authentication and validates the user ID. If the ID is valid, it returns a success message. If the ID is invalid or authentication fails, it returns an error.
- **Handlers:**
  - Handler 1:
```javascript
(req, res, next) => {
  const token = req.headers['authorization'];
  if (!token || token !== "Bearer secret123") {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
}
```
  - Handler 2:
```javascript
req, res, next) {
  const { id } = req.params;
  if (isNaN(parseInt(id))) {
    return res.status(400).json({ error: "User ID must be a number" });
  }
```
  - Handler 3:
```javascript
req, res) {
  const { id } = req.params;
  res.status(200).json({ message: `User ${id} deleted` });
}

// ---------------------- ROUTES ----------------------
app.get('/api/users/:id', checkAuth, validateUserId, getUserData);
app.post('/api/users', checkAuth, createUser);
app.put('/api/users/:id', checkAuth, validateUserId, updateUser);
app.delete('/api/users/:id', checkAuth, validateUserId, deleteUser);

// ---------------------- ERROR HANDLER ----------------------
app.use((err, req, res, next) => {
  console.error("Unhandled error:", err);
  res.status(500).json({ error: "Internal Server Error" });
}
```
- **Query Params:**
  _None_
- **Request Body:**
  _None_

### `GET /api/users/:id`
- **Endpoint:** `GET /api/users/:id`
- **Source File:** `expressAPIdemo.js`
- **Logic Explanation:**
  - The endpoint retrieves a user's data by their unique ID. It first validates the 'id' path parameter, then queries the database for the user record. If the user is not found, it returns a 400 error. Otherwise, it returns the user's data. The endpoint also supports query parameters to include the user's posts. If the 'includePosts' query parameter is set to 'true', the user's posts are included in the response.
- **Handlers:**
  - Handler 1:
```javascript
(req, res, next) => {
  const token = req.headers['authorization'];
  if (!token || token !== "Bearer secret123") {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
}
```
  - Handler 2:
```javascript
req, res, next) {
  const { id } = req.params;
  if (isNaN(parseInt(id))) {
    return res.status(400).json({ error: "User ID must be a number" });
  }
```
  - Handler 3:
```javascript
req, res) {
  const userId = req.params.id;
  const includePosts = req.query.includePosts === "true"; // query param
  const user = { id: userId, name: `User ${userId}`, status: 'active' };

  if (includePosts) {
    user.posts = [
      { id: 1, title: "Hello World" },
      { id: 2, title: "Express.js is great!" }
    ];
  }

  res.status(200).json(user);
}

// CREATE a new user
const createUser = (req, res) => {
  const { name, email } = req.body; // request body
  if (!name || !email) {
    return res.status(400).json({ error: "Name and email are required" });
  }
  const newUser = { id: Date.now(), name, email, status: "active" };
  res.status(201).json(newUser);
};

// UPDATE user
const updateUser = async (req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;
  res.status(200).json({ message: `User ${id} updated`, name, email });
};

// DELETE user
function deleteUser(req, res) {
  const { id } = req.params;
  res.status(200).json({ message: `User ${id} deleted` });
}

// ---------------------- ROUTES ----------------------
app.get('/api/users/:id', checkAuth, validateUserId, getUserData);
app.post('/api/users', checkAuth, createUser);
app.put('/api/users/:id', checkAuth, validateUserId, updateUser);
app.delete('/api/users/:id', checkAuth, validateUserId, deleteUser);

// ---------------------- ERROR HANDLER ----------------------
app.use((err, req, res, next) => {
  console.error("Unhandled error:", err);
  res.status(500).json({ error: "Internal Server Error" });
}
```
- **Query Params:**

| Name | Description | Type |
|------|-------------|------|
| `includePosts` | Specifies whether to include the user's posts in the response. | `boolean` |
- **Request Body:**
  Request body for creating a new user.
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "email"
  ]
}
```

### `PUT /api/users/:id`
- **Endpoint:** `PUT /api/users/:id`
- **Source File:** `expressAPIdemo.js`
- **Logic Explanation:**
  - The endpoint handles user profile updates. It first checks for a valid authorization token. If the token is invalid, it returns a 401 Unauthorized response. Then, it validates the 'id' path parameter to ensure it's a number. If the 'id' is invalid, it returns a 400 Bad Request response. If the 'id' is valid, it updates the user's profile with the provided 'name' and 'email' in the request body and returns a 200 OK response.
- **Handlers:**
  - Handler 1:
```javascript
(req, res, next) => {
  const token = req.headers['authorization'];
  if (!token || token !== "Bearer secret123") {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
}
```
  - Handler 2:
```javascript
req, res, next) {
  const { id } = req.params;
  if (isNaN(parseInt(id))) {
    return res.status(400).json({ error: "User ID must be a number" });
  }
```
  - Handler 3:
```javascript
(req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;
  res.status(200).json({ message: `User ${id} updated`, name, email });
}
```
- **Query Params:**
  _None_
- **Request Body:**
  Request body for updating a user's profile.
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "email"
  ]
}
```
