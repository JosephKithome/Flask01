from app import app
from flask import render_template,redirect,request,jsonify,make_response
from datetime import datetime

# Image uploading
import os
from werkzeug.utils import secure_filename


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    print(app.config["ENV"])
    print(app.config["DB_NAME"])
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

@app.route("/sign_up", methods=['GET','POST'])
def sign_up():
    if request.method =="POST":
        req = request.form

        print(req)
        username =req["username"]
        email =req.get("email")
        password = request.form.get("password")

        print(username,email,password)
        
        return redirect(request.url)
    return render_template("public/auth/sign_up.html")  

# Dynamic urls

users ={
    "joseph":{
        
        "username":"joseph",
        "bio": "i am a fullstack web and mobile developer",
        "twitter_handle":"@RiserRiser2",
        "password":"password1"
    },
    "onesmus":{
        "username":"onesmus ",
        "bio": "i am a government official",
        "twitter_handle":"@onesones",
        "password":"password2"
    },
    "juliamer":{
        "username":"juliamer",
        "bio": "i am a musician",
        "twitter_handle":"@RiserRiser2",
        "password":"password3"
    }
}
# @app.route("/profile/<username>")
# def userProfile(username):

#     user = None

#     if username in users:
#         user=users[username]
#     return render_template("public/profile.html",username=username,user=user)           

 # multiple dynamic urls

@app.route("/multiple/<foo>/<bar>/<baz>")
def multipl(foo,bar,baz):
    return f"My foo is {foo},bar is {bar},baz is {baz}"

@app.route("/json",methods =["POST","GET"])  
def json():
    if request.is_json:
        req=request.get_json()
        print(type(req))
        print(req)
        response = {
            "message":"JSON received",
            "name":req.get("name")
        }
        res = make_response(jsonify(response),200)
        return res
    else:
        res = make_response(jsonify({"message":"No Json received!"}),400)
        return  res

# fetch api
@app.route("/guestbook")
def questbook():
    return render_template("public/guestbook.html")
    
@app.route("/guestbook/create_entry", methods=["POST"])
def create_entry():
    if request.is_json:
        req = request.get_json()
        print(req)
        res = make_response(jsonify({"message":"JSON received"}),200)

        return res
    return "JSON not received",403   

# query strings 
@app.route("/query") 
def query():
    print("Query Str",request.query_string)
    args = request.args
    # accessing querry strings 

    # for k,v in args.items():
    #     print(f"{k}:{v}")
    # if "title" in args:
    #     title =args.get("title")
    #     print(title)

    # if request.args:
    #     args = request.args
    #     if "foo" in args:
    #         foo = request.args.get("foo")
    #     print(foo)    

    if request.args:
        args = request.args
        serialized = ",".join (f"{k} :{v}" for k,v in args.items())
        return f"(Query) {serialized}",200  
    else:
        return "No query received",404    

# uploading images
def check_image_extension(filename):
    if not "." in  filename:
        return False

    else:
        ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    return False            

def allowed_filename_size(filesize):
    if int(filesize) <=app.config["MAX_IMAGE_FILESIZE"]:
        return True
    return False    
@app.route("/upload-image",methods=["GET","POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            if not allowed_filename_size(request.cookies.get("filesize")):
                print("File exceeded maximum limit required")
                return redirect(request.url)
                

            image = request.files["image"]
            print(image)

            if image.filename=="":
                print("image must have a name")
                return redirect(request.url)

            if not check_image_extension(image.filename):
                print("The image extension is not accepted try another")  
                return redirect(request.url)  
            else:
                filename = secure_filename(image.filename)    

                image.save(os.path.join(app.config["IMAGE_UPLOADS"],filename))
                print("Image saved successfully")
                return redirect(request.url)
    return render_template("public/upload_image.html")  


# sending files 
"""
string:
int:
float:
path:
uuid:

"""
from flask import send_from_directory,abort

@app.route("/get-image/<image_name>")
def get_image(image_name):
  
  try:
      return send_from_directory(app.config["CLIENT_IMAGES"],image_name,as_attachment=True)
  except FileNotFoundError:
      abort(404)  

@app.route("/get-csv/<filename>")
def get_csv(filename):
  
  try:
      return send_from_directory(app.config["CLIENT_CSV"],filename,as_attachment=False)
  except FileNotFoundError:
      abort(404)    

# working with cookies
from flask import request,make_response

@app.route("/cookies")
def cookies():
    res = make_response("Cookies",200)

    # Accessing cookies 
    cookies =request.cookies
    cookie3 = cookies.get("footbal")
    print(cookie3)
    # properties of cookies 
    res.set_cookie("Cookie", value="Chocolate",
    max_age=10,
    expires=None,
    path=request.path,
    domain=None,
    secure=False,
    httponly=False,)

    res.set_cookie("cart", "cart items")
    res.set_cookie("footbal", "livescore")
    return res 

from flask import render_template,  request,session,redirect,url_for

@app.route("/login",methods=["GET","POST"])
def login():
    
    if request.method == "POST":
        req = request.form
        username = req.get("username")
        # email = req.get("email")
        password = req.get("password")
        print(username,password)
        if not username in users:
            print("username not found")
            return redirect(request.url)
        else:
            user = users[username]  

        if not password == user["password"]:
            print("Incorrect password") 
            return redirect(request.url) 

        else:
            # Dont store sensitive information in cookies
            session["USERNAME"] = user["username"] 
            print("user added to session")  
            # return redirect(request.url) 
            return redirect(url_for("profile_page"))    
    return render_template("public/auth/sign_in.html")

@app.route("/profile_page") 
def profile_page():
    if session.get("USERNAME",None) is not  None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template("public/profile.html",user=user)  
    else:
        print("üsername not found")
        return redirect(url_for('login'))

@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME")
    return redirect("login")