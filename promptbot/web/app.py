from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

'''
    Database Models
'''
class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return '<Field %r>' % self.name

class FieldValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(1024), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    field = db.relationship('Field', backref=db.backref('values', lazy=True))

    def __repr__(self):
        return '<Field %r>' % self.value
'''
    Endpoints
'''
@app.route("/")
def hello():
    return "To do!"

if __name__ == '__main__':
   db.create_all()
   app.run()