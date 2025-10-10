from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user database
USERS = {"testuser": "password123"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if USERS.get(username) == password:
            return f"Welcome, {username}!"
        return "Invalid credentials", 401
    return '''
        <form method="post">
            <input name="username" placeholder="Username"/>
            <input name="password" type="password" placeholder="Password"/>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
