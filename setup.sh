#!/usr/bin/env bash
monitor_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )""/monitor/monitor.py"

echo "0 8 * * 1"${monitor_path} >> /var/spool/cron/root

/etc/init.d/cron stop
/etc/init.d/cron start