from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CVForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    profession = StringField('Profesión', validators=[DataRequired()])
    experience = TextAreaField('Experiencia', validators=[DataRequired()])
    education = TextAreaField('Educación', validators=[DataRequired()])
    skills = TextAreaField('Habilidades', validators=[DataRequired()])
    submit = SubmitField('Generar Portfolio')
 
