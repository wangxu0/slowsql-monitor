import os
import ConfigParser

parser = ConfigParser.ConfigParser()

host = parser.get("database", "host")
port = parser.get("database", "port")
user = parser.get("database", "user")
password = parser.get("database", "password")

interval = parser.get("time", "interval")

use_this_conf = parser.get("monitor", "use_this_conf")
long_query_time = parser.get("monitor", "long_query_time")
log_queries_not_using_indexes = parser.get("monitor", "log_queries_not_using_indexes")

slow_query_log_file = parser.get("log", "slow_query_log_file")

if host and port and user and password and use_this_conf:
    if use_this_conf.upper() == "NO":
        os.system("bash mysql -h " + host + " -P " + port + " -u " + user + " -p " + password +
                  " -e 'source common.sql'")
    elif use_this_conf.upper() == "YES" and long_query_time and log_queries_not_using_indexes:
        os.system("bash mysql -h " + host + " -P " + port + " -u " + user + " -p " + password +
                  " -e 'source common.sql;set global long_query_time=" + long_query_time +
                  ";set session long_query_time=" + long_query_time +
                  ";set global log_queries_not_using_indexes=" + log_queries_not_using_indexes + ";'")
    else:
        print("use_this_conf YES but the section monitor none value")
else:
    print("monitor.conf is illegal")

os.system("bash mysql -h " + host + " -P " + port + " -u " + user + " -p " + password + " -e 'source common.sql'")
parser.set("path", "slow_query_log_file", logFilePath)



