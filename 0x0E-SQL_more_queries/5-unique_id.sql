-- Creates the table unique_id on our MySQL server
-- id must be unique and has default value 1
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
