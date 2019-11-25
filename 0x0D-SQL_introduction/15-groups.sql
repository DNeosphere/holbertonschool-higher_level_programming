-- script that lists the number of records with the same score in the table
SELECT
    score,
    COUNT(score)
FROM
    second_table
GROUP BY score DESC
HAVING COUNT(score) >= 1;
