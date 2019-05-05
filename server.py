import os
import base64

import flask
import jinja2

app = flask.Flask('hackme')
here = os.path.dirname(os.path.realpath(__file__))

app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([os.path.join(here, 'templates')])
])

THE_PASSWORD = base64.b64decode('YmxhY2toYXdrcwo=').decode().strip()


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if flask.request.method == 'POST':
        guess = flask.request.form.get('password')

        if not guess:
            error = 'What?  You didn\'t guess a password!'
        elif guess == THE_PASSWORD:
            return flask.redirect(flask.url_for('success'))
        else:
            error = f'Sorry, but \"{guess}\" is not the password!'

    return flask.render_template('login.html', error=error)


@app.route('/success/', methods=['GET'])
def success():
    return flask.render_template('success.html', correct=THE_PASSWORD)


if __name__ == '__main__':
    app.run()
