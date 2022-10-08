from sqlalchemy import Column, Integer, String, DateTime, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from migraine_calendar import db

#
# engine = create_engine('sqlite:///../databases/migraines.db', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()


###########
# Tables  #
###########
class Migraine(db.Model):
    __tablename__ = 'migraines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.utcnow)
    start = Column(DateTime, nullable=False)
    stop = Column(DateTime)
    intensity = Column(Integer)
    medication = Column(String)
    reason = Column(String)
    notes = Column(String)

    def __repr__(self):
        return f"Migraine(id:{self.id}, started:{self.start}, stopped:{self.stop}, intensity:{self.intensity})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Sleep(db.Model):
    __tablename__ = 'sleep'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.utcnow)
    start = Column(DateTime, nullable=False)
    stop = Column(DateTime)
    light_min = Column(Integer)
    deep_min = Column(Integer)
    rem_min = Column(Integer)
    awake_min = Column(Integer)
    feeling = Column(String)
    notes = Column(String)

    def __repr__(self):
        return f"Sleep(id:{self.id}, sleep_date:{self.sleep_date}, started:{self.start}, stopped:{self.stop})"


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.utcnow)
    name = Column(String)
    password_hash = Column(String)


############
# Queries  #
############

# Migraine
########
def get_all_migraines():
    return db.session.query(Migraine).all()


def get_migraine_by_id(migraine_id):
    return db.session.query(Migraine).filter(Migraine.id == migraine_id).first()


def insert_new_migraine(migraine_json):
    date_format = '%Y-%m-%d'

    migraine = Migraine(start=datetime.strptime(migraine_json['start'], date_format),
                        stop=datetime.strptime(migraine_json['stop'], date_format),
                        intensity=migraine_json['intensity'],
                        medication=migraine_json['medication'],
                        reason=migraine_json['reason'],
                        notes=migraine_json['notes'])
    db.session.add(migraine)
    db.session.commit()


def update_migraine_by_id(migraine_id, migraine_json):
    date_format = '%Y-%m-%d'

    migraine = db.session.query(Migraine).filter(Migraine.id == migraine_id).first()

    if 'start' in migraine_json:
        migraine.start = datetime.strptime(migraine_json['start'], date_format)
    if 'stop' in migraine_json:
        migraine.stop = datetime.strptime(migraine_json['stop'], date_format)
    if 'intensity' in migraine_json:
        migraine.intensity = migraine_json['intensity']
    if 'medication' in migraine_json:
        migraine.medication = migraine_json['medication']
    if 'reason' in migraine_json:
        migraine.reason = migraine_json['reason']
    if 'notes' in migraine_json:
        migraine.notes = migraine_json['notes']

    # db.session.query(Migraine).filter(Migraine.id == migraine_id).update(migraine, synchronize_session=False)
    db.session.commit()


def delete_migraine_by_id(migraine_id):
    db.session.query(Migraine).filter(Migraine.id == migraine_id).delete()
    db.session.commit()


# Sleep
########
def get_all_sleeps():
    return db.session.query(Sleep).all()


def get_sleep_by_id(sleep_id):
    return db.session.query(Sleep).filter(Sleep.id == sleep_id).first()


def insert_new_sleep(sleep_json):
    date_format = '%Y-%m-%d'

    sleep = Sleep(start=datetime.strptime(sleep_json['start'], date_format),
                  stop=datetime.strptime(sleep_json['stop'], date_format),
                  light_min=sleep_json['light_min'],
                  deep_min=sleep_json['deep_min'],
                  rem_min=sleep_json['rem_min'],
                  awake_min=sleep_json['awake_min'],
                  feeling=sleep_json['feeling'],
                  notes=sleep_json['notes'])
    db.session.add(sleep)
    db.session.commit()


def update_sleep_by_id(sleep_id, sleep_json):
    date_format = '%Y-%m-%d'

    sleep = db.session.query(Sleep).filter(Sleep.id == sleep_id).first()

    if 'start' in sleep_json:
        sleep.start = datetime.strptime(sleep_json['start'], date_format)
    if 'stop' in sleep_json:
        sleep.stop = datetime.strptime(sleep_json['stop'], date_format)
    if 'light_min' in sleep_json:
        sleep.light_min = sleep_json['light_min']
    if 'deep_min' in sleep_json:
        sleep.deep_min = sleep_json['deep_min']
    if 'rem_min' in sleep_json:
        sleep.rem_min = sleep_json['rem_min']
    if 'feeling' in sleep_json:
        sleep.feeling = sleep_json['feeling']
    if 'notes' in sleep_json:
        sleep.notes = sleep_json['notes']

    # db.session.query(Migraine).filter(Migraine.id == migraine_id).update(migraine, synchronize_session=False)
    db.session.commit()


def delete_sleep_by_id(sleep_id):
    db.session.query(Sleep).filter(Sleep.id == sleep_id).delete()
    db.session.commit()


# User
########
def add_new_user(user_json):
    date_format = '%Y-%m-%d'

    user = User(name=user_json['name'],
                password_hash=user_json['password_hash'])
    db.session.add(user)
    db.session.commit()
