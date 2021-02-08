import os
from flask import Flask, render_template

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route('/')
def index():
    """
    Function that opens home/index page of the project.
    """

    return render_template('pages/index.html', 
                            title='Home')


@app.route('/about')
def about():
    """
    Function that opens about page of the project.
    """

    return render_template('pages/about.html', 
                            title='About')


@app.route('/services')
def services():
    """
    Function that opens services page of the project.
    """

    return render_template('pages/services.html', 
                            title='Services')


@app.route('/contact')
def contact():
    """
    Function that opens contact page of the project.
    """

    return render_template('pages/contact.html', 
                            title='Contact')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)