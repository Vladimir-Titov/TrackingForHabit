CREATE TABLE users
(
    user_id       SERIAL PRIMARY KEY,
    username      VARCHAR(64) NOT NULL,
    password      TEXT        NOT NULL,
    first_name    VARCHAR(64),
    last_name     VARCHAR(64),
    email         VARCHAR(64),
    phone         varchar(16),
    created_at    TIMESTAMP DEFAULT NOW(),
    have_telegram BOOLEAN   DEFAULT FALSE,
    is_archive    BOOLEAN   DEFAULT FALSE,
    UNIQUE (username),
    UNIQUE (phone),
    UNIQUE (email)
);

CREATE UNIQUE INDEX ON USERS (user_id);

CREATE TABLE habits
(
    habit_id    SERIAL PRIMARY KEY,
    name        VARCHAR(64) NOT NULL,
    description TEXT NOT NULL,
    user_id     INTEGER NOT NULL,
    is_archive  BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

CREATE UNIQUE INDEX ON habits (habit_id);