CREATE TABLE users(
	users_id SERIAL PRIMARY KEY,
	username VARCHAR(64) NOT NULL,
	password TEXT NOT NULL,
	first_name VARCHAR(64) ,
	last_name VARCHAR(64),
	email VARCHAR(64),
	phone varchar(16),
	created_at TIMESTAMP DEFAULT NOW(),
	last_login TIMESTAMP ,
	have_telegram BOOLEAN DEFAULT FALSE,
	is_archive BOOLEAN DEFAULT FALSE,
	UNIQUE (username, email, phone));

CREATE UNIQUE INDEX ON USERS(users_id);