from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from User import User
from Chat_room import Chat_room


app = Flask(__name__, template_folder=r"C:\Users\denis\Desktop\Projects\Dialogix\templates")

users = []
rooms = []

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

                    return redirect(url_for("rooms"))
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
            print(users)
            return redirect(url_for("rooms"))
    return render_template("create_account.html")




@app.route("/rooms")
def rooms():
    if not rooms:
        return redirect(url_for("create_room"))

    return render_template("rooms.html")


@app.route("/create_room")
def create_room():
    if request.method == "POST":
        if request.form["action"] == "Create Room":
            room_name = request.form["room_name"]
            new_room = Chat_room(room_name)
            rooms[room_name] = new_room
            return redirect(url_for("room"),room_name=room_name)


    return render_template("create_room.html")

@app.route("/room/<room_name>", methods=["POST", "GET"])
def room_chat(room_name):
    return render_template("room_chat.html")






if __name__ == "__main__":
    app.run(debug=True)