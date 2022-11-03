from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

@app.route('/page/<int:postID>')
def show_page(postID):
    return 'Page number %d' %postID

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signin')
def signin():
    return render_template('sign in.html')


@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/login')
def login():
    return 'Login Page'
@app.route('/home')
def home():
    return 'Home Page'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
