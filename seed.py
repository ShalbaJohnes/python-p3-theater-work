from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Role, Audition

engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create roles
hamlet = Role(character_name="Hamlet")
ophelia = Role(character_name="Ophelia")

session.add_all([hamlet, ophelia])
session.commit()

# Add auditions
aud1 = Audition(actor="Alice", location="London", phone=1234567890, role=hamlet)
aud2 = Audition(actor="Bob", location="Paris", phone=2345678901, role=hamlet)
aud3 = Audition(actor="Clara", location="Berlin", phone=3456789012, role=ophelia)

session.add_all([aud1, aud2, aud3])
session.commit()

print("Seed data added!")
