"""
Kazu Umemoto's Flask API.
"""

from flask import Flask, render_template, send_from_directory, request, abort

app = Flask(__name__)

@app.route("/<path:page>")
def open(page):
    if ('//' in page) or ('~' in page) or ('..' in page):
        abort(403)
    return send_from_directory('pages')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def file_forbidden(e):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
