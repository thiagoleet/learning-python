import uuid
import qrcode


class Pix:
    def __init__(self) -> None:
        pass

    def create_payment(self):
        # criar pagamento na instituição financeira
        bank_payment_id = uuid.uuid4()

        # código copia e cola
        hash_payment = f"hash-{bank_payment_id}"

        # qr_code
        img = qrcode.make(hash_payment)
        qr_code_path = f"static/img/qr_code_payment_{bank_payment_id}.png"
        img.save(qr_code_path)

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path":  qr_code_path
        }
