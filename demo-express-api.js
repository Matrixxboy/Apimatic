const express = require('express');
const app = express();
const port = 3000;

// ---------------------- MIDDLEWARES ----------------------

// Logs every request
const requestLogger = (req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.originalUrl}`);
  next();
};

// Simple auth check middleware
const checkAuth = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token || token !== "Bearer secret123") {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
};

// Middleware to validate userId param
function validateUserId(req, res, next) {
  const { id } = req.params;
  if (isNaN(parseInt(id))) {
    return res.status(400).json({ error: "User ID must be a number" });
  }
  next();
}

app.use(express.json()); // parse JSON bodies
app.use(requestLogger);  // global logger

// ---------------------- CONTROLLERS ----------------------

// GET user data
function getUserData(req, res) {
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
});

// ---------------------- START SERVER ----------------------
app.listen(port, () => {
  console.log(`🚀 Server is running at http://localhost:${port}`);
});
