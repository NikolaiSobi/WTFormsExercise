from flask import Flask, request, redirect, render_template
from models import *
from forms import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret159"

app.app_context().push()

connect_db(app)

@app.route('/')
def list_pets():
    """list of pets"""

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        if form.photo_url.data != "":
            photo_url = form.photo_url.data
        else:
            photo_url = "https://t4.ftcdn.net/jpg/06/20/95/53/360_F_620955397_sqXk8IzGzvqOfvQddznWjND2T5PC44VO.jpg"
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    return render_template('add_pet_form.html', form=form)

@app.route('/pet/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form)