
############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu

# Set the file maintainer (your name - the file's author)
MAINTAINER Anastasia Filatova

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    python python-pip gunicorn

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKAPPS )
# Local directory with project source
ENV DOCKAPPS_SRC=.

# Directory in container for all project files
ENV DOCKAPPS_SRVHOME=/srv

# Directory in container for project source files
ENV DOCKAPPS_SRVPROJ=/srv/urlshortener

# Create application subdirectories
WORKDIR $DOCKAPPS_SRVHOME

RUN mkdir media static logs
VOLUME ["$DOCKAPPS_SRVHOME/media/", "$DOCKAPPS_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $DOCKAPPS_SRC $DOCKAPPS_SRVPROJ

# Install Python dependencies 
RUN pip install -r $DOCKAPPS_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKAPPS_SRVPROJ
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]