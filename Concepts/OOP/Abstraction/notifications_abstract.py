"""
5 ) --- 
Build an abstract class Notification with abstract method send(message).
Subclasses: EmailNotification, SMSNotification, PushNotification.
"""
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message=None) -> None:
        self._messsage = message
    @abstractmethod
    def send(self) -> str:
        pass
    def __repr__(self) -> str:
        return (
            "--------------------------\n"
            f"{self.__class__.__name__}\nSendirg Message:\n    {self._messsage}" 
        )
class Email_Notification(Notification):
    def __init__(self, sender: str, receiver: str, issue : str, message="...") -> None:
        super().__init__(message)
        self._sender = sender
        self._receiver = receiver
        self._issue = issue
    def send(self) -> str:
        return f"Sending message: {self._messsage}\nTo {self._receiver} from {self._sender}\nIssue: {self._issue}"    
    def __repr__(self) -> str:
        return super().__repr__() + f"\nIssue: {self._issue}\nSend: {self._sender}\nReceive: {self._receiver}"
class SMS_Notification(Notification):
    def __init__(self,sender: str, receiver: str,  message="...") -> None:
        super().__init__(message)
        self._sender = sender
        self._receiver = receiver
    def send(self) -> str:
        return f"Sending message: {self._messsage}\nTo {self._receiver} from {self._sender}"
    def __repr__(self) -> str:
        return super().__repr__() + f"\nSend: {self._sender}\nReceive: {self._receiver}"
class Push_Notification(Notification):
    def __init__(self, message : str) -> None:
        super().__init__(message)
    def send(self) -> str:
        return f"Sending message: {self._messsage}"
def main():
    email = Email_Notification("Jose Frernandez", "Maria Delgado", "Trabajo", "Hola espero que se encuentre bien...")
    sms = SMS_Notification("Fernando", "Pepe", "Hola amigo\nespero estes en...")
    push_notification = Push_Notification("Envio de paquete listo\nEsperamos su confirmacion para...")
    print("\n".join(f"{notification}\n <> {notification.send()}" for notification in [email, sms, push_notification]))

if __name__ == "__main__":
    main()
