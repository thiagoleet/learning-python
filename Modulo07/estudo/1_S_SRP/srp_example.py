# SOLID - Single Responsability Principle (SRP)

class Process:

    def handle(self, username: str, password: str) -> None:
        if selk.__verify_input_data(username, password):  # 1
            self.__verify_input_in_database(username)  # 2
            self.__insert_new_user(username, password)  # 3
        else:
            self.__raise_error('Dados Invalidos')

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados...')
        print('Verificando existencia do usuario...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuarios realizado com sucesso!')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)
