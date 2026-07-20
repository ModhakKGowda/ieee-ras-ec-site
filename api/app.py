from flask import Flask, render_template
from flask import Response

@app.route('/sitemap.xml')
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>https://your-app-name.vercel.app/</loc>
        <lastmod>2026-07-20</lastmod>
        <priority>1.0</priority>
      </url>
    </urlset>"""
    return Response(xml, mimetype='text/xml')

app = Flask(__name__)

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

# The dedicated game page route
@app.route('/sandbox')
def sandbox():
    return render_template('sandbox.html')

if __name__ == '__main__':
    app.run(debug=True)
