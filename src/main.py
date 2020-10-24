from flask import Flask, render_template, request, redirect
from scrapperReddit import get_subreddits
from scrapperJobs import get_jobs
from exporter import save_to_file


app = Flask("DayEleven", template_folder="./src/templates")

db = {}

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django",
]


@app.route("/")
def index():
    try:
        return render_template("home.html", subreddits=subreddits)
    except IOError:
        return redirect("/")


@app.route("/reddit")
def read():
    subreddits = []
    try:
        aggregated_subreddits_dict = request.args.to_dict()
        subreddits = get_subreddits(aggregated_subreddits_dict)
        return render_template("reddit.html", subreddits=subreddits)
    except IOError:
        return redirect("/")


@app.route("/search")
def jobs():
    word = request.args.get("term")
    if word:
        word = word.lower()
        if word in db:
            jobs = db[word]
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "search.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)

        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return redirect("/")
    except:
        print("error")
        return redirect("/")


app.run(host="127.0.0.1")