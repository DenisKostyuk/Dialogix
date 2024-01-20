class User:

    def __init__(self, userName:str, password:str):
        self.fullName = userName
        self.password = password
        self.online = False
        self.current_room = None

    def send_message(self, msgContent:str) -> None:
        if self.current_room is not None:
            self.current_room.add_message(self.fullName, msgContent)
        else:
            print('You Are Not Participating In Any Room Yet.')


    def leave_chat_room(self) -> None:
        self.current_room = None

    def join_chat_room(self, roomName):
        self.online = True
        self.current_room = roomName
        roomName.addUser(self.fullName)



