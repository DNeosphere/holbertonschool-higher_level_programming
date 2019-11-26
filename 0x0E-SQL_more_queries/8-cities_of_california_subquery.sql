--  lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM hbtn_0d_usa.cities
WHERE hbtn_0d_usa.cities.id = (
SELECT hbtn_0d_usa.states WHERE name = 'California'
);
