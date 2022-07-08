#
# Docker entry point
#

# ensure nginx is started
service nginx start

# start the application server
gunicorn -w 2 -b 0.0.0.0:8080 --log-level debug dhweb.wsgi

#
# end of file
#
