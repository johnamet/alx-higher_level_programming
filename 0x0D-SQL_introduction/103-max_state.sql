-- displays the max temperature of each state
USE hbtn_0c_0
source temperatures.sql

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
