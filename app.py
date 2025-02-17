from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["query"]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )["choices"][0]["message"]["content"]
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
