-- Change History:
-- 2020-03-23/ec:   Initial release.

/* how many rows are there
select count(*) as rec_count
from sensor_log;
*/

/* last few records
select *
from sensor_log
order by log_time desc
limit 20;
*/

/* begin time and end time
select
    min(log_time) as begin_time,
    max(log_time) as end_time
from sensor_log;
*/

/* how many rows in a given date
select count(*) as rec_count
from sensor_log
where date(log_time) = '2020-03-23';
*/

/* temperature distribution
select
    min(temperature) min_temperature,
    max(temperature) max_temperature,
    avg(temperature) avg_temperature
from sensor_log;
*/

/* humidity distribution
select
    min(humidity) min_humidity,
    max(humidity) max_humidity,
    avg(humidity) avg_humidity
from sensor_log;
*/

/* when is the minimum temperature occurred
select
    temperature,
    log_time
from sensor_log
where temperature = (
    select
        min(temperature)
    from sensor_log
);
*/

/* when is the maximum temperature occurred
select
    temperature,
    log_time
from sensor_log
where temperature = (
    select
        max(temperature)
    from sensor_log
);
*/
