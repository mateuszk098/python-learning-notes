-- https://www.hackerrank.com/challenges/population-density-difference
SELECT
    max(population) - min(population)
FROM
    city