# Write your MySQL query statement below
WITH unbanned AS (
    SELECT T1.status, T1.request_at
    FROM Trips T1
    JOIN Users U1 ON T1.client_id = U1.users_id
    JOIN Users U2 ON T1.driver_id = U2.users_id
    WHERE U1.banned != 'Yes'
      AND U2.banned != 'Yes'
      AND T1.request_at BETWEEN '2013-10-01' AND '2013-10-03'
)

SELECT request_at AS Day,
       ROUND(SUM(CASE WHEN status like 'cancelled%' THEN 1.00 ELSE 0 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM unbanned
GROUP BY request_at;