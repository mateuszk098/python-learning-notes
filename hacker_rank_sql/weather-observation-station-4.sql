-- https://www.hackerrank.com/challenges/weather-observation-station-4
SELECT
    count(city) - count(DISTINCT(city))
FROM
    station