-- script that lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT cities.name
from cities, states
WHERE states.id = cities.state_id
AND states.name = 'California'
ORDER BY cties.name DESC;
