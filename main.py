import utils
from flask import Flask, render_template

app = Flask(__name__)


# создаём роут "/" для вывода всех профилей
@app.route('/')
def hello():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


# создаём роут "candidates/" для поиска по id
@app.route("/candidate/<int:id>")
def show_user_profile(id):
    candidate = utils.get_candidate(id)
    return render_template('single.html', candidate=candidate)


# создаём роут "search/" для поиска по имени
@app.route("/search/<candidate_name>")
def show_candidates_by_name(candidate_name):
    candidates_by_name = utils.get_candidates_by_name(candidate_name)
    candidates_counter = len(candidates_by_name)
    return render_template('search.html', candidates_by_name=candidates_by_name, candidates_counter=candidates_counter)


# создаём роут "skill/" для поиска по скиллам
@app.route("/skill/<skill_name>")
def show_candidates_by_skill(skill_name):
    candidates_by_skill = utils.get_candidates_by_skill(skill_name)
    candidates_counter = len(candidates_by_skill)
    return render_template('skill.html', candidates_by_skill=candidates_by_skill, candidates_counter=candidates_counter)


app.run()
