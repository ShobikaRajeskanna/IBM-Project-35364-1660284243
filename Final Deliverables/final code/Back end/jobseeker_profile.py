from flask import *#importing flask (Install it using python -m pip install flask)
import os
import ibm_db
import bcrypt
#import send_from_directory
app = Flask(__name__) #initialising flask
app.secret_key = ''
PEOPLE_FOLDER = os.path.join('static', 'people_photo')

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=phb43134;PWD=mTTnIE45Raj9A0rr",'','')


@app.route("/") #defining the routes for the home() funtion (Multiple routes can be used as seen here)
@app.route("/home")

def dashboard():
    return render_template("dashboard.html") #rendering our home.html contained within /templates
