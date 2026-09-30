from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"{source}|{target}"
        }

        response = requests.get(url, params=params)
        data = response.json()

        translated_text = data["responseData"]["translatedText"]

    return render_template(
        "index.html",
        translated_text=translated_text
    )


if __name__ == "__main__":
    app.run(debug=True)