from flask import Flask, url_for, request, render_template, Blueprint, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/search', methods=['POST', 'GET'])
def search():
    query = request.form['query']
    return redirect('/results?query=' + query)


@app.route('/results')
def results():
    query = request.args.get('query')
    return render_template("results.html", query=query)


if __name__ == "__main__":
    app.run(debug=True)
