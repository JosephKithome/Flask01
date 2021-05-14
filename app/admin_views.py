from app import app
from flask import render_template


@app.route("/admin/dashboard")
def admin():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def profile():
    return "<h1>admin Profile</h1>"
