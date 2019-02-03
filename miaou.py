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
    search_string = '^JobCards_' + search.data['search']

    allJobCards = mongo.db.Job.find_one({"_id":{'$regex' : search_string}})

    if not allJobCards or not search.data['search']:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        jobcards = allJobCards["jobCardsList"]
        return render_template('results.html', form = search, jobcards=jobcards)

@app.route('/date')
def date():
    d = mongo.db.SearchedJobStats.find_one({"_id":"data"})
    return render_template('date.html', la_date=d)

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
