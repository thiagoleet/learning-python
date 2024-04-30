from flask import Flask, jsonify, request, send_file, render_template
from datetime import datetime, timedelta
from repository.database import db
from db_models.payment import Payment
from payments.pix import Pix

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY_WEBSOCKET"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)


@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    data = request.get_json()
    if "value" not in data:
        return jsonify({"message": "Invalid value"}), 400

    try:
        expiration_date = datetime.now() + timedelta(minutes=30)
        new_payment = Payment(
            value=data["value"], expiration_date=expiration_date)

        pix_obj = Pix()
        data_payment_pix = pix_obj.create_payment()
        new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]
        new_payment.qr_code = data_payment_pix["qr_code_path"]

        db.session.add(new_payment)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"}), 500
    else:
        return jsonify({
            "message": "The payment has been created",
            "payment": new_payment.to_dict()
        }), 201


@app.route("/payments/pix/qr_code/<file_name>", methods=["GET"])
def get_image(file_name):
    return send_file(f"static/img/{file_name}.png", mimetype="image/png")


@app.route("/payments/pix/confirmation", methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"}), 202


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    return render_template("payment.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
