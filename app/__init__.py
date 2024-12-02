from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config
import time

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    csrf.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    with app.app_context():
        # Intentar conectar a la base de datos con reintentos
        max_retries = 5
        for retry in range(max_retries):
            try:
                db.create_all()
                break
            except Exception as e:
                if retry == max_retries - 1:
                    raise e
                print(f"Intento {retry + 1} de {max_retries} para conectar a la base de datos...")
                time.sleep(5)
    
    return app