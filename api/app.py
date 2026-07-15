from flask import Flask, render_template
# Import the isolated sandbox blueprint
from blueprints.sandbox import sandbox_bp

app = Flask(__name__)
app.secret_key = "ieee_ras_secret_key_session_handler"  # Required to keep track of high scores

# Register the Sandbox Blueprint
app.register_blueprint(sandbox_bp)

# --- Primary Website Page Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)
