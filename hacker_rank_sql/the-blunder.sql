-- https://www.hackerrank.com/challenges/the-blunder
SELECT
    ROUND(AVG(Salary), 0) - ROUND(AVG(REPLACE(Salary, '0', '')), 0)
FROM
    EMPLOYEES