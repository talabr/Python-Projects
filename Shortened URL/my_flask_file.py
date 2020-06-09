from flask import Flask, render_template, request, redirect, url_for
from url_shortened_utils import get_new_url, get_origin_url_form_shorten_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", origin_url="", shorten_url="")


@app.route('/change', methods=['POST'])
def change():
	origin_url = request.form['url']
	shorten_url = request.url_root + get_new_url(origin_url)
	return render_template("home.html", origin_url=origin_url, shorten_url=shorten_url)


@app.route('/<url>')
def convert(url):
	origin_url = get_origin_url_form_shorten_url(url)
	return redirect(origin_url)


if __name__ == "__main__":
    app.run(debug=True)