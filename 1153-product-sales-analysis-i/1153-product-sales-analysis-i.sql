# Write your MySQL query statement below
select P.product_name, S.year ,S.price from Product P right join Sales S on P.product_id = S.product_id where S.year is not null ;