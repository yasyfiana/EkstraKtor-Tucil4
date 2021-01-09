#Yasyfiana Fariha
#13518143
#app
#Tucil 4

from flask import Flask, render_template, Response, request, redirect, url_for, render_template
from Program import *

"""
File ini mengatur mengenai pembangunan aplikasi ini
menggunakan flask. Laman web dibuat dengan rout yang sama
namun menggunakan 3 template html yaitu perihal, hasil, dan upload.
"""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/", methods=["POST","GET"])
def upload():
    render_template("upload.html")
    if request.method == "POST":
        if(request.form["button"]=="cek"):
            word = request.form["key"]
            algo = request.form["options"] 
            files = request.files.getlist("file[]")
            loc = "doc\\"
            hasil = []
            for f in files:
                hasil.append(match(word,algo,f.filename))
                # print(hasil)
            return render_template("hasil.html", result = hasil, key = word)
        elif(request.form["button"] == "disini"):
            return render_template("perihal.html")
    else:
        return("Failed!")


if __name__ == "__main__":
    app.run()