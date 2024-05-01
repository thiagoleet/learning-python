from flask import Flask
from src.main.routes.calculators import calc_route_bp

app = Flask(__name__)

# registrando a blueprint da calculadora np app
app.register_blueprint(calc_route_bp)