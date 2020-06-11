from urllib.parse import urljoin
from flask import Flask, render_template, request, redirect, url_for
from url_shortened_utils import create_db, get_shorten_url, get_origin_url

app = Flask(__name__)
create_db()


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", origin_url="", message="")


@app.route('/', methods=['POST'])
def change():
    origin_url = request.form['url']
    shorten_url = urljoin(request.url_root, url_for('convert', url=get_shorten_url(origin_url)))
    return render_template("home.html", origin_url=origin_url, message=shorten_url)


@app.route('/convert/<url>')
def convert(url):
    origin_url = get_origin_url(url)
    return redirect(origin_url)


if __name__ == "__main__":
    app.run(debug=True)
