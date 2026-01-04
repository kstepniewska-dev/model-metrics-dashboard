from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # TODO: Implement actual user authentication
        # For now, validate basic inputs
        
        if not email or not password:
            return render_template(
                'login.html', 
                error='Email and password are required.',
                year=datetime.now().year
            )
        
        # TODO: Query database and verify credentials
        # if authenticate_user(email, password):
        #     session['user_id'] = user.id
        #     session['email'] = user.email
        #     return redirect(url_for('index'))
        
        # Placeholder error
        flash('Invalid email or password.', 'error')
        return render_template('login.html',
                               error='Invalid email or password.',
                               year=datetime.now().year)
    
    return render_template('login.html', year=datetime.now().year)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
        # Validation
        if not email or not password or not password_confirm:
            return render_template(
                'register.html',
                error='All fields are required.',
                year=datetime.now().year
            )
        
        if password != password_confirm:
            return render_template(
                'register.html',
                error='Passwords do not match.',
                year=datetime.now().year
            )
        
        if len(password) < 8:
            return render_template(
                'register.html',
                error='Password must be at least 8 characters.',
                year=datetime.now().year
            )
        
        # TODO: Check if email already exists
        # TODO: Hash password and save to database
        # if user_exists(email):
        #     return render_template('register.html', error='Email already registered.', year=datetime.now().year)
        # create_user(email, hash_password(password))
        
        return render_template(
            'register.html',
            success='Account created! You can now log in.',
            year=datetime.now().year
        )
    
    return render_template('register.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
