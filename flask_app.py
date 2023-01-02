from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
# built-in, don't need to install with pip
import logging

app = Flask(__name__)
# Used during development, enables more detailed error messages in the browser instead of just showing the Error 500 Page
app.config["DEBUG"] = True

# Required for logger.info. Also saves to file.
# Adds timestamp, name, level name, log message
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='application.log',
                    filemode='w')

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#    username="the username from the 'Databases' tab",
#    password="the password you set on the 'Databases' tab",
#    hostname="the database host address from the 'Databases' tab",
#    databasename="the database name you chose, probably yourusername$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#    username="the username from the 'Databases' tab",
#    password="the password you set on the 'Databases' tab",
#    hostname="the database host address from the 'Databases' tab",
#    databasename="the database name you chose, probably yourusername$comments",


db = SQLAlchemy(app)



class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


# legacy in-memory variable before using db
#comments = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        # legacy in-memory comments rendering, before using db
        #return render_template("main_page.html", comments=comments)

        return render_template("main_page.html", comments=Comment.query.all())

    # legacy in-memory variable before using db
    #comments.append(request.form["contents"])

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()

    return redirect(url_for('index'))

# simple page sample
@app.route('/anotherpage')
def anotherpage():
    # root logger e.g. logger1.info for other loggers
    logging.info('Returning AnotherPage blabla')
    return 'This is another page'
