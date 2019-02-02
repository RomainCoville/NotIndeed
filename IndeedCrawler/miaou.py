#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
#from flask_pymongo import PyMongo
from flask import render_template
app = Flask(__name__)


@app.route('/')
def accueil():
    mots = ["bonjour", "a", "toi,", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)

@app.route('/date')
def date():
    d =  "a"
    return render_template('date.html', la_date=d)


if __name__ == '__main__':
    app.run(debug=True)
