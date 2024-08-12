# Write your MySQL query statement below
Select teacher_id, count(distinct subject_id) cnt
from Teacher
group by teacher_id