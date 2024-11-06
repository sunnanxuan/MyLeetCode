# Write your MySQL query statement below
SELECT  customer_id FROM Customer GROUP BY customer_id
having COUNT(distinct product_key)=(SELECT COUNT(product_key) FROM Product)
