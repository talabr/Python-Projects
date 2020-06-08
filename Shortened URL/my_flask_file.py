from flask import Flask, render_template
from url_shortened_utils import get_new_url, get_origin_url_form_shorten_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/change/<url>')
def change(url):
	return get_new_url(url)


@app.route('/convert/<url>')
def convert(url):
	return get_origin_url_form_shorten_url(url)


if __name__ == "__main__":
    app.run(debug=True)