from flask import Flask, request, session, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def enter_mobile():
    if request.method == 'POST':
        mobile_number = request.form['mobile_number']
        # Generate a random OTP (for demonstration purposes)
        otp = '1234'
        # Store the OTP in session (for demonstration purposes)
        session['otp'] = otp
        return redirect(url_for('verify_otp'))
    
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Enter Mobile Number</title>
        </head>
        <body>
            <h1>Enter Mobile Number</h1>
            <form method="post">
                <label for="mobile_number">Enter your mobile number:</label><br>
                <input type="text" id="mobile_number" name="mobile_number" required><br>
                <input type="submit" value="Get OTP">
            </form>
        </body>
        </html>
    '''

@app.route('/verify', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        stored_otp = session.get('otp')
        if entered_otp == stored_otp:
            return "OTP Verified!"
        else:
            return "OTP Verification Failed!"
    
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Verify OTP</title>
        </head>
        <body>
            <h1>Verify OTP</h1>
            <form method="post">
                <label for="otp">Enter the OTP you received:</label><br>
                <input type="text" id="otp" name="otp" required><br>
                <input type="submit" value="Verify OTP">
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

