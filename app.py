from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)


@app.route('/')
def page_image():
    return render_template("index.html")

@app.route('/new_page')
def new_page():
    return render_template("add.html")

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('new_page'))

@app.route('/start_page')
def start_page():
    return render_template("start.html")


@app.route('/redirect_start')
def redirect_start():
    return redirect(url_for('start_page'))

@app.route('/contact_page')
def contact_page():
    return render_template("contact.html")


@app.route('/contact_redirect')
def contact_redirect():
    return redirect(url_for('contact_page'))



@app.route('/back')
def go_back():
    return redirect(url_for('page_image'))



if __name__ == '__main__':
    app.run()
