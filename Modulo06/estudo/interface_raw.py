from abc import ABC, abstractmethod


class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass


class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")


class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")


# notification_sender = SMSNotificationSender()
# notification_sender.send_notification("Hello World")


class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, mensaje: str) -> None:
        # some validation
        # ...
        self.__notification_sender.send_notification(mensaje)


obj = Notificator(SMSNotificationSender())  # Injeção de dependência
obj.send("Hello World")
