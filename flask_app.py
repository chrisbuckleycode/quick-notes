from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

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
    return 'This is another page'
