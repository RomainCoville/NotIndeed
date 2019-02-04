# forms.py

from wtforms import Form, StringField, SelectField

class JobSearchForm(Form):
    search = StringField('', render_kw={"placeholder": "Métier, entreprise ou lieu..."})
