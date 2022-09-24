CREATE TABLE IF NOT EXISTS migraines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    start TIMESTAMP NOT NULL,
    stop TIMESTAMP,
    intensity INTEGER,
    medication TEXT,
    reason TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS sleep (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sleep_date TIMESTAMP NOT NULL,
    start TIMESTAMP NOT NULL,
    stop TIMESTAMP,
    light_min INTEGER,
    deep_min INTEGER,
    rem_min INTEGER,
    awake_min INTEGER,
    feeling TEXT,
    notes TEXT
);