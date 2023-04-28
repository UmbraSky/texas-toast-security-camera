from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)

app.secret_key = "jlsakdjflk;asjdfllhi"

@app.route("/")
def main():
    return "flask app is running"

if __name__ == "__main__":
    app.run(host="127.0.0.1")