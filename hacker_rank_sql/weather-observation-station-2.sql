-- https://www.hackerrank.com/challenges/weather-observation-station-2
SELECT
    round(sum(lat_n), 2) AS 'lat',
    round(sum(long_w), 2) AS 'lon'
FROM
    station