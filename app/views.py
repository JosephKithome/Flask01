from app import app
from flask import render_template,redirect,request,jsonify,make_response
from datetime import datetime


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
    "Joseph":{
        "name":"joseph kithome",
        "bio": "i am a fullstack web and mobile developer",
        "twitter_handle":"@RiserRiser2"
    },
    "onesmus":{
        "name":"onesmus kithome",
        "bio": "i am a government official",
        "twitter_handle":"@onesones"
    },
    "juliamer":{
        "name":"juliamer Waaris",
        "bio": "i am a musician",
        "twitter_handle":"@RiserRiser2"
    }
}
@app.route("/profile/<username>")
def userProfile(username):

    user = None

    if username in users:
        user=users[username]
    return render_template("public/profile.html",username=username,user=user)           

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