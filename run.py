from app import create_app, db

app = create_app()

def init_db():
    """Initialize the database (create tables)."""
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)