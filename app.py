import sys
import os
import random
import markdown
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #Single Page App
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=80)
    app.run(debug=True)
