from User import User
class Admin(User):

    def __init__(self, name:str, password:str):
        self.fullName = name
        self.password = password
        self.email = None
        self.online = None
        self.current_room = None
        print("Admin has been created")


