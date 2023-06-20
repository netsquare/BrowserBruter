const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));

// Form page route
app.get('/', (req, res) => {
  res.send(`
    <h1>Form Page</h1>
    <form action="/submit" method="POST">
      <label for="data">Data:</label>
      <input type="text" name="data" id="data" placeholder="Enter data" required/><br/>

      <label for="yesno">Yes/No:</label>
      <input type="radio" name="yesno" value="yes" id="yes" required/> Yes
      <input type="radio" name="yesno" value="no" id="no" required/> No<br/>

      <label for="hobbies">Hobbies:</label>
      <input type="checkbox" name="hobbies" id="reading" value="reading"/> Reading
      <input type="checkbox" name="hobbies" id="writing" value="writing"/> Writing
      <input type="checkbox" name="hobbies" id="painting" value="painting"/> Painting<br/>

      <label for="phone">Phone Number:</label>
      <input type="tel" name="phone" id="phone" placeholder="Enter phone number" required/><br/>

      <button id="submit" type="submit">Submit</button>
    </form>
  `);
});

// Form submission endpoint
app.post('/submit', (req, res) => {
  const { data, yesno, hobbies, phone } = req.body;
  res.send(`
    <h1>Received Data</h1>
    <p>Data: ${data}</p>
    <p>Yes/No: ${yesno}</p>
    <p>Hobbies: ${Array.isArray(hobbies) ? hobbies.join(', ') : hobbies}</p>
    <p>Phone Number: ${phone}</p>
  `);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
