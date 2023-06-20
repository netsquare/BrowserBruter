const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));

// Login page route
app.get('/', (req, res) => {
  res.send(`
    <h1>Login Page</h1>
    <form action="/login" method="POST">
      <input type="text" name="username" placeholder="Username" required/><br/>
      <input type="password" name="password" placeholder="Password" required/><br/>
      <button type="submit">Login</button>
    </form>
  `);
});

// Login endpoint
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'admin' && password === 'admin') {
    res.redirect('/form');
  } else {
    res.send('Invalid username or password');
  }
});

// Form page route
app.get('/form', (req, res) => {
  res.send(`
    <h1>Form Page</h1>
    <form action="/submit" method="POST">
      <input type="text" name="data" placeholder="Enter data" required/><br/>
      <button type="submit">Submit</button>
    </form>
  `);
});

// Form submission endpoint
app.post('/submit', (req, res) => {
  const { data } = req.body;
  res.send(`Received data: ${data}`);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
