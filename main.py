import pandas as pd
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = "data_small/TG_STAID"+ str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates = ["    DATE"])  # read data in csv file
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() /10  # label temperature, call statiton in df
    return {"station" : station,
            "date" : date,
            "temperature" : temperature}

@app.route('/api/v1/<word>/')
def page(word):
    definition = word.upper()
    return {"definition": definition,
            "word": word}

if __name__ == "__main__":
    app.run(debug=True, port=5001) # specify port if running multiple apps
