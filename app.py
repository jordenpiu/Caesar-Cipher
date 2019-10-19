from flask import *
from wtforms import *
import caesarCypher

app = Flask(__name__)



class getMessage(Form):
        #declare variables against fields created
    message = StringField("Enter your message:", [validators.Length(min=1, max=90)])
    mode = StringField("Mode (e or d):", [validators.Length(min=1, max=10)])
    key= StringField("key: ", [validators.Length(min=1, max = 5)])

@app.route("/")
def greet():
    return "<h1> Go to /cyph/</h1>"

@app.route("/cyph/", methods = ["GET", "POST"])
def cypher():

    try:
        form = getMessage(request.form)
        if request.method == "POST" and form.validate:
            message = form.message.data
            key = form.key.data
            mode = form.mode.data

            x = caesarCypher
            data_value = x.getTranslatedMessage(mode = "{}".format(mode),message = "{}".format(message),key = int("{}".format(key)))
            print(data_value)
            return f"<p>Encoded: {data_value} </p>"

        return render_template("registration.html", form = form)



    except Exception as e:
        print(e)



if __name__ == "__main__":
     app.debug = True
     app.run()
