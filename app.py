from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)

app.secret_key = "jlsakdjflk;asjdfllhi"