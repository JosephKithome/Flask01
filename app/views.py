from app import app
from flask import render_template,redirect
from datetime import datetime


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "<h1>Keep going joseph</h1>"

@app.route("/jinja") 
def jinja():
    my_name = "Joseph Kithome"
    my_html ="<h1>THIS IS SOME HTML</h1>"
    my_script ="<script>alert('You got hacked!')</script>"
    age = 18
    langs =["Python Django","python Flask","React","Android java","android kotlin"]
    diction ={
        "Music":"Lingala",
        "Mobile":"Java",
        "WebDev":"Javascript"
    }
    myTup = ("Red","Green","Yellow")

    cool = True
    class GitRemote:
        def __init__(self,name,description,url):
            self.name=name
            self.description = description
            self.url = url
        def pull(self):
            return f"Pulling {self.name} repo"

        def clone(self):
            return f"Cloning  into {self.url}"
    my_git=GitRemote(
        "Flask jinja",
        "Jinja templates",
        "https://github.flaskoo1.git"
    )        
    date = datetime.utcnow()
    def repeat(x,qty):
        return x * qty            
            
    return render_template(
        "public/jinja.html",
        my_name=my_name,
        age =age,
        langs = langs,
        myTup=myTup,
        diction=diction,
        cool=cool,
        GitRemote=GitRemote,
        repeat=repeat,
        my_git = my_git,
        date = date,
        my_html =my_html,
        my_script=my_script)   
