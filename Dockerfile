# vim:set ft=dockerfile:
FROM birdhouse/bird-base:latest
MAINTAINER https://github.com/bird-house/emu

LABEL Description="Emu Web Processing Service Application" Vendor="Birdhouse" Version="0.5.3"

# Configure hostname and user for services
ENV OUTPUT_PORT 38094
ENV HOSTNAME localhost

# Set current home
ENV HOME /root

# Copy application sources
COPY . /opt/birdhouse/src/emu

# cd into application
WORKDIR /opt/birdhouse/src/emu

# Provide custom.cfg with settings for docker image
RUN printf "[buildout]\nextends=profiles/docker.cfg" > custom.cfg

# Install system dependencies
RUN bash bootstrap.sh -i && bash requirements.sh

# Set conda enviroment
ENV ANACONDA_HOME /opt/conda
ENV CONDA_ENVS_DIR /opt/conda/envs

# Run install
RUN make clean install

# Volume for data, cache, logfiles, ...
VOLUME /opt/birdhouse/var/lib
VOLUME /opt/birdhouse/var/log

# Ports used in birdhouse
EXPOSE 9001 8094 28094 $OUTPUT_PORT

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon

# Start service ...
CMD ["make", "update-config", "start"]
