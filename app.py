from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Carregar modelo e vetorizador
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    text = ""

    if request.method == "POST":
        text = request.form["description"]
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]

    return render_template("index.html", prediction=prediction, text=text)

if __name__ == "__main__":
    app.run(debug=True)
