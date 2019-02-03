# forms.py
 
from wtforms import Form, StringField, SelectField
 
class JobSearchForm(Form):
    search = StringField('')

