#!/usr/bin/dumb-init /bin/bash

export SETTINGS_MODULE=deli_worker.settings
deli_worker $@