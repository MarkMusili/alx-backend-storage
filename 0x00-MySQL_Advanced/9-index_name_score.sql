-- A SQL script that creates an index idx_name_first on the table names and the first letter of name and score
-- Index implimentation
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
