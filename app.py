from config import Config
from app import app, db

@app.before_first_request
def create_tables():
    print("Creating database tables...")
    db.create_all()
    print("Done!")

if __name__ == '__main__':
    # app.run(debug=Config.DEBUG)
    app.secret_key=Config.SECRET_KEY
    app.run(host='127.0.0.1', port=8087, debug=True)


