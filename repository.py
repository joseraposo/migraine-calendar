import sqlite3
import json

schema_file = 'databases/migraines/schema.sql'
database_file = 'databases/migraines/migraines.db'


def init_db():
    with open(schema_file) as f:
        with DBCursor(database_file) as cursor:
            cursor.executescript(f.read())


def insert_new_migraine(migraine_json):
    with DBCursor(database_file) as cursor:
        cursor.execute('''INSERT INTO migraines (start, stop, intensity, medication, reason, notes) 
                          VALUES (:start, :stop, :intensity, :medication, :reason, :notes)''', migraine_json)


def update_migraine_by_id(migraine_id, migraine_json):
    with DBCursor(database_file) as cursor:
        cursor.execute('''UPDATE migraines 
                            SET start = ?,
                                stop = ?, 
                                intensity = ?, 
                                medication = ?, 
                                reason = ?, 
                                notes =?
                            WHERE id = ?''', (migraine_json['start'],
                                              migraine_json['stop'],
                                              migraine_json['intensity'],
                                              migraine_json['medication'],
                                              migraine_json['reason'],
                                              migraine_json['notes'],
                                              migraine_id))


def get_all_migraines():
    with DBCursor(database_file) as cursor:
        cursor.execute('SELECT * FROM migraines')
        data = cursor.fetchall()
        return json.dumps(data)


def get_migraine_by_id(migraine_id):
    with DBCursor(database_file) as cursor:
        cursor.execute('SELECT * FROM migraines where id=?', migraine_id)
        data = cursor.fetchall()
        return json.dumps(data)


def delete_migraine_by_id(migraine_id):
    with DBCursor(database_file) as cursor:
        cursor.execute('DELETE FROM migraines WHERE id=?', migraine_id)


class DBCursor:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        self.cur = self.connection.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

