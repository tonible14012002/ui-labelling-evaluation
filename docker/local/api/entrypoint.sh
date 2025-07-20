#!/bin/sh

set -o errexit

set -o pipefail

set -o nounset

# DBUrl="postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=${DB_SSL_MODE}"

# Construct the database URL

# /wait-for-it.sh "${DB_HOST}:${DB_PORT}" --timeout=100
# >&2 echo "DB is available"

/wait-for-it.sh "${REDIS_DSN}" --timeout=100
>&2 echo "REDIS is available"

exec "$@"