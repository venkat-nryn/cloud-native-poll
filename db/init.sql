-- Create a table to store poll options and their vote counts
CREATE TABLE polls (
  id SERIAL PRIMARY KEY,
  option_name VARCHAR(255) UNIQUE NOT NULL,
  votes INT NOT NULL DEFAULT 0
);

-- Insert the initial options for our poll
INSERT INTO polls (option_name) VALUES ('Python'), ('JavaScript'), ('Go');