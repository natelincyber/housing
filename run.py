from app import create_app, db
from app.models import HousingOption, User, Rating

app = create_app()

# Optional: Create shell context for Flask CLI
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'HousingOption': HousingOption, 'User': User, 'Rating': Rating}

if __name__ == '__main__':
    app.run(debug=True)
