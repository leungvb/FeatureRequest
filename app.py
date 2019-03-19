from flask import Flask, redirect, url_for, render_template, request, session
from flask_bootstrap import Bootstrap
from scripts import forms


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'thisisasecret'

# -------- Home route -------#
@app.route('/', methods=['GET'])
def home():
    users=['User 1','User 2','User 3']

    return render_template('home.html', users=users)

# -------  Create Feature route ---- #

@app.route('/feature', methods=['GET','POST'])
def feature():
    form = forms.RequestForm()
    return render_template('feature.html', form=form)

# ========= MAIN ======= #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
