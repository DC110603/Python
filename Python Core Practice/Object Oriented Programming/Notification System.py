"""1. You are building a notification system for a large-scale application such as a
banking platform or an online learning portal.
The system must support sending notifications through multiple channels such
as email, SMS, and push notifications.
Design a class named Notifier that represents the idea of sending a notification, not the
actual implementation.
This class must:
• Contain a method named send(message) whose responsibility is to send a message
to a user.
• Not provide any implementation for send(), because the way an email is sent is
fundamentally different from how an SMS or push notification is sent.
• Force every class that represents a specific notification type to provide its own
implementation of send().
Now create three separate classes:
• EmailNotifier
• SMSNotifier
• PushNotifier
Each of these classes must:
• Provide its own logic for sending the message.
• Store sensitive configuration details (such as API keys or server settings) in such a
way that they cannot be modified directly from outside the class.
Write client code that:
• Accepts a list of notifier objects.
• Calls send() on each object without checking what type of notifier it is.
Finally, explain within your answer:
• Why the base Notifier class should not contain any actual sending logic.
• Why forcing child classes to implement send() is safer than trusting developers to
remember it.
• Why writing if/else conditions based on notification type would become a problem
as the system grows. """
from abc import ABC,abstractmethod
class Notifier(ABC):
    def __init__(self,name,ph_no,mail):
        self.name=name
        self.__ph_no=ph_no
        self.__mail=mail
    @abstractmethod
    def send(self):
        pass
    @property
    def get_ph_no(self):
        return self.__ph_no
    @property
    def get_mail(self):
        return self.__mail
    @get_ph_no.setter
    def get_ph_no(self,new_ph_no):
        if len(str(new_ph_no))==10:
            self.__ph_no=new_ph_no
        else:
            print("Incorrect Phone Number")
    @get_mail.setter
    def get_mail(self, new_mail):
        if "@gmail.com" or "@yahoo.com" or "outlook.com" or "zohomail.in" in new_mail:
            self.__mail = new_mail
        else:
            print("Incorrect Mail")


class EmailNotifier(Notifier):
    def __init__(self, name,ph_no,mail):
        super().__init__(name,ph_no,mail)
    def send(self):
        if "@gmail.com" or "@yahoo.com" or "outlook.com" or "zohomail.in"in self.get_mail:
            return f"Mail Notification for {self.name}"
        else:
            return f"Incorrect Mail"

class SMSNotifier(Notifier):
    def __init__(self, name, ph_no, mail):
        super().__init__(name, ph_no, mail)
    def send(self):
        if len(str(self.get_ph_no))==10:
            return f"SMS Notification for {self.name}"
        else:
            return f"Incorrect Phone number"

class PushNotifier(Notifier):
    def __init__(self, name, ph_no, mail):
        super().__init__(name, ph_no, mail)
    def send(self):
        return f"Push Notification for {self.name}"

user1=EmailNotifier("swadeepa",9014999999,"swadeepa@gmail.")
print(user1.send())
print(PushNotifier.send(user1))
print(SMSNotifier.send(user1))