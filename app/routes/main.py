from flask import Blueprint, render_template, session, redirect, url_for
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template(
        "main/index.html", 
        year=datetime.now().year)

@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template(
        "main/dashboard.html",
        user_role=session.get('user_role'),
        year=datetime.now().year)