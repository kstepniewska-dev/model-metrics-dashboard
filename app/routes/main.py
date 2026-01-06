from flask import Blueprint, render_template, session, redirect, url_for
from datetime import datetime
from app.services.uploads_service import get_user_uploads

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html", year=datetime.now().year)

@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_uploads = get_user_uploads(session.get('user_id'))
    
    return render_template(
        "dashboard.html",
        user_role=session.get('user_role'),
        uploads=user_uploads,
        year=datetime.now().year)