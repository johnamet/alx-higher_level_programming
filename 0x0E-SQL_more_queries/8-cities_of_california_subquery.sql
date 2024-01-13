-- lists all cities of california
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states
	WHERE name = 'CALIFORNIA'
	)
ORDER BY id ASC;
