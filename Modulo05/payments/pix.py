import uuid
import qrcode


class Pix:
    def __init__(self) -> None:
        pass

    def create_payment(self):
        # criar pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())

        # código copia e cola
        hash_payment = f"hash-{bank_payment_id}"

        # qr_code
        img = qrcode.make(hash_payment)
        qr_code_path = f"qr_code_payment_{bank_payment_id}"
        img.save(f"static/img/{qr_code_path}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path":  qr_code_path
        }
