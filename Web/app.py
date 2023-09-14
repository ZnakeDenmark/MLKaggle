import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

#Vi loader vores pickle med pickle filen som vi lavet i jupyter notebook
model = pickle.load(open("./Job.pkl", "rb"))

#Vi loader home med template test.html
@app.route("/")
def home():
    return render_template("test.html")

#This is the function to predict the outcome
@app.route("/predict", methods=["POST"])
def predict():
    #Her vil den finde ud af hvad man har valgt på hjemmesiden og finde ud daf om det giver mening i modellen
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)

#her får vi så vores prediction som output
    output = prediction[0]

#Her har vi en array som giver os de 2 svar som er mulige
    Employment = ["No", "Yes"]

#Her siger vi til systemet at den skal loade test.html men at vores Jinja variable "prediction" skal fortælle os om det er No eller Yes
    return render_template(
        "test.html", prediction="Employed?: {}".format(Employment[output])
    )


if __name__ == "__main__":
    app.run(debug=True)