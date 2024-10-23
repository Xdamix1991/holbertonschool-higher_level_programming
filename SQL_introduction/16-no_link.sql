--script that lists all records of the table second_table


SELECT score, name
from second_table
WHERE name NOT NULL
ORDER BY score DESC;
