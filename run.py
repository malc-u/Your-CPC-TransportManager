import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Function that opens home/index page of the project.
    """
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)