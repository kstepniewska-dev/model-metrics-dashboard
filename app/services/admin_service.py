from app.models.upload import Upload
from app.models.user import User
from app import db

def get_user(user_id):
    """Retrieve a user by their ID."""
    return User.query.get(user_id)

def get_all_users():
    """Retrieve all users except admins in the system."""
    return User.query.filter(User.role != 'admin').all()

def soft_delete_user(user_id):
    """Soft delete a user by setting their deleted_at timestamp."""
    user = User.query.get(user_id)
    if user and user.role != 'admin' and user.deleted_at is None:
        user.deleted_at = db.func.current_timestamp()
        db.session.commit()
    return user

def soft_delete_uploads_by_user_id(user_id):
    """Soft delete all uploads associated with a user."""
    uploads = Upload.query.filter_by(user_id=user_id, deleted_at=None).all()
    for upload in uploads:
        upload.deleted_at = db.func.current_timestamp()
    db.session.commit()
    return uploads
