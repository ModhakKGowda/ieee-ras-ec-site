from flask import Flask, render_template, Response

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/sitemap.xml')
def sitemap():
    xml_content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url>\n'
        '    <loc>https://ieee-ras-pesu-ec.vercel.app/</loc>\n'
        '    <lastmod>2026-07-20</lastmod>\n'
        '    <changefreq>weekly</changefreq>\n'
        '    <priority>1.0</priority>\n'
        '  </url>\n'
        '  <url>\n'
        '    <loc>https://ieee-ras-pesu-ec.vercel.app/about</loc>\n'
        '    <lastmod>2026-07-20</lastmod>\n'
        '    <changefreq>monthly</changefreq>\n'
        '    <priority>0.8</priority>\n'
        '  </url>\n'
        '  <url>\n'
        '    <loc>https://ieee-ras-pesu-ec.vercel.app/events</loc>\n'
        '    <lastmod>2026-07-20</lastmod>\n'
        '    <changefreq>weekly</changefreq>\n'
        '    <priority>0.8</priority>\n'
        '  </url>\n'
        '</urlset>'
    )
    return Response(xml_content, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True)
