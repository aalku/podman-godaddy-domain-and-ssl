FROM docker.io/python:3.11-alpine

RUN python3 -m venv penv
RUN . penv/bin/activate
RUN penv/bin/pip3 install godaddypy

COPY ./godaddy-dns-home.py .

ENV HOST_AND_DOMAIN=host.domain

CMD [ "sh", "-c", "penv/bin/python3 godaddy-dns-home.py \"${HOST_AND_DOMAIN}\"" ]

# sudo podman build --tag godaddy-update-dyn-ip .
# sudo podman run -e HOST_AND_DOMAIN=home.aalku.org -v ./godaddy_credentials.ini:/godaddy_credentials.ini godaddy-update-dyn-ip