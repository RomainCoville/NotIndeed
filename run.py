#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_pymongo import PyMongo
from flask import flash, render_template, request, redirect
from forms import JobSearchForm
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["MONGO_URI"] = "mongodb://mongo:27017/Indeed"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def accueil():
    search = JobSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    else:
        return render_template('accueil.html',form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = '^JobCards_' + search.data['search']
    stats_search_String = 'Stats_' + search.data['search']

    jobStats = mongo.db.Job.find_one({"_id": stats_search_String})

    if jobStats:
        salariesList = jobStats['salaryItem']['salaries']
        salariesCount = jobStats['salaryItem']['salariescount']

        jobTypesList = jobStats['jobTypeItem']['jobtypes']
        jobTypesCount = jobStats['jobTypeItem']['jobtypescount']

        locationsList = jobStats['locationItem']['locations']
        locationsCount = jobStats['locationItem']['locationscount']

        data = [go.Bar(
                x=salariesList,
                y=salariesCount
        )]
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        data2 = [go.Bar(
                x=jobTypesList,
                y=jobTypesCount
        )]
        graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    jobCards = mongo.db.Job.find({"_id":{'$regex' : search_string}})
    alljobcards = []
    for jobCard in jobCards:
        alljobcards+=jobCard["jobCardsList"]

    if not jobStats or not jobCards or not search.data['search']:
        flash('No results found! Type another job maybe you will have more luck next time.')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', form = search, jobcards=alljobcards, graphJSON=graphJSON, graphJSON2=graphJSON2)

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
