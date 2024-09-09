import os
import random
import string
from flask import Flask, render_template_string, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Global variable to store the captcha text
captcha_text_storage = {}

# Captcha generator function
def generate_captcha():
    # Generate a random 4-character captcha
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=4))

    # Create an image with white background
    image = Image.new('RGB', (200, 80), color='white')
    draw = ImageDraw.Draw(image)

    # Use a TrueType font for better control over the font size
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this to a valid path if necessary
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the position for each character to add spacing
    x_position = 20
    for char in captcha_text:
        y_position = (80 - font_size) // 2  # Center the character vertically
        draw.text((x_position, y_position), char, font=font, fill='black')
        x_position += font_size  # Move to the right for the next character with some spacing

    # Save the image with the captcha text as the file name
    image_path = os.path.join("static", "captcha.png")
    image.save(image_path)

    return captcha_text, image_path

# Home route with login form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # Generate a captcha for the initial GET request
        captcha_text, captcha_image = generate_captcha()
        captcha_text_storage['captcha_text'] = captcha_text  # Store captcha text in global variable
        return render_template_string(
            login_template,
            captcha_image=captcha_image
        )
    else:
        # Handle POST request (form submission)
        username = request.form.get('username')
        password = request.form.get('password')
        captcha_input = request.form.get('captcha_input')
        captcha_correct = captcha_text_storage.get('captcha_text')  # Retrieve captcha text from global variable

        if username == 'admin' and password == 'admin' and captcha_input == captcha_correct:
            return redirect(url_for('welcome'))
        else:
            # Generate a new captcha in case of invalid submission
            captcha_text, captcha_image = generate_captcha()
            captcha_text_storage['captcha_text'] = captcha_text  # Update captcha text in global variable
            return render_template_string(
                login_template,
                error="Invalid credentials" if username!= 'admin' or password!='admin' else "Invalid captcha",
                captcha_image=captcha_image
            )

# Welcome route
@app.route('/welcome')
def welcome():
    return "<h1>Welcome, Admin!</h1>"

# Login template with embedded HTML
login_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <label for="captcha_input">Captcha:</label><br>
        <img id="captcha_image" src="{{ captcha_image }}" alt="Captcha Image"><br>
        <input type="text" id="captcha_input" name="captcha_input"><br><br>
        <input type="submit" name="submit" value="Login">
    </form>
</body>
</html>
'''

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(host="0.0.0.0",debug=True)
