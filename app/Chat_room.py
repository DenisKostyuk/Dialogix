import time

class Chat_room:

    def __init__(self, roomname: str):
        self.roomName = roomname
        self.users = []
        self.userMessageHistory = {}
        self.creationTime = time.time()
        self.isPublic = True
        self.isActive = True
        self.generalMessageHistory = []
        self.topic = None
        self.bannedUsers = {}   # key=use value=reason why got banned

    def __str__(self):
        return self.roomName

    def addUser(self, userName: str):
        # Here i need to print to the chat room that a new user has joined the chat in live broadcast
        if userName not in self.users:
            self.users.append(userName)
        elif userName in self.bannedUsers:
            print('You Are Banned From This Room Due To The Reason : ' + self.bannedUsers[userName])
        else:
            print('Hey There, You Are Already Participating In The Chat! Have Fun')

    def removeUser(self,userName:str):
        if userName in self.users:
            self.users.remove(userName)
        else:
            print('This User Is Not Participating In This Room. Maybe You Meant Some One Else ?')

    def add_message(self,sender ,message):
        if sender not in self.userMessageHistory:
            self.userMessageHistory[sender] = []

        self.userMessageHistory[sender].append({'Time : ':time.time(), 'Content : ': message})
        self.generalMessageHistory.append({'Sender : ':sender,'Time : ':time.time(), 'Content : ': message})

    def broadcastMessage(self, sender, message):
        # Here i need to do it live broadcasted via socket
        print('The User : '+ sender + 'Has Sent A New Message : ' + message)

    def getMessageHistory(self) -> None:
        for message in self.generalMessageHistory:
            print('Message : ')
            for key, value in message.items():
                print(f" {key}: {value}")



    def getUsersList(self) -> list:
        return self.users

    def set_room_description(self, description: str):
        self.topic = description

    def ban_user(self, user: str):
        self.bannedUsers.append(user)

    def un_ban_user(self, user: str):
        if user in self.bannedUsers:
            del self.bannedUsers[user]
        else:
            print('This User Is Not In The List Of The Users Who Got Banned. Maybe You Meant Some One Else ? ')

    def close_room(self):
        self.isActive = False






