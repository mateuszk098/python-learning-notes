-- https://www.hackerrank.com/challenges/revising-aggregations-the-average-function
SELECT
    avg(population)
FROM
    city
WHERE
    district = 'California'