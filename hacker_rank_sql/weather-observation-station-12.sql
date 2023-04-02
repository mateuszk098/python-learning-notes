-- https://www.hackerrank.com/challenges/weather-observation-station-12
SELECT
    DISTINCT city
FROM
    station
WHERE
    left(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
    AND right(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')