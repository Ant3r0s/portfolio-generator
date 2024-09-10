from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'  # Cambia esta clave por algo más seguro
    from .routes import main
    app.register_blueprint(main)
    return app
