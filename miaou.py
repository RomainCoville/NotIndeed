#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_pymongo import PyMongo
from flask import flash, render_template, request, redirect
from forms import JobSearchForm

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["MONGO_URI"] = "mongodb://localhost:27017/Indeed"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def accueil():
    search = JobSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    else:
        return render_template('accueil.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    results = mongo.db.SearchedJobStats.find_one({"_id":search_string})

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)

@app.route('/date')
def date():
    d = mongo.db.SearchedJobStats.find_one({"_id":"data"})
    return render_template('date.html', la_date=d)


if __name__ == '__main__':
    app.run(debug=True)
#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def accueil():
    mots = ["Grosse Bite", "a", "toi,", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)

@app.route('/date')
def date():
    d =  "a"
    return render_template('date.html', la_date=d)


if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
