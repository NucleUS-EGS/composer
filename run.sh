#!/bin/bash

# run IDP Proxy
COMMAND="cd idp_proxy; source venv/bin/activate; flask run;"
gnome-terminal --title="IDP Proxy" -- bash -c "$COMMAND"

# run Composer
docker-compose up --build