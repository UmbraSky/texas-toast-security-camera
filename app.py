from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)

app.secret_key = "jlsakdjflk;asjdfllhi"

@app.route("/")
def main():
    return render_template("GUI.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/test_error_<id>")
def error(id):
    return render_template("error.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1")