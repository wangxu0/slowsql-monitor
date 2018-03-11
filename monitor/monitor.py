import ConfigParser
import os

parser = ConfigParser.ConfigParser()

os.system("mysql -h localhost -P 3306 -uroot -p123456 -e \"show variables like 'slow_query_log_file;'\"")
