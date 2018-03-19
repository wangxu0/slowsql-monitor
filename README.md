# slowsql-monitor
Monitor slow sql and inform you of statistical data report

## Overview

Analyze your SQL through the MySQL slow query log and find out which SQL does not meet your expectations, and then you can continue to optimize them until you reach your expectations. You can set related thresholds through some configuration.

![overview](https://github.com/wxisme/slowsql-monitor/blob/master/static/overview.png)

## Document
### Configuration
First configure the MySQL slow query log,you need to log in to the mysql client.
Turn on MySQL slow query log switch:
```sql
show variables like 'slow_query_log';
set global slow_query_log='ON';
```
Set the long query time in seconds:
```sql
show variables like 'long_query_time';
set global long_query_time=1;
```
Set the log queries not using indexes:
```sql
show variables like 'log_queries_not_using_indexes';
set global log_queries_not_using_indexes='ON';
```
If you want a simpler configuration, you can execute `config.sql` directly on the MySQL client.

Some configuration in `monitor.conf`:
Config the mysql_home,if you don't know that you can query with this sql:
```sql
select @@basedir as basePath from dual;
```
Config the log_file_path,if you don't know that you can query with this sql:
```sql
show variables like 'slow_query_log_file';
```
Of course, you can also modify this path, as long as you ensure the same configuration in MySQL and `monitor.conf`.

Finally, you need to fill in the mailing list and mail server information to `monitor.conf` for receiving SQL analysis reports.

### Setup & Test
You can execute the setup.sh script directly to set up scheduled analysis tasks. The default frequency is once per week. You can also set the frequency you need by modifying the crontab expression.
```bash
bash setup.sh
```
Now you can execute some SQL in MySQL to detect if slow query monitoring and report analysis tasks work. If everything is ready you will receive an email with an analysis report.
This is a sample test:

![Test](https://github.com/wxisme/slowsql-monitor/blob/master/static/test.png)
