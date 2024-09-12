# Write your MySQL query statement below
SELECT DISTINCT(n1) as ConsecutiveNums
FROM (
    SELECT l1.num AS n1,
           l2.num AS n2,
           l3.num AS n3
    FROM Logs l1
    JOIN Logs l2 ON l1.id = l2.id - 1
    JOIN Logs l3 ON l2.id = l3.id - 1
) AS temp
WHERE n1 = n2 AND n2 = n3;