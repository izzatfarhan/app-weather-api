import pandas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pandas.read_csv("") # read data in csv file
    temperature = df.station(date)  # label temperature, call statiton in df
    return {"station" : station,
            "date" : date,
            "temperature" : temperature}
if __name__ == "__main__":
    app.run(debug=True)
