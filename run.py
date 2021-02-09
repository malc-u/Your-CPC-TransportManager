import os
from flask import Flask, render_template
from flask_mail import Mail, Message
from forms import ContactForm

# Enviroment variables  - containing sensitive info
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

#SECRET_KEY configuration
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


#Settings needed by Flask-Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['MAIL_USERNAME'],
    "MAIL_PASSWORD": os.environ['MAIL_PASSWORD'],
}

#Flask-Mail and Mail instance configuration
app.config.update(mail_settings)
mail = Mail(app)

"""
Routes and views
"""

#Index
@app.route('/')
def index():
    """
    Function that opens home/index page of the project.
    """

    return render_template('pages/index.html', 
                            title='Home')


#About
@app.route('/about')
def about():
    """
    Function that opens about page of the project.
    """

    return render_template('pages/about.html', 
                            title='About')


#Services
@app.route('/services')
def services():
    """
    Function that opens services page of the project.
    """

    return render_template('pages/services.html', 
                            title='Services')


#Contact
@app.route('/contact')
def contact():
    """
    Function that opens contact page of the project.
    """
    form = ContactForm()

    if form.validate_on_submit(): 
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(name,
                      sender=os.environ["MAIL_USERNAME"],
                      recipients=[os.environ["MAIL_USERNAME"]],
                      body="This is message from "+name+"\nEmail Address: "+email+"\n\nMessage sent:\n"+message)
        mail.send(msg)


    return render_template('pages/contact.html', 
                            title='Contact')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)