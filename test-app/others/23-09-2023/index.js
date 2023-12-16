const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const csrf = require('csurf');
const { body, validationResult } = require('express-validator');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(csrf({ cookie: true }));

// Custom CSRF error handler
app.use((err, req, res, next) => {
  if (err.code !== 'EBADCSRFTOKEN') return next(err);
  res.status(403).send('CSRF Token Validation Failed');
});

// Custom validation error handler
const handleValidationErrors = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    const errorMessages = errors.array().map((error) => error.msg);
    return res.status(400).send(errorMessages);
  }
  next();
};

// Form page route
app.get('/', (req, res) => {
  const csrfToken = req.csrfToken();
  res.send(`
    <h1>Form Page</h1>
    <form action="/submit" method="POST">
      <input type="hidden" name="_csrf" value="${csrfToken}">
      
      <label for="data">Data:</label>
      <input type="text" name="data" placeholder="Enter data" required/><br/>

      <label for="yes">Yes:</label>
      <input type="radio" name="yesno" id="yes" value="yes" required/>
  
      <label for="no">No:</label>
      <input type="radio" name="yesno" id="no" value="no" required/>
      
      <label for="hobbies">Hobbies:</label>
      <input type="checkbox" name="hobbies" value="reading"/> Reading
      <input type="checkbox" name="hobbies" value="writing"/> Writing
      <input type="checkbox" name="hobbies" value="painting"/> Painting<br/>
      
      <label for="phone">Phone Number:</label>
      <input type="tel" name="phone" placeholder="Enter phone number" pattern="[0-9]{10}" required/><br/>
      
      <label for="calendar">Calendar:</label>
      <input type="date" name="calendar" required/><br/>
      
      <label for="time">Time:</label>
      <input type="time" name="time" required/><br/>
      
      <label for="color">Color:</label>
      <input type="color" name="color" required/><br/>
      
      <label for="select">Select:</label>
      <select name="select" required>
        <option value="">Select an option</option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </select><br/>
      
      <label for="textarea">Textarea:</label>
      <textarea name="textarea" placeholder="Enter text" required></textarea><br/>
      
      <button id="submit" type="submit">Submit</button>
    </form>
  `);
});

// Form validation rules
const validationRules = [
  body('data').trim().notEmpty().withMessage('Data field is required'),
  body('yesno').notEmpty().withMessage('Yes/No field is required'),
  body('hobbies').optional().isArray().withMessage('Hobbies must be an array'),
  body('phone').trim().matches(/^[0-9]{10}$/).withMessage('Phone number must be a 10-digit number'),
  body('calendar').notEmpty().withMessage('Calendar field is required'),
  body('time').notEmpty().withMessage('Time field is required'),
  body('color').notEmpty().withMessage('Color field is required'),
  body('select').notEmpty().withMessage('Select field is required'),
  body('textarea').trim().notEmpty().withMessage('Textarea field is required'),
];
// Form submission endpoint
app.post('/submit', validationRules, handleValidationErrors, (req, res) => {
  const { data, yesno, hobbies, phone, calendar, time, color, select, textarea } = req.body;

  // Process form data as needed

  res.send(`
    <h1>Received Data</h1>
    <p>Data: ${data}</p>
    <p>Yes/No: ${yesno}</p>
    <p>Hobbies: ${Array.isArray(hobbies) ? hobbies.join(', ') : hobbies}</p>
    <p>Phone Number: ${phone}</p>
    <p>Calendar: ${calendar}</p>
    <p>Time: ${time}</p>
    <p>Color: ${color}</p>
    <p>Select: ${select}</p>
    <p>Textarea: ${textarea}</p>
  `);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
