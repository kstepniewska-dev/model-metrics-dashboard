from flask import Blueprint, render_template, request
from datetime import datetime
from app.services.auth_service import create_user
from app.models.user import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
    #Validation
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
                error='Password must be at least 8 characters long.',
                year=datetime.now().year
            )
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template(
                'register.html', 
                error='Email already registered.', 
                year=datetime.now().year
                )

        create_user(email, password)
        return render_template(
            'register.html', 
            success='Registration successful!', 
            year=datetime.now().year
            )
            
    return render_template('register.html', year=datetime.now().year)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not email or not password:
            return render_template(
                'login.html',
                error='Email and password are required.',
                year=datetime.now().year
            )
        
        # Here you would typically add code to verify the user's credentials and log them in
        
        return render_template(
            'login.html',
            success='Login successful!',
            year=datetime.now().year
        )
    
    return render_template('login.html', year=datetime.now().year)