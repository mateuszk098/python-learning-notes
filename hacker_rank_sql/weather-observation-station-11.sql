-- https://www.hackerrank.com/challenges/weather-observation-station-11
SELECT
    DISTINCT city
FROM
    station
WHERE
    left(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
    OR right(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')