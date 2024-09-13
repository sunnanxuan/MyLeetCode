# Write your MySQL query statement below
select W1.id as id
from
Weather W1 left join Weather W2 on datediff(W1.recordDate,W2.recordDate)=1
where W1.temperature > W2.temperature
