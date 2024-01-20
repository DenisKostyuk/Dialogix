import dataclasses
import User
class Message:

    def __init__(self, sender:str, time:str, content:str):
        self.sender = sender
        self.time = time
        self.content = content

    def showMessage(self):
        print(self.sender.fullname + ' Have sent you a new Message :' + self.content)

