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
    e = int(id)
    abort(e)

@app.errorhandler(400)
def bad_request(error):
    print("400")
    return render_template("error.html", code = "400"), 400

@app.errorhandler(401)
def unauthorized(error):
    print("401")
    return render_template("error.html", code = "401"), 401

@app.errorhandler(403)
def forbidden(error):
    print("403")
    return render_template("error.html", code = "403"), 403

@app.errorhandler(404)
def not_found(error):
    print("404")
    return render_template("error.html", code = "404"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    print("405")
    return render_template("error.html", code = "405"), 405

@app.errorhandler(406)
def not_acceptable(error):
    print("406")
    return render_template("error.html", code = "406"), 406

@app.errorhandler(408)
def request_timeout(error):
    print("408")
    return render_template("error.html", code = "408"), 408

@app.errorhandler(410)
def gone(error_code):
    print("410")
    return render_template("error.html", code = "410"), 410

@app.errorhandler(413)
def payload_too_large(error):
    print("413")
    return render_template("error.html", code = "413"), 413

@app.errorhandler(415)
def unsupported_media_type(error):
    print("415")
    return render_template("error.html", code = "415"), 415

@app.errorhandler(429)
def range_not_satisfiable(error):
    print("429")
    return render_template("error.html", code = "429"), 429

@app.errorhandler(500)
def internal_server_error(error):
    print("500")
    return render_template("error.html", code = "500"), 500

@app.errorhandler(501)
def not_implemented(error):
    print("501")
    return render_template("error.html", code = "501"), 501


if __name__ == "__main__":
    app.run(host="127.0.0.1")