from flask import Flask, request
from captcha.image import ImageCaptcha
import random
import string
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Generate a random string for the CAPTCHA
def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Generate a CAPTCHA image and save it to a directory
def generate_captcha_image(text, image_dir):
    image = ImageCaptcha()
    image_path = os.path.join(image_dir, f'{text}.png')
    image.write(text, image_path)
    return image_path

@app.route('/', methods=['GET', 'POST'])
def index():
    image_dir = 'captcha_images'  # Directory to store CAPTCHA images

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    if request.method == 'POST':
        # Validate the CAPTCHA
        captcha_text = request.form['captcha']
        if captcha_text == request.cookies.get('captcha'):
            return "CAPTCHA Passed!"
        else:
            return "CAPTCHA Failed!"

    # Generate a new CAPTCHA for each request
    captcha_text = generate_captcha_text()
    captcha_image_path = generate_captcha_image(captcha_text, image_dir)

    # Set the CAPTCHA text as a cookie
    response = app.make_response('')
    response.set_cookie('captcha', captcha_text)

    # Return the HTML form with the CAPTCHA image path
    return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>CAPTCHA Form</title>
        </head>
        <body>
            <h1>CAPTCHA Form</h1>
            <form method="post">
                <label for="captcha">Enter the CAPTCHA:</label><br>
                <img src="{captcha_image_path}" /><br>
                <input type="text" id="captcha" name="captcha" required><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

