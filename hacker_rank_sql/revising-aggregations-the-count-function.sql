-- https://www.hackerrank.com/challenges/revising-aggregations-the-count-function
SELECT
    count(name)
FROM
    city
WHERE
    population > 100000