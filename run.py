import os
from flask import Flask, render_template, flash, url_for, redirect
from flask_mail import Mail, Message
from forms import ContactForm

# Enviroment variables  - containing sensitive info
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

#SECRET_KEY configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


#Settings needed by Flask-Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD'),
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
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Function that opens contact page of the project with contact form included.
    Form sends all required contact details provided by the sender and is validated
    on on submit to make sure no information is missing.
    """
    form = ContactForm()

    if form.validate_on_submit(): 
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(name,
                      sender=os.environ.get("MAIL_USERNAME"),
                      recipients=[os.environ.get("MAIL_USERNAME")],
                      body="This is message from "+name+"\nEmail Address: "+email+"\n\nMessage sent:\n"+message)
        mail.send(msg)
        flash(u'Your message has been sent.', 'danger')
        return redirect(url_for('index'))

    return render_template('pages/contact.html', 
                            title='Contact', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)