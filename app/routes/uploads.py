import os
from flask import Blueprint, request, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename
from datetime import datetime
from app.services.uploads_service import create_upload
from app.models.upload import Upload

uploads = Blueprint('uploads', __name__)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@uploads.route('/upload', methods=['POST'])
def upload():
    """Handle file upload."""
    # Check if user is authenticated
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    # Check if file is in the request
    if 'file' not in request.files:
        return redirect(url_for('main.dashboard'))
    
    file = request.files['file']
    
    # Check if a file was selected
    if file.filename == '':
        return redirect(url_for('main.dashboard'))
    
    # Validation
    if file and allowed_file(file.filename):
        # Create secure filename
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        original_filename = secure_filename(file.filename)
        filename = f"{timestamp}_{original_filename}"
        
        # Ensure upload folder exists
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        
        # Save file to the upload folder
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        # Create upload record in the database
        user_id = session['user_id']
        create_upload(user_id, original_filename, filepath)
        
        # Redirect back to dashboard
        return redirect(url_for('main.dashboard'))
    
    # If file validation fails
    return redirect(url_for('main.dashboard'))