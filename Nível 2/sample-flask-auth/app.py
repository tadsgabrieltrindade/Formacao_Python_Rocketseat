from flask import Flask, request, jsonify
from flask_login import LoginManager
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret-key-for-tests"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

# @login_manager.user_loader
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        username = data.get("username")
        password = data.get("password")

        if username and password:
            return jsonify({"message": "Usuário autenticado com sucesso!"}), 200

        return jsonify({"message": "Credenciais inválidas!"}), 401 
    except:
        return jsonify({"message": "Erro ao processar login!"}), 500
        

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def hello_world():
    return jsonify({"message": "API running"}), 200

if  __name__ == '__main__':
    app.run(debug=True)