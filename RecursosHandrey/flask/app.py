from flask import Flask
from flask_migrate import Migrate
from modelos.modelos import db
from flask_restful import Api
from config import Config
from vistas import VistaUsuario, VistaSignIn, VistaLogin
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# Inicializar la base de datos y las migraciones
db.init_app(app)
migrate = Migrate(app, db)
jwt=JWTManager(app)

# Registrar los blueprints
api.add_resource(VistaUsuario, '/usuarios')
api.add_resource(VistaLogin, '/login')
api.add_resource(VistaSignIn, '/signin')


if __name__ == '__main__':
    app.run(debug=True)
