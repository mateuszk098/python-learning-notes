-- https://www.hackerrank.com/challenges/japan-population
SELECT
    sum(population)
FROM
    city
WHERE
    countrycode = 'JPN'