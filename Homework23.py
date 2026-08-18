from flask import Flask, render_template, request, redirect

app = Flask(__name__)

events = []
next_id = 1

@app.route("/")
def index():
    return render_template("index.html", events=events)

@app.route("/add", methods=["POST"])
def add_event():
    global next_id

    title = request.form.get("title")
    date = request.form.get("date")
    description = request.form.get("description")

    if title and date:
        events.append({
            "id": next_id,
            "title": title,
            "date": date,
            "description": description
        })
        next_id += 1

    return redirect("/")

@app.route("/delete/<int:event_id>", methods=["POST"])
def delete_event(event_id):
    global events

    events = [
        event
        for event in events
        if event["id"] != event_id
    ]

    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)