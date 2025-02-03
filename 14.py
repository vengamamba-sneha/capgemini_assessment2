class Notification:
    def send(self):
        print('notifications')
class EmailNotification:
    def send(self):
        print('u got an email')
class SMSnotification:
    def send(self):
        print('you got a SMS')
def fun(a):
    a.send()
e=EmailNotification()
fun(e)
s=SMSnotification()
fun(s)
