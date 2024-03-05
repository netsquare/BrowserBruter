const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto-js');

const app = express();
const PORT = 3000;

// Use middleware to parse request bodies
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (e.g., HTML, CSS, client-side JS)
app.use(express.static('public'));

// Define routes
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/submit', (req, res) => {
  // Decrypt the data
  const decryptedData = decrypt(req.body.encryptedData);

  // Render the submitted data on submitted.html
  res.send(`<h1>Submitted Data</h1><pre>${JSON.stringify(decryptedData, null, 2)}</pre>`);
});

// Decrypt function using crypto-js
function decrypt(encryptedData) {
  const algorithm = 'aes-256-cbc';
  const key = '4f5cfd0a0a5a4d0b64e065a561a5e5a'; // Example secret key (32 bytes)
  const ivHex = 'a2b1c0d9e8f7fe0dc1b2a3c4d5e6f7d'; // Example IV (16 bytes)

  try {
    // Convert the IV from hex to a WordArray
    const iv = crypto.enc.Hex.parse(ivHex);

    // Convert the encrypted data from hex to a WordArray
    const ciphertext = crypto.enc.Hex.parse(encryptedData);

    // Create a decryption configuration
    const config = { iv, mode: crypto.mode.CBC, padding: crypto.pad.Pkcs7 };

    // Decrypt the data
    const bytes = crypto.AES.decrypt({ ciphertext }, crypto.enc.Utf8.parse(key), config);

    // Convert the decrypted data to a string
    const decryptedData = bytes.toString(crypto.enc.Utf8);

    // Parse the decrypted JSON data
    return JSON.parse(decryptedData);
  } catch (error) {
    console.error('Decryption error:', error.message);
    return null; // Handle decryption errors as needed
  }
}

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
