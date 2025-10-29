from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret-key-for-tests"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Hello World"

if  __name__ == '__main__':
    app.run(debug=True)