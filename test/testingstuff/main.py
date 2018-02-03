from flask import Flask, request, render_template
from random import randint
app = Flask(__name__)


# below is routing or mapping, tying the url to the python function
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/random')
def random():
    f = open('posts.txt', 'r')
    posts = f.read().splitlines()
    length = len(posts)
    i = randint(0,length)
    line = posts[i-1]
    img = line[0:7]
    facts = line[7:]
    return render_template("profiles.html", imgsrc=img, fact=facts, post=i)
@app.route('/<int:post>')
def post(post):
    print(post)
    j=post
    f=open('posts.txt', 'r')
    posts=f.read().splitlines()
    length=len(posts)
    print(posts)
    print(length)
    if post<=length:
        print("Post %s Valid",post)
        line = posts[post-1]
        img = line[0:7]
        facts = line[7:]
        print(facts)
        f.close()
        return render_template("profiles.html", imgsrc=img, fact=facts, post=j)

    else:
        print("Post DNE")
        f.close()

        return ""


# Start this webserver, only if this script was run directly (meaning its the main file)
if __name__ == "__main__":
    app.run(debug=True)



