from flask import Flask, redirect, render_template, request, flash, url_for
from flask_bootstrap import Bootstrap
from scripts import forms
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig


# change to ProductionConfig or DevelopmentConfig
ENVIRONMENT = ProductionConfig

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(ENVIRONMENT)
db = SQLAlchemy(app)
db.drop_all()
db.create_all()


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75))
    description = db.Column(db.String(75))
    client = db.Column(db.String(10))
    priority = db.Column(db.Integer)
    date = db.Column(db.DATE)
    area = db.Column(db.String(80))

    def __repr__(self):
        return self.title


# saves form data to database
def save_changes(feature, form):
    feature.title = form.title.data
    feature.description = form.description.data
    feature.client = form.client.data
    feature.priority = int(form.priority.data)
    feature.date = form.date.data
    feature.area = ', '.join(form.area.data)

    db.session.add(feature)
    db.session.commit()


# -------- Home route -------#
@app.route('/', methods=['GET'])
def home():
    all_features = Feature.query.order_by(Feature.client).all()
    return render_template('home.html', features=all_features)


# -------  Create Feature route ---- #
@app.route('/feature', methods=['GET', 'POST'])
def feature():
    form = forms.RequestForm(request.form)
    if request.method == 'POST' and form.validate():
        feature = Feature()
        save_changes(feature, form)
        flash('Feature Successfully Added!')
        return redirect(url_for('home'))
    return render_template('feature.html', form=form)


# ------ Error Handlers ------- #
@app.errorhandler(404)
def pagenotfound(e):
    return render_template('pagenotfound.html'), 404


@app.errorhandler(500)
def pagenotfound500(e):
    return render_template('pagenotfound.html'), 500

# ========= MAIN ======= #
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, use_reloader=True)
