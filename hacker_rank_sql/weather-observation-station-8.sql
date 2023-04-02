-- https://www.hackerrank.com/challenges/weather-observation-station-8
SELECT
    DISTINCT city
FROM
    station
WHERE
    left(city, 1) IN ('a', 'e', 'i', 'o', 'u')
    AND right(city, 1) IN ('a', 'e', 'i', 'o', 'u')