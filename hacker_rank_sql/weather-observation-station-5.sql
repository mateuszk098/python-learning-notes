-- https://www.hackerrank.com/challenges/weather-observation-station-5
(
    SELECT
        city,
        length(city)
    FROM
        station
    ORDER BY
        length(city) ASC,
        city
    LIMIT
        1
)
UNION
(
    SELECT
        city,
        length(city)
    FROM
        station
    ORDER BY
        length(city) DESC,
        city
    LIMIT
        1
)