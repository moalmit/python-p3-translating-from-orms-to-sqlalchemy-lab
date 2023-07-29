from sqlalchemy import create_engine
from models import Dog

engine = create_engine('sqlite:///:memory:')

def create_table(base, engine):
    base.metadata.create_all(engine)
    return engine
    
def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def get_all(session):
    all = session.query(Dog).all()
    return [dog for dog in all]

def find_by_name(session, name):
    row = session.query(Dog).filter_by(name=name).first()
    return row

def find_by_id(session, id):
    row = session.query(Dog).filter_by(id=id).first()
    return row

def find_by_name_and_breed(session, name, breed):
    row = session.query(Dog).filter_by(name=name, breed=breed).first()
    return row

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    return session