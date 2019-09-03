#!/bin/sh

yarn config set cache-folder $YARN_CACHE_FOLDER

(yarn check --integrity && yarn check --verify-tree) || yarn install --frozen-lockfile

# Call command issued to the docker service
exec "$@"
