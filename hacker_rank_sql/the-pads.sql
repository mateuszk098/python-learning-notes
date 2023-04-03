-- https://www.hackerrank.com/challenges/the-pads
(
    SELECT
        CONCAT(Name, '(', LEFT(Occupation, 1), ')') AS N
    FROM
        OCCUPATIONS
)
UNION
(
    SELECT
        CONCAT(
            'There are a total of ',
            COUNT(Occupation),
            ' ',
            LOWER(Occupation),
            's.'
        )
    FROM
        OCCUPATIONS
    GROUP BY
        Occupation
    ORDER BY
        COUNT(Occupation),
        Occupation
)
ORDER BY
    N