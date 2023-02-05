import pandas as pd
from flask import Flask, url_for, request, render_template, Blueprint, redirect
app = Flask(__name__)


#loads csv file into 3 arrays
df = pd.read_csv("data/list.csv")

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/search', methods=['POST', 'GET'])
def search():
    query = request.form['query']
    return redirect('/results?query=' + query)


@app.route('/results')
def results():
    query = request.args.get('query').lower()
    index = -1
    for i in range(len(df)):
        if df["Product"][i] == quer:
            print(i)
            index = i
    
    if index == -1:
        results = "Item not found"
    else:
        results = df["Impact"][index]
    
    return render_template("results.html", query=query, results=results)


if __name__ == "__main__":
    app.run(debug=True)
