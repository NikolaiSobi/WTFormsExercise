from models import *
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name="Mindy", species="dog", photo_url="https://soranews24.com/wp-content/uploads/sites/3/2013/10/shiba10.jpg", age=2, notes="hyper")
db.session.add(pet1)
db.session.commit()