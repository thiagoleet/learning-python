from repository.database import db
from mixins.to_dict_mixin import ToDictMixin


class Payment(db.Model, ToDictMixin):
    __tablename__ = 'payments'
    # id, value, paid, bank_payment_id, qr_code, expiration_date
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(255), nullable=True)
    expiration_date = db.Column(db.DateTime, nullable=False)
