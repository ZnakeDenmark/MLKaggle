import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("./MarvelDCName.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)

    output = prediction[0]

    names = ["test", "test2", "test3", "test4", "test1", "test5"]


    return render_template(
        "index.html", prediction="Name of Character: {}".format(output)
    )


if __name__ == "__main__":
    app.run(debug=True)