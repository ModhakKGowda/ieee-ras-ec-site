from flask import Flask, render_template, Response

@app.route('/sitemap.xml')
def sitemap():
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url>\n'
        '    <loc>https://ieee-ras-pesu-ec.vercel.app/</loc>\n'
        '    <lastmod>2026-07-20</lastmod>\n'
        '    <changefreq>weekly</changefreq>\n'
        '    <priority>1.0</priority>\n'
        '  </url>\n'
        '</urlset>'
    )
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
