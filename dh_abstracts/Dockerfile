FROM public.ecr.aws/docker/library/python:3.9.12-buster

# update the packages
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install cron nginx vim

# remove default nginx site
RUN rm /etc/nginx/sites-enabled/default

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
RUN mkdir -p $APP_HOME/scripts $APP_HOME/data

# Define port and startup script
EXPOSE 80
CMD scripts/entry.ksh

# Move in other assets
COPY package/scripts/entry.ksh $APP_HOME/scripts/entry.ksh
COPY package/scripts/export.ksh $APP_HOME/scripts/export.ksh
COPY package/scripts/migrate.ksh $APP_HOME/scripts/migrate.ksh
COPY package/scripts/install-cron.ksh $APP_HOME/scripts/install-cron.ksh
COPY package/data/crontab $APP_HOME/crontab
COPY package/data/container_bash_profile /root/.profile
COPY package/data/default.conf /etc/nginx/conf.d

# Add the build tag
ARG BUILD_TAG
RUN test -n "$BUILD_TAG" && touch $APP_HOME/buildtag.build-$BUILD_TAG || touch $APP_HOME/buildtag.build-0

#
# end of file
#
