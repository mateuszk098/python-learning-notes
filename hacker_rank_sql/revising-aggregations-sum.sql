-- https://www.hackerrank.com/challenges/revising-aggregations-sum
SELECT
    sum(population)
FROM
    city
WHERE
    district = 'California'