FROM public.ecr.aws/docker/library/python:3.9.12-buster

# update the packages
RUN apt -y update && apt -y upgrade && apt -y install nginx

# Create the run user and group
RUN addgroup --gid 1000 webservice && adduser -q --uid 1000 --gid 1000 --disabled-login webservice

# set the timezone appropriatly
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install the application requirements
COPY dh_abstracts/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Specify home 
ENV APP_HOME /dh-abstracts
WORKDIR $APP_HOME

# install the application
ADD dh_abstracts/app $APP_HOME

# create necessary directories
RUN mkdir -p $APP_HOME/scripts

# Update permissions
RUN chown -R webservice $APP_HOME /home/webservice && chgrp -R webservice $APP_HOME /home/webservice

# Define port and startup script
EXPOSE 8080
CMD package/scripts/entry.ksh

# Move in other assets
COPY package/scripts/entry.ksh $APP_HOME/scripts/entry.ksh
COPY package/data/container_bash_profile /home/webservice/.profile
COPY package/data/default.conf /etc/nginx/conf.d

# Ensure permissions are correct
RUN chown webservice:webservice /home/webservice/.profile $APP_HOME/scripts/entry.ksh && chmod 755 /home/webservice/.profile $APP_HOME/scripts/entry.ksh

# Add the build tag
ARG BUILD_TAG
RUN test -n "$BUILD_TAG" && touch $APP_HOME/buildtag.build-$BUILD_TAG || touch $APP_HOME/buildtag.build-0

# Specify the user
#USER webservice

#
# end of file
#
