from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def watch():
    video = request.args.get("video")
    return render_template("watch.html", video=video)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)