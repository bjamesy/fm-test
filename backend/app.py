from flask import Flask, jsonify, request, json, abort, make_response
from flask_mysqldb import MySQL
from flask_cors import CORS
import os 

app = Flask(__name__)

app.config.from_pyfile('settings.py')

mysql = MySQL(app)

CORS(app, origins=[os.environ.get("CLIENT_URL")])


# a POST route as "/login" to allow any user with correct username and password to login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return "post login"
    elif request.method == "GET":
        return "get login"

# a POST route as "/signup" to allow new user to sign up
@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        return "post signup"

# a POST route as "/logout" to allow new user to sign up
@app.route("/logout", methods=["POST"])
def logout():
    if request.method == "POST":
        return "post logout"

# a GET route as "/users" to read all records from the MySQL Users table
@app.route("/users", methods=["GET"])
def get_users():
    if request.method == "GET":
        return "get users "

# a GET route as "/products" to read all records from the MySQL Products table
@app.route("/products", methods=["GET"])
def get_products():
    if request.method == "GET":
        return "get products"


if(__name__ == "__main__"):
    app.run(debug=True)