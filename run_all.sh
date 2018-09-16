#!/usr/bin/env bash

intexit() {
    # Kill all subprocesses (all processes in the current process group)
    kill -HUP -$$
}

hupexit() {
    # HUP'd (probably by intexit)
    echo
    echo "Interrupted"
    exit
}

trap hupexit HUP
trap intexit INT

# start identity provider on port 3000
export FLASK_APP=idp/run.py
python -m flask run -h localhost -p 3000 &

# start toaster service
export FLASK_APP=sp_toaster/run.py
python -m flask run -h localhost -p 4000 &

#start tv service
export FLASK_APP=sp_tv/run.py
python -m flask run -h localhost -p 5000 &

#start policy decision point
pdp/authzforce-ce-restful-pdp-cxf-spring-boot-server-1.3.0.jar &

wait
