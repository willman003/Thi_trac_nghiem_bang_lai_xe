from DoAn_LTV2 import app
from flask import render_template,session

@app.route('/',methods=['GET','POST'])
def index():
    session.clear()
    return render_template('index.html')