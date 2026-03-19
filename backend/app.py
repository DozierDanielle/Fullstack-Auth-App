from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp  

app = Flask(__name__)  
app.config.from_object(Config)

CORS(app)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)  

@app.route("/")
def home():
    return {"message": "API running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)