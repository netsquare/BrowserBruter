// encryption.js
const CryptoJS = require('crypto-js');

function encryptAndSubmit() {
  const formData = new FormData(document.getElementById('myForm'));

  // Encrypt the data
  const encryptedData = encrypt(formData);

  // Create a hidden input field to store the encrypted data
  const encryptedInput = document.createElement('input');
  encryptedInput.type = 'hidden';
  encryptedInput.name = 'encryptedData';
  encryptedInput.value = encryptedData;

  // Append the hidden input to the form
  document.getElementById('myForm').appendChild(encryptedInput);

  // Submit the form
  document.getElementById('myForm').submit();
}

// Encryption function using crypto-js
function encrypt(formData) {
  const algorithm = 'aes-256-cbc';
  const key = '4f5cfd0a0a5a4d0b64e065a561a5e5a'; // Replace with your secret key
  const ivHex = 'a2b1c0d9e8f7fe0dc1b2a3c4d5e6f7d'; // Replace with your initialization vector

  // Convert the IV from hex to a WordArray
  const iv = CryptoJS.enc.Hex.parse(ivHex);

  // Convert the form data to a JSON string
  const jsonData = JSON.stringify(Object.fromEntries(formData));

  // Encrypt the data
  const encrypted = CryptoJS.AES.encrypt(jsonData, key, { iv, mode: CryptoJS.mode.CBC });

  // Convert the encrypted data to a hex string
  return encrypted.ciphertext.toString(CryptoJS.enc.Hex);
}
