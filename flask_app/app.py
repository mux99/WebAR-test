#!/app/venv/bin/python3

from flask import Flask, request, render_template, send_from_directory
from subprocess import check_output
import os

app = Flask(__name__)

print(app.root_path)
print(app.has_static_folder)
print(app.static_folder)
import os
names = os.listdir(os.path.join(app.static_folder))
print(names) # list of static files

@app.errorhandler(404)
def page_not_found(error):
    # Render a custom 404 template
    return render_template('404.html'), 404

@app.route("/")
def landing_page():
    return render_template('index.html')

@app.route("/exemple")
def exemple_page():
    return render_template('exemple.html')

if __name__ == "__main__":
    app.run(host="::", port=4000, debug=True, ssl_context='adhoc')
