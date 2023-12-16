const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const base64url = require('base64url');
const csurf = require('csurf');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(csurf({ cookie: true }));

// Redirect user to login page
app.get('/', (req,res) => { res.redirect('/login'); });

app.get('/login', (req, res) => {
  // Check if the user already has a success cookie set to true
  if (req.cookies.success === 'true') {
    res.redirect('/welcome');
  } else {
    const csrfToken = req.csrfToken();
    res.send(`
      <h1>Login Page</h1>
      <form action="/login" method="POST">
        <input type="hidden" name="_csrf" value="${csrfToken}"/>
        <label for="username">Username:</label>
        <input type="text" name="username" placeholder="Enter your username" required/><br/>

        <label for="password">Password:</label>
        <input type="password" name="password" placeholder="Enter your password" required/><br/>

        <button name="submit" type="submit">Login</button>
      </form>
    `);
  }
});


// Login page route
/*app.get('/login', (req, res) => {
  // Check if the user already has a success cookie set to true
  if (req.cookies.success === 'true') {
    res.redirect('/welcome');
  } else {
    const csrfToken = req.csrfToken();
    res.send(`
      <h1>Login Page</h1>
      <form action="/login" method="POST">
        <input type="hidden" name="_csrf" value="${csrfToken}"/>
        <label for="username">Username:</label>
        <input type="text" name="username" placeholder="Enter your username" required/><br/>

        <label for="password">Password:</label>
        <input type="password" name="password" placeholder="Enter your password" required/><br/>

        <button name="submit" type="submit">Login</button>
      </form>
    `);
  }
});*/

// Login submission endpoint
app.post('/login', (req, res) => {
  const { username, password, _csrf } = req.body;

  // Check CSRF token validity
  if (!req.csrfToken() || _csrf !== req.csrfToken()) {
    res.status(403).send('Invalid CSRF token');
    return;
  }

  // Check if username and password are correct
  if (username === 'admin' && password === 'admin') {
    // Set the success cookie to true
    const encodedValue = base64url.encode('true');
    res.cookie('success', encodedValue);
    res.redirect('/welcome');
  } else {
    res.send('Invalid username or password');
  }
});

// Welcome page route
app.get('/welcome', (req, res) => {
  // Check if the user has the success cookie set to true
  if (req.cookies.success === 'true') {
    res.send('<h1>Welcome Page</h1>');
  } else {
    res.redirect('/login');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
