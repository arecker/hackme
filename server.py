import flask

app = flask.Flask('hackme')

THE_PASSWORD = 'chicagoblackhawks'


@app.route('/', methods=['GET', 'POST'])
def login():
    data = {}
    if flask.request.method == 'POST':
        guess = flask.request.form.get('password', '')

        if guess == THE_PASSWORD:
            return flask.redirect(flask.url_for('success'))

        return 'INCORRECT'

    return flask.render_template('login.html')


@app.route('/success/', methods=['GET'])
def success():
    return flask.render_template('success.html', correct=THE_PASSWORD)


if __name__ == '__main__':
    app.run()
