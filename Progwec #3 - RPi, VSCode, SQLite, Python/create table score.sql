-- Change History:
-- 2020-03-13/ec:   Initial release.

-- drop table if exists score;

create table score (
    class_number    integer not null,
    student_number  integer not null,
    test_score      real not null,

    primary key (class_number, student_number)
) without rowid;

create index score_class_number on score (class_number);
create index score_student_number on score (student_number);
