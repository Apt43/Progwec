-- Change History:
-- 2020-03-21/ec:   Initial release.

-- drop table if exists sensor_log

create table sensor_log (
    temperature real not null,
    humidity    real not null,
    log_time    text not null
)
