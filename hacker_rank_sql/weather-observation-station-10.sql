-- https://www.hackerrank.com/challenges/weather-observation-station-10
SELECT
    DISTINCT city
FROM
    station
WHERE
    right(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')