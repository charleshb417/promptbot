from config import *
import random

class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return '<Field %r>' % self.name

    def random_value(self):
        if len(self.values) > 0:
            return random.choice(self.values).value
        else:
            return ''

class FieldValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(1024), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    field = db.relationship('Field', backref=db.backref('values', lazy=True))

    def __repr__(self):
        return '<Field %r>' % self.value

db.create_all()
