from app import db

class Upload(db.Model):
    """Upload model representing a file upload."""
    __tablename__ = 'uploads'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(512), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    user = db.relationship('User', backref=db.backref('uploads', lazy=True))
    
    def __repr__(self):
        return f'<Upload {self.filepath} by User {self.user_id}>'