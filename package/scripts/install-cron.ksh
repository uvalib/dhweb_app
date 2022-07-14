#!/usr/bin/env bash

# define the crontab we can load
CRONTAB=/dh-abstracts/crontab

# if we have a crontab available, load it
if [ -f $CRONTAB ]; then
   # load the cron table
   crontab -u root $CRONTAB
fi

#
# start the cron service
#
service cron start

#
# end of file
#
