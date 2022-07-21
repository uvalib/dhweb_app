#!/usr/bin/env bash
#
# Docker entry point
#

# make media link if appropriate (done cos Django serves static assets from a location and we want to store these
# elsewhere)
if [ ! -z "${MEDIA_PATH}" ]; then
   if [ ! -d ${STATIC_ASSETS_PATH}/media ]; then
      ln -s ${MEDIA_PATH} ${STATIC_ASSETS_PATH}/media
   fi
fi

# run any pending migrations
scripts/migrate.ksh

# ensure nginx is started
service nginx start

# start the application server
gunicorn -w 2 -b 0.0.0.0:8080 --log-level debug dhweb.wsgi

#
# end of file
#
