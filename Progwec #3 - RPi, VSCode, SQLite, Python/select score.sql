-- Change History:
-- 2020-03-13/ec:   Initial release.

/* detail
select *
from score
order by student_number, class_number
limit 100;
*/
/* order by average
select
    student_number,
    avg(test_score) average_score
from score
group by student_number
order by 2 desc;
*/
