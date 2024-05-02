# Erro 400 -> Bad Request
# Erro 422 -> Unprocessable Entity

class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unprocessable Entity"
        self.status_code = 422


try:
    print("Estou no bloco try")
    raise HttpUnprocessableEntityError("Estou lançando uma exceção")
except Exception as ex:
    print("Estou no tratamento de erro")
    print(str(ex.name))
    print(str(ex.status_code))
    print(str(ex.message))
