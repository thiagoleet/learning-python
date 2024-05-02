# SOLID - Dependency Inversion Principle (DIP)

from .notificator_interface import NotificatorInterface


class ClientService:  # High-level module
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)
