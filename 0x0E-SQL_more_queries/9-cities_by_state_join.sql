-- Use of Join command
SELECT c.id, c.name, s.name
FROM cities AS c
JOIN states AS s
ON c.state_id = s.id
ORDER BY c.id ASC;
