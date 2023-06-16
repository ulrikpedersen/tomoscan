FROM python:3.10.6-slim

RUN pip install bluesky ophyd ipython matplotlib databroker pyepics

RUN mkdir /code
COPY src/tomoscan/ophyd_inter_setup.py /code/ophyd_inter_setup.py

WORKDIR /code

CMD ["ipython", "-i", "ophyd_inter_setup.py"]
