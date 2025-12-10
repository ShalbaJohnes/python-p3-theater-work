from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Role

engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

# Get Hamlet role
hamlet_role = session.query(Role).filter_by(character_name="Hamlet").first()

if hamlet_role:
    print("Actors:", hamlet_role.actors)
    print("Locations:", hamlet_role.locations)

    # Hire first audition
    if hamlet_role.auditions:
        first_audition = hamlet_role.auditions[0]
        first_audition.call_back()
        session.commit()

    print("Lead:", hamlet_role.lead())
    print("Understudy:", hamlet_role.understudy())
else:
    print("No role named Hamlet found.")
