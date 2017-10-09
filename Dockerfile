FROM python:3-alpine
WORKDIR /usr/src/app

COPY . .
RUN apk -U add git && python setup.py sdist bdist_wheel

FROM python:3-alpine
WORKDIR /usr/src/app

# Install build time dependencies for uwsgi
# Install dumb-init
# Remove build time dependencies
# Install runtime dependencies
RUN apk --no-cache add --virtual build-deps \
    build-base linux-headers pcre-dev postgresql-dev && \
    pip install dumb-init psycopg2 && \
    apk del build-deps && \
    apk --no-cache add bash openssl pcre libpq ca-certificates

# COPY tar.gz from build container
# Install it
# TODO: this should be replaced by a build arg to install the correct version from pypi
COPY --from=0 /usr/src/app/dist/. .
RUN bash -c "pip install *"

# add entrypoint
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh

ENTRYPOINT ["/bin/docker-entrypoint.sh"]