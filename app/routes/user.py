from flask import Blueprint, render_template, session, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from datetime import datetime
from app.services.uploads_service import create_upload, get_upload_by_id, get_user_uploads, soft_delete_upload
from app.services.admin_service import get_user, soft_delete_user
import os

user = Blueprint('user', __name__)

# ===== USER PROFILE =====
@user.route('/user/profile')
def user_profile():
    """Display current user profile."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    current_user = get_user(session['user_id'])
    return render_template(
        'user/user_profile.html',
        user=current_user,
        year=datetime.now().year
    )

@user.route('/user/delete', methods=['POST'])
def delete_account():
    """Soft delete current user account (and their uploads)."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    soft_delete_user(user_id)
    session.clear()
    return redirect(url_for('main.index'))

# ===== USER UPLOADS =====
@user.route('/user/uploads')
def user_uploads():
    """Display user's uploads."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    uploads = get_user_uploads(session['user_id'])
    
    return render_template(
        'user/user_uploads.html',
        uploads=uploads,
        year=datetime.now().year
    )

def allowed_file(filename):
    """Check if file has allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@user.route('/user/upload', methods=['POST'])
def upload_file():
    """Handle file upload for current user."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if 'file' not in request.files:
        return redirect(url_for('user.user_uploads'))
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('user.user_uploads'))
    
    if file and allowed_file(file.filename):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        original_filename = secure_filename(file.filename)
        filename = f"{timestamp}_{original_filename}"
        
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        create_upload(session['user_id'], original_filename, filepath)
    
    return redirect(url_for('user.user_uploads'))

@user.route('/user/upload/delete/<int:upload_id>', methods=['POST'])
def delete_upload(upload_id):
    """Soft delete an upload (user can only delete own)."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    upload = get_upload_by_id(upload_id)
    
    if upload and upload.user_id == session['user_id']:
        soft_delete_upload(upload_id)
    
    return redirect(url_for('user.user_uploads'))