# Write your MySQL query statement below
Select*
from Cinema 
Where id%2 != 0 AND description != 'boring'
order by rating DESC