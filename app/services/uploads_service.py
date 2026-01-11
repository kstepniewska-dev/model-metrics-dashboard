from app.models.upload import Upload
from app import db

def create_upload(user_id, filename, filepath):
    """Create a new upload record in the database."""
    upload = Upload(user_id=user_id, filename=filename, filepath=filepath)
    db.session.add(upload)
    db.session.commit()
    return upload

def get_upload_by_id(upload_id):
    """Get upload by ID (only if not deleted)."""
    return Upload.query.filter_by(id=upload_id, deleted_at=None).first()

def get_user_uploads(user_id):
    """Retrieve all uploads for a specific user."""
    return Upload.query.filter_by(user_id=user_id, deleted_at=None).all()

def get_all_uploads():
    """Retrieve all uploads in the system (for admin)."""
    return Upload.query.filter_by(deleted_at=None).all()

def soft_delete_upload(upload_id):
    """Soft delete an upload by setting its deleted_at timestamp."""
    upload = Upload.query.get(upload_id)
    if upload and upload.deleted_at is None:
        upload.deleted_at = db.func.current_timestamp()
        db.session.commit()
    return upload
