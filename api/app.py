from flask import Flask, render_template

app = Flask(__name__)

members = [
    {
        "name": "Member One",
        "role": "Chair",
        "image": "https://via.placeholder.com/150",
        "linkedin": "#"
    },
    {
        "name": "Member Two",
        "role": "Vice Chair",
        "image": "https://via.placeholder.com/150",
        "linkedin": "#"
    },
    {
        "name": "Member Three",
        "role": "Secretary",
        "image": "https://via.placeholder.com/150",
        "linkedin": "#"
    }
]

@app.route("/")
def home():
    return render_template("index.html", members=members)

if __name__ == "__main__":
    app.run(debug=True)