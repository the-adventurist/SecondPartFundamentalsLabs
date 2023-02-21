class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


message = input()
emails = []
while message != 'Stop':
    message_args = message.split()
    email = Email(message_args[0], message_args[1], message_args[2])
    emails.append(email)
    message = input()
send_emails = [int(x) for x in input().split(', ')]
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())
