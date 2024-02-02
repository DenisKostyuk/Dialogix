from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from User import User
from Chat_room import Chat_room
from flask_socketio import SocketIO

app = Flask(__name__, template_folder=r"C:\Users\denis\Desktop\Projects\Dialogix\templates")
app.config["SECRET_KEY"] = "hellogoodbye"
app.config['PERMANENT_SESSION_LIFETIME'] = 30
socketio = SocketIO(app)


users = []
rooms = {}

@app.route("/" )
def redirecting():
    return redirect(url_for("home"))

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form["action"] == "Sign in":
            return redirect(url_for("login"))
        else:
            return redirect(url_for("create_account"))
    return render_template("home.html")
    # print("Here you create a new account if you dont have one yet PAGE 1.1")


@app.route("/login", methods=["POST", "GET"])
def login():
    message = None
    if request.method == "POST":
        if request.form["action"] == "Log in":
            user_name = request.form["username"]
            password = request.form["password"]
            for user in users:
                if user.fullName == user_name and user.password == password:

                    return redirect(url_for("display_rooms"))
            message = "Incorrect User Name Or Password , Please Try Again .."


    return render_template("login.html", message=message)

@app.route("/create_account",methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        if request.form["action"] == "Create":
            user_name = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]
            usr = User(str(user_name),str(password),str(email))
            users.append(usr)
            session["name"] = user_name
            print("this is the session name ==== ", session["name"])
            print(users)
            return redirect(url_for("display_rooms"))
    return render_template("create_account.html")




@app.route("/rooms")
def display_rooms():
    return render_template("rooms.html",rooms=rooms)


@app.route("/create_room", methods=["GET","POST"])
def create_room():
    if request.method == "POST":
        if request.form["action"] == "Create":
            room_name = request.form["room_name"]
            new_room = Chat_room(room_name)
            rooms[room_name] = new_room
            session["room"] = room_name
            return redirect(url_for("room_chat",room_name=room_name))
            user_name = session.get("name")
            for user in users:
                if user.fullName == user_name:
                    user.current_room = room_name
    return render_template("create_room.html")


    return render_template("create_room.html")

@app.route("/room/<room_name>", methods=["POST", "GET"])
def room_chat(room_name):
    print("from the room_chat the room name is : ",room_name)
    session["room"] = room_name
    for user in users:
        if user.fullName == session.get("name"):
            user.current_room = room_name
            print("in method room_chat , the users room is :", user.current_room)
    # room = rooms.get(room_name)
    return render_template("room_chat.html", room=room_name)

@socketio.on("message")
def handle_message(message):
    name = session.get("name")
    room = session.get("room")
    socketio.emit('message', {'name': name, 'message': message})


@socketio.on("participants")
def show_users_in_room():
    room_name = session.get("room")
    print("room name is : ", room_name)
    users_in_room = [user.fullName for user in users if user.current_room == room_name]
    socketio.emit("participants", [{"username": fullName} for fullName in users_in_room])
    print("Current users in the room are: ", users_in_room)







if __name__ == "__main__":
    try:
        socketio.run(app,debug=True, allow_unsafe_werkzeug=True)
    finally:
        session.clear()