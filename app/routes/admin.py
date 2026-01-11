from flask import Blueprint, render_template, request, redirect, session, url_for
from datetime import datetime
from app.services.admin_service import get_user, get_all_users, soft_delete_user, soft_delete_uploads_by_user_id
from app.services.uploads_service import get_all_uploads, soft_delete_upload
from app import db

admin = Blueprint('admin', __name__)

@admin.route('/admin/all_profiles')
def all_profiles():
    """Display all user profiles to the admin."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    current_user = get_user(session['user_id'])
    if current_user.role != 'admin':
        return redirect(url_for('main.dashboard'))
    
    users = get_all_users()
    return render_template(
        'admin/all_profiles.html', 
        users=users, 
        current_user=current_user,
        datetime=datetime.now)

@admin.route('/admin/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Soft delete a user profile."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    current_user = get_user(session['user_id'])
    if current_user.role != 'admin':
        return redirect(url_for('main.dashboard'))
    
    user_to_delete = get_user(user_id)
    if user_to_delete and user_to_delete.role != 'admin':
        soft_delete_user(user_id)
        soft_delete_uploads_by_user_id(user_id)
        
    return redirect(url_for('admin.all_profiles'))

@admin.route('/admin/all_uploads')
def all_uploads():
    """Display all uploads to the admin."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    current_user = get_user(session['user_id'])
    if current_user.role != 'admin':
        return redirect(url_for('main.dashboard'))
    
    uploads = get_all_uploads()
    return render_template(
        'admin/all_uploads.html', 
        uploads=uploads, 
        current_user=current_user,
        datetime=datetime.now)

@admin.route('/admin/upload/delete/<int:upload_id>', methods=['POST'])
def delete_upload(upload_id):
    """Soft delete an upload (admin only)."""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    current_user = get_user(session['user_id'])
    if current_user.role != 'admin':
        return redirect(url_for('main.dashboard'))
    
    soft_delete_upload(upload_id)
    return redirect(url_for('admin.all_uploads'))
