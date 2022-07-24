from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases/migraines/migraines.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


###########
# Tables  #
###########
class Migraine(Base):
    __tablename__ = 'migraines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    start = Column(DateTime(timezone=True), nullable=False)
    stop = Column(DateTime(timezone=True))
    intensity = Column(Integer)
    medication = Column(String)
    reason = Column(String)
    notes = Column(String)


############
# Queries  #
############
def get_all_migraines():
    return session.query(Migraine).all()


def get_migraine_by_id(migraine_id):
    return session.query(Migraine).filter(Migraine.id == migraine_id).first()


def insert_new_migraine(migraine_json):
    migraine = Migraine(start=migraine_json['start'],
                        stop=migraine_json['stop'],
                        intensity=migraine_json['intensity'],
                        medication=migraine_json['medication'],
                        reason=migraine_json['reason'],
                        notes=migraine_json['notes'])
    session.add(migraine)
    session.commit()


def update_migraine_by_id(migraine_id, migraine_json):
    session.query(Migraine).filter(Migraine.id == migraine_id).update(
        {
            'start': migraine_json['start'],
            'stop': migraine_json['stop'],
            'intensity': migraine_json['intensity'],
            'medication': migraine_json['medication'],
            'reason': migraine_json['reason'],
            'notes': migraine_json['notes']
        }, synchronize_session=False)
    session.commit()


def delete_migraine_by_id(migraine_id):
    session.query(Migraine).filter(Migraine.id == migraine_id).delete()
    session.commit()
