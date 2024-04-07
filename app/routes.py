from flask import render_template, request, g
import requests

from . import app, db
from .models import Blogs

@app.before_request
def set_layout():
    g.useLayout = request.headers.get('hx-request') != 'true'

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/blogs")
def blogs():
    blogs = Blogs.query.all()
    return render_template('blogs.html', blogs=blogs)

@app.route("/about-us")
def about_us():
    return render_template('about-us.html')

@app.route("/contact")
def contact():
    # res = requests.get('https://dummyjson.com/products')
    return render_template('contact.html')