from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_bootstrap import Bootstrap
from scripts import forms
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
Bootstrap(app)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+ os.path.join(BASE_DIR, 'feature.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'
db= SQLAlchemy(app)


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75))
    description =db.Column(db.String(75))

    def __repr__(self):
        return self.title

db.drop_all()
db.create_all()  

# saves form data to database
def save_changes(feature, form):
    feature.title = form.title.data
    feature.description = form.description.data
    db.session.add(feature)
    db.session.commit()


# -------- Home route -------#
@app.route('/', methods=['GET'])
def home():
    users=['User 1','User 2','User 3']
    all_features = Feature.query.all()
    print(all_features)
    print(type(all_features))

    return render_template('home.html', users=users, features=all_features)

# -------  Create Feature route ---- #

@app.route('/feature', methods=['GET','POST'])
def feature():
    form = forms.RequestForm(request.form)
    if request.method == 'POST' and form.validate():
        print('that was a post request')
        print(form.title.data)
        feature=Feature()
        
        save_changes(feature, form)
        flash('Feature Successfully Added!')
        return redirect('/')        # change this to url_for
    return render_template('feature.html', form=form)

# ========= MAIN ======= #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
