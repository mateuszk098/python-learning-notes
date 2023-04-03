-- https://www.hackerrank.com/challenges/earnings-of-employees
SELECT
    months * salary AS earnings,
    COUNT(employee_id)
FROM
    Employee
GROUP BY
    earnings
ORDER BY
    earnings DESC
LIMIT
    1