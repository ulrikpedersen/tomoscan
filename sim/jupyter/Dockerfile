#Due to copying a top level file this must be run from the top level directory
FROM jupyter/base-notebook

#Long term this list should somehow be synced with the bluesky pip install list
RUN set -ex && pip install h5py bluesky ophyd ipython matplotlib databroker pyepics area-detector-handlers
RUN mkdir -p ~/.config/databroker
COPY ./mongo.yml /home/jovyan/.config/databroker/mongo.yml