import os

import flask
import jinja2

app = flask.Flask('hackme')
here = os.path.dirname(os.path.realpath(__file__))

app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([os.path.join(here, 'templates')])
])

THE_PASSWORD = 'blackhawks'


@app.route('/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        guess = flask.request.form.get('password')

        if not guess:
            return '"password" required'

        if guess == THE_PASSWORD:
            return flask.redirect(flask.url_for('success'))

        return 'INCORRECT'

    return flask.render_template('login.html')


@app.route('/success/', methods=['GET'])
def success():
    return flask.render_template('success.html', correct=THE_PASSWORD)


if __name__ == '__main__':
    app.run()
