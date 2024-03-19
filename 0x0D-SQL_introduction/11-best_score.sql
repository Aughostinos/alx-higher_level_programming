--  a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 
SELECT score, name
From second_table
where score >= 10
order by score DESC
