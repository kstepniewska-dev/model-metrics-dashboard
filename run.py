import os
from dotenv import load_dotenv
from app import create_app, db
from app.models.user import User

# Load environment variables from .env file
load_dotenv()

app = create_app()

def init_db():
    """Initialize the database (create tables)."""
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")
        
def create_admin():
    """Create an admin user if not exists."""
    with app.app_context():
        if not User.query.filter_by(email='admin@example.com').first():
            admin = User(email='admin@example.com')
            admin_password = os.getenv('ADMIN_PASSWORD', 'default_password')
            admin.set_password(admin_password)
            admin.role = 'admin'
            db.session.add(admin)
            db.session.commit()
            print("Admin user created.")
            
if __name__ == '__main__':
    init_db()
    create_admin()
    app.run(debug=True)