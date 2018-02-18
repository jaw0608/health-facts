import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template
from random import randint
app = Flask(__name__)


# below is routing or mapping, tying the url to the python function
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/random')
def random():
    length = getLength()
    i = randint(0,int(length))
    info=get(i- 1)
    info=info.split('||',1)
    img=info[0]
    fact=info[1]
    print("Loading fact number: "+str(i))
    return render_template("profiles.html", imgsrc=img, fact=fact, post=i)
@app.route('/<int:post>')
def post(post):
 length=getLength()
 if post<=length:
    info=get(post - 1)
    info=info.split('||',1)
    img=info[0]
    fact=info[1]
    print("Loading fact number: " + str(post))
    return render_template("profiles.html", imgsrc=img, fact=fact, post=post)
 else:
     render_template("home.html")
def getLength():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='Jaw0608.mysql.pythonanywhere-services.com',
                                       database='Jaw0608$info',
                                       user='Jaw0608',
                                       password='HIDDEN')
        if conn.is_connected():
            print("Connected")
            # Create a Cursor object to execute queries.
            cur = conn.cursor()
            cur.execute("""SELECT * FROM fact""")
            list=cur.fetchall()
            num=len(list)
            return num

    except Error as e:
        print(e)

def get(id):
    conn = mysql.connector.connect(host='Jaw0608.mysql.pythonanywhere-services.com',
                                       database='Jaw0608$info',
                                       user='Jaw0608',
                                       password='ApplePie1')
    cur = conn.cursor()
    cur.execute("Select * FROM fact")
    while id>0:
        cur.fetchone()
        id=id-1
    row=cur.fetchone()
    return row[0]+"||"+row[1]


# Start this webserver, only if this script was run directly (meaning its the main file)
if __name__ == "__main__":
    app.run(debug=True)

