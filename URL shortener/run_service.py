from urllib.parse import urljoin
from flask import Flask, render_template, request, redirect, url_for
from utils import get_short_url, get_user_url_by_short_url
from data_access_manager import create_urls_db
app = Flask(__name__)
create_urls_db()


@app.route('/')
def home():
    return render_template("home.html", origin_url="", message="")


@app.route('/', methods=['POST'])
def change():
    origin_url = request.form['url']
    custom_url = request.form.get('custom_url')
    short_url_after_check = get_short_url(origin_url, custom_url)  # returns error string or random string
    if short_url_after_check.startswith('ERROR '):
        return render_template("home.html", origin_url=origin_url, message=short_url_after_check)
    full_short_url = urljoin(request.url_root, url_for('convert', url=short_url_after_check))
    return render_template("home.html", origin_url=origin_url, message=full_short_url)


@app.route('/convert/<url>')
def convert(url):
    origin_url = get_user_url_by_short_url(url)
    return redirect(origin_url)


if __name__ == "__main__":
    app.run(debug=True)
