-- temperature

USE hbtn_0c_0;

source temperatures.sql;

SELECT
    city,
    AVG(value) AS avg_temperature_fahrenheit
FROM
    temperatures
GROUP BY
    city
ORDER BY
    avg_temperature_fahrenheit DESC;
