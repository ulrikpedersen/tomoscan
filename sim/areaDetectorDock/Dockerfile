##### runtime stage ############################################################

FROM ghcr.io/epics-containers/ioc-adsimdetector-linux-runtime:23.3.4 AS runtime

#copy config folder
COPY config ${IOC}/config

#User created to avoid writing files as root
RUN useradd --shell /bin/bash ioc
USER ioc
