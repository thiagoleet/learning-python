from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)


@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()
    if "value" not in data:
        return jsonify({"message": "Invalid value"}), 400

    try:
        expiration_date = datetime.now() + timedelta(minutes=30)
        new_payment = Payment(
            value=data["value"], expiration_date=expiration_date)
        db.session.add(new_payment)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"}), 500
    else:
        return jsonify({
            "message": "The payment has been created",
            "payment": new_payment.to_dict()
        }), 201


@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"}), 202


@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return "pagamento pix"


if __name__ == '__main__':
    app.run(debug=True, port=3000)
