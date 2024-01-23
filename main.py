from app.User import User
from app.Chat_room import Chat_room

user1 = User('Denis Kostyuk', 'abc123','414')
chat_room1 = Chat_room('Goats')
user1.join_chat_room(chat_room1)
print(user1.current_room)
print(chat_room1.getUsersList())
msg = 'Hello im new here What''s up?!'
user1.send_message(msg)
print(chat_room1.getMessageHistory())

user2 = User('David Losh', '356',"34324")
user2.join_chat_room(chat_room1)
print(chat_room1.getUsersList())
msg2 = 'YO YO WASSUP'
user2.send_message(msg2)
# print(chat_room1.getMessageHistory())
