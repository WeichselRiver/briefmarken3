from flask import Flask, render_template
import json
import os

app = Flask(__name__)

marken = [
    {"MichNr": "7", "filename": "Mn_7.jpg"},
    {"MichNr": "10 II", "Typ": "II", "filename": "Mn_10i.jpg"},
    {"MichNr": "10 I", "Typ": "I", "filename": "Mn_10ii.jpg"}
]

with open("marken.json", encoding="UTF8") as f:
    my_stamps = json.load(f)


@app.route("/")
def index():
    # image_names = os.listdir(r"static/images")
    return render_template("index.html", image_names=marken)


@app.route("/AD_Baden_index")
def ad_baden_index():
    return render_template("index_ad_baden.html")


@app.route("/AD_Baden/<int:jahr>")
def ad_baden(jahr):
    return render_template(
        "adbaden_1851.html", marken=my_stamps["AD Baden"]["1851"]["1-8"]
    )


if __name__ == "__main__":
    app.run(debug=True)
