-- https://www.hackerrank.com/challenges/what-type-of-triangle
SELECT
    CASE
        WHEN (
            A = B
            AND B = C
        ) THEN 'Equilateral'
        WHEN (
            (
                A = B
                AND A + B > C
            )
            OR (
                A = C
                AND A + C > B
            )
            OR (
                C = B
                AND C + B > A
            )
        ) THEN 'Isosceles'
        WHEN (
            (
                A <> B
                AND B <> C
                AND A <> C
            )
            AND (
                A + B > C
                AND A + C > B
                AND C + B > A
            )
        ) THEN 'Scalene'
        ELSE 'Not A Triangle'
    END AS 'IsTriangle'
FROM
    TRIANGLES