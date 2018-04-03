from config import *
from flask import redirect, render_template
from models import *
from forms import *

'''
    Endpoints
'''
@app.route("/")
def index():
    return render_template('index.html', fields = Field.query.all() )

@app.route('/fields', methods=['GET', 'POST'])
def fields():
    form = FieldForm()
    if form.validate_on_submit():
        field = Field(name=form.name.data)
        db.session.add(field)
        db.session.commit()
        return redirect('/')
    return render_template('create_field.html', title='Create Field', form=form)

@app.route('/fieldvalues', methods=['GET', 'POST'])
def values():
    form = FieldValueForm()
    form.field.choices = [(f.id, f.name) for f in Field.query.all()]
    # Validators broken for some reason, TODO figure out why?
    if form.field.data is not None and form.value.data is not None:
        try:
            value = FieldValue(field_id=int(form.field.data), value=form.value.data)
            db.session.add(value)
            db.session.commit()
            return redirect('/')
        except:
            return render_template('create_field_value.html', title='Create Field Value', form=form)
    return render_template('create_field_value.html', title='Create Field Value', form=form)

if __name__ == '__main__':
   app.run()