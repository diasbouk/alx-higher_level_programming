-- Creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXIST second_table (
	id int,
	name varchar(256),
	score int
);

-- Creates new records

INSERT INTO second_table (id, name, values) VALUES(1, 'Jhon', 10);
INSERT INTO second_table (id, name, values) VALUES(2, 'Alex', 3);
INSERT INTO second_table (id, name, values) VALUES(3,'Bob', 14);
INSERT INTO second_table (id, name, values) VALUES(4,'George', 8);
