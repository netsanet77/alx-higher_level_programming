-- lists all records of the table second_table of the database hbtn_0c_0
-- don't list rows without name
-- the result display with score and name with descending order of score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
