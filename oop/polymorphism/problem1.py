'''Build a notification system with base class Notification having a send() method.
 Implement:

EmailNotification
SMSNotification
PushNotification

Add priority levels (high, medium, low) and implement a queue system that sends 
notifications based on priority and type.'''

class Notification:
    def send(self):
        pass