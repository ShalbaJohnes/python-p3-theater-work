from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    auditions = relationship('Audition', back_populates='role', cascade="all, delete-orphan")

    @property
    def actors(self):
        return [aud.actor for aud in self.auditions]

    @property
    def locations(self):
        return [aud.location for aud in self.auditions]

    def lead(self):
        hired_actors = [a for a in self.auditions if a.hired]
        return hired_actors[0].actor if len(hired_actors) > 0 else 'no actor has been hired for this role'

    def understudy(self):
        hired_actors = [a for a in self.auditions if a.hired]
        return hired_actors[1].actor if len(hired_actors) > 1 else 'no actor has been hired for understudy for this role'


class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        self.hired = True
