from flask import Flask, render_template, request

app = Flask(__name__)

story_templates = {
    "1": "It was a {adjective1} November day. {name} woke up to the {adjective2} smell of {bird1} roasting in the {location1}.",
    "2": "Today {name} went to the zoo. {name} saw a(n) {adjective1} {animal1} jumping up and down in its tree. It {adverb1} {verb1} through the large tunnel that led to its {bodypart1}.",
    "3": "My family is very {adjective1}. Every {time1}, {name} and my family {verb1} together at the {place1}."
}

@app.route("/")
def index():
    return render_template("index.html", templates=story_templates)

@app.route("/story/<story_id>", methods=["GET", "POST"])
def story_form(story_id):
    if request.method == "POST":
        user_inputs = request.form.to_dict()
        story = story_templates[story_id].format(**user_inputs)
        return render_template("story_result.html", story=story)
    return render_template("story_form.html", story_id=story_id)

if __name__ == "__main__":
    app.run(debug=True)
