from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}<h1>"

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

@app.route('/page/<int:postID>')
def show_page(postID):
    return 'Page number %d' %postID



@app.route('/signin')
def signin():
    return render_template('sign in.html')


@app.route('/')
def hello_world():
    return 'Hello world'




if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

