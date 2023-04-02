-- https://www.hackerrank.com/challenges/revising-the-select-query-2
SELECT
    name
FROM
    city
WHERE
    (population > 120000)
    AND (countrycode = 'USA')