from urllib.parse import urljoin
from flask import Flask, render_template, request, redirect, url_for
from url_shortened_utils import create_db, get_shorten_url, get_origin_url, custom_url

app = Flask(__name__)
create_db()


@app.route('/')
def home():
    return render_template("home.html", origin_url="", message="")


@app.route('/', methods=['POST'])
def change():
    origin_url = request.form['url']
    print("received original url %s" % origin_url)
    # try:
    if request.form.get('check_custom'):
        # request.form["check_custom"]  # checks whether the checkbox is empty or not
        user_url = request.form['custom_url']
        user_url_after_check = custom_url(origin_url, user_url)  # returns error string or random string
        if user_url_after_check.startswith('ERROR '):
            return render_template("home.html", origin_url=origin_url, message=user_url_after_check)
        else:
            full_custom_url = urljoin(request.url_root, url_for('convert', url=user_url_after_check))
            return render_template("home.html", origin_url=origin_url, message=full_custom_url)
    # except:
    else:
        shorten_url_after_check = get_shorten_url(origin_url)  # returns error string or random string
        if shorten_url_after_check.startswith('ERROR '):
            return render_template("home.html", origin_url=origin_url, message=shorten_url_after_check)
        else:
            full_shorten_url = urljoin(request.url_root, url_for('convert', url=shorten_url_after_check))
            return render_template("home.html", origin_url=origin_url, message=full_shorten_url)


# def check_input(origin_url, user_url=None, is_custome=False):
# 	if is_custome:
# 		url = custom_url(origin_url, user_url)
# 	else:
# 		url = get_shorten_url(origin_url)
# 	if url.startswith('ERROR '):
# 		return url
# 	return urljoin(request.url_root, url_for('convert', url))


@app.route('/convert/<url>')
def convert(url):
    origin_url = get_origin_url(url)
    return redirect(origin_url)


if __name__ == "__main__":
    app.run(debug=True)
