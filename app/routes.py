from flask import Blueprint, render_template
from .forms import CVForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = CVForm()
    if form.validate_on_submit():
        name = form.name.data
        profession = form.profession.data
        experience = form.experience.data
        education = form.education.data
        skills = form.skills.data

        return render_template('portfolio.html', name=name, profession=profession, experience=experience, education=education, skills=skills)

    return render_template('index.html', form=form)
